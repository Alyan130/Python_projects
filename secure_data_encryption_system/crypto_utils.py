import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import hashlib
import hmac

def pbkdf2_hash(passkey: str, salt: bytes = None):
    if not salt:
        salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac(
        'sha256',
         passkey.encode(),
         salt,
         100000,
    )
    return base64.b64encode(hashed).decode(), base64.b64encode(salt).decode()


def verify_password(passkey: str, hashed_password: str, salt: str) -> bool:
    test_hash = pbkdf2_hash(passkey, base64.b64decode(salt))
    
    if isinstance(test_hash, tuple):
        test_hash = test_hash[0] 
    
    return hmac.compare_digest(test_hash, hashed_password)


def derive_key_from_password(password: str, salt: bytes = None):
    if salt is None:
        salt = os.urandom(16)

    kdf =PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt


def encrypt_text(text: str, password: str):
    key, salt = derive_key_from_password(password)
    cipher = Fernet(key)
    encrypted = cipher.encrypt(text.encode())
    
    return {
        'encrypted': base64.b64encode(encrypted).decode(),
        'salt': base64.b64encode(salt).decode()
    }


def decrypt_text(encrypted_data: dict, password: str):
    encrypted = base64.b64decode(encrypted_data['encrypted'])
    salt = base64.b64decode(encrypted_data['salt'])
    
    key, _ = derive_key_from_password(password, salt)
    cipher = Fernet(key)
    
    decrypted = cipher.decrypt(encrypted)
    return decrypted.decode()