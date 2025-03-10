import re
import streamlit as st
import string
import random

st.set_page_config(page_title="Password Strength meter", page_icon="",layout="centered" )
st.title(":orange[Password Strength Meter]")
st.subheader("Check your password strength and get suggestions!")
st.divider()

blacklist_passwords = ["password", "password123", "123456", "admin", "qwerty", "letmein", "welcome", "abc123", "123123"]

if "passwords" not in st.session_state:
  st.session_state.passwords = [] 

if "blacklist" not in st.session_state:
  st.session_state.blacklist = [] 


def suggest_password():
   characters=(
     random.choices(string.ascii_uppercase,k=2) +
     random.choices(string.ascii_lowercase,k=4) +
     random.choices(string.digits,k=3) +
     random.choices("!@#$%^&*",k=3) 
   )
   random.shuffle(characters)
   return "".join(characters)


def check_password_strength(password):
    score:int=0
    suggestion:list[str]=[]
   

    if len(password)>=8:
        score+=1
    else:
        suggestion.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score+=1
    else:
        suggestion.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d",password):
        score+=1
    else:
        suggestion.append("❌ Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        print("❌ Include at least one special character (!@#$%^&*).")

    return score,suggestion


password = st.text_input(label="Enter your password:",max_chars=20,)

if st.button("Check password"):
   st.session_state.passwords.append(password)       
   score,suggestion = check_password_strength(password)
   

   st.subheader(f"Feedback for your Password : ")
   if password.lower() in blacklist_passwords:
      st.session_state.blacklist.append(password)
      st.error("❌ This password is blacklisted because it is too common!")
   elif score==4:
      st.success("✅ Strong Password!")
   elif  score==3:
      st.warning("⚠️ Moderate Password - Consider adding more security features.") 
   else:
      st.error("❌ Weak Password - Improve it using the suggestions below.")


   with st.container(border=True):
      st.subheader("Suggestions for password:")
      if len(suggestion)==0:
          st.success("Your password is strong! need no suggestions")
      else: 
         for i in suggestion:
            st.warning(i)
        
         suggested_pass = suggest_password()
         st.subheader(f"Suggested Password: :orange[{suggested_pass}]")

    

   with st.sidebar:
      with st.spinner():
        st.header(":orange[Password History:]")
        for i in st.session_state.passwords:
            st.markdown(i)
        st.header(":orange[Black Listed Passwords:]")
        for i in st.session_state.blacklist:
            st.markdown(i)