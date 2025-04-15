import streamlit as st
from crypto_utils import pbkdf2_hash, verify_password, encrypt_text, decrypt_text
from storage_utils import load_data, save_data
from auth_utils import register_user, login_user
import time


st.set_page_config(page_title='Secure Data System', layout='centered')

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "username" not in st.session_state:
    st.session_state["username"] = ""

if "user_attempts" not in st.session_state:
    st.session_state["user_attempts"] = {} 

header_container = st.container()
st.markdown("""
    <style>
    div.stButton button {
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

left_col, right_col = header_container.columns([4, 1])

with right_col:
    if st.session_state.logged_in:
     if st.button("Logout"):
        st.session_state.clear()

with left_col:
    st.title("Secure Data System 🔑")
    st.divider()


menu=["Login", "Register","Store Data","Retrieve Data"]
choice = st.sidebar.selectbox("Menu", menu)

match choice:
  case "Login":
     st.header("Login into your account 📳")
     user_name = st.text_input("Enter your name:")
     password = st.text_input("Enter your password:", type="password")
       
     if user_name and user_name not in st.session_state["user_attempts"]:
         st.session_state["user_attempts"][user_name] = {"count": 0, "lock_until": 0}
     
     if user_name and user_name in st.session_state["user_attempts"]:
         user_data = st.session_state["user_attempts"][user_name]
         time_remaining = user_data.get("lock_until") - time.time()
          
         if time_remaining > 0:
           st.warning(f"⏳ Too many failed attempts. Try again in {int(time_remaining)} seconds.")
           st.stop()    
         elif user_data.get("lock_until", 0) > 0: 
           st.session_state["user_attempts"][user_name]["count"] = 0
           st.session_state["user_attempts"][user_name]["lock_until"] = 0
        
     if st.button("Login"):
        if user_name:
           success, msg = login_user(user_name, password)
           if success:
              st.success(msg)
              st.session_state["logged_in"] = True
              st.session_state["username"] = user_name
              st.session_state["password"] = password

              if user_name in st.session_state["user_attempts"]:
                st.session_state["user_attempts"][user_name]["count"] = 0
           else:
              if msg == "Login failed user not registered!":
                 st.error(msg)
              else:
                 st.session_state["user_attempts"][user_name]["count"] += 1
                 attempts = st.session_state["user_attempts"][user_name]["count"]
                        
                 if attempts >= 3:
                    lock_duration = 60
                    st.session_state["user_attempts"][user_name]["lock_until"] = time.time() + lock_duration
                    st.error(f"Too many failed attempts. Account locked for {lock_duration} seconds.")
                 else:
                    remaining = 3 - attempts
                    st.error(f"{msg} | Attempts remaining: {remaining}")
        else:
           st.error("Please enter your username and password")


  case "Register":
     st.header("Register New Account 🙍‍♂️ ")
     user_name= st.text_input("Enter your name:")
     password = st.text_input("Enter your password:", type="password")
     if st.button("Register"):
       register, msg = register_user(user_name, password)
       if register:
         st.success(msg)
       else:
         st.error(msg)


  case "Store Data":
      st.subheader("Encrypt and store your data 📦")
      if not st.session_state["logged_in"]:
         st.warning("Login first to encrypt and store data")
         st.stop()
      
      data_input = st.text_area("Enter text:",height=150)
      encryption_passkey = st.text_input("Enter encryption passkey:", type="password")
      
      if st.button("encrypt"):
         if data_input and encryption_passkey:
           encrypted = encrypt_text(data_input, encryption_passkey)
           db = load_data()
           db[st.session_state.username]["encryptions"].append(encrypted)
           save_data(db)
           st.success("Data encrypted and stored successfully!")
         else:
            st.warning("Enter both text and encryption passkey!")
        

  case "Retrieve Data":
     st.subheader("Retrieve your data 🔓")
     if not st.session_state["logged_in"]:
        st.warning("Login first to retrieve data") 
        st.stop()
        
     db = load_data()
     user_encryptions = db[st.session_state.username]["encryptions"]
        
     if not user_encryptions:
        st.warning("No data to show!")
        
     for index, encryption in enumerate(user_encryptions):
        with st.expander(f"Encryption {index + 1}"):
           decryption_passkey = st.text_input(f"Enter decryption passkey for item {index + 1}:",    type="password", key=f"passkey_{index}")
                
           if st.button(f"Decrypt", key=f'button{index+1}'):
               if not decryption_passkey:
                 st.error("Please enter your decryption passkey")
                 continue
                   
               try:
                 decrypted_text = decrypt_text(encryption, decryption_passkey)
                 st.session_state[f"decrypted_text_{index}"] = decrypted_text
                 st.success(st.session_state[f"decrypted_text_{index}"])
               except Exception as e:
                 st.error(f"Decryption failed. Incorrect passkey or corrupted data.")
        