from crypto_utils import pbkdf2_hash , verify_password
from storage_utils import load_data, save_data


def register_user(username:str,passkey:str):
  data = load_data()
  if username in data:
    return False,"User already registered!"
  
  hash, salt = pbkdf2_hash(passkey)

  data[username] = {
    "password": hash,
     "salt": salt,
     "encryptions":[], 
  }
  save_data(data)
  return True, "User registered sucessfully!"


def login_user(username:str, passkey:str):
  data = load_data()
  if username not in data:
    return False,"Login failed user not registered!"
  user = data[username]
  password_valid = verify_password(passkey,user["password"],user["salt"])
  if password_valid:
    return True,"User login successfully..."
  else:
    return False, "Incorrect password"