


import re
import streamlit as st  

st.set_page_config(page_title="🔐 Password Strength Checker", page_icon="🔑", layout="centered")

# Custom CSS 
st.markdown("""
    <style>
       
        body, .stApp {
            background: linear-gradient(to right, #A1C4FD, #C2E9FB) !important;
            color: black;
        }

        .main-container { 
            text-align: center; 
            font-family: Arial, sans-serif; 
        }

        
        .stTextInput > div > div > input { 
            width: 70%; 
            margin: auto; 
            padding: 10px; 
            font-size: 16px; 
            text-align: center; 
        }

       
        .stButton { display: flex; justify-content: center; }
.stButton > button {
    background: linear-gradient(to right, #C2E9FB,#D8BFD8   );
    color: black;
    font-size: 18px;
    padding: 12px 20px;
    border-radius: 10px;
    border: none;
    width: 60%;
    max-width: 300px;
    transition: all 0.4s ease-in-out;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
}


.stButton > button:hover {
    background: linear-gradient(to right,  #D8BFD8, #9370DB);
    transform: scale(1.05);
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
}
    </style>
""", unsafe_allow_html=True)

# Page Title and Description
st.markdown("<h1 style='text-align: center; color: black;'>🔑 Password Strength Checker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px; color: black;'>🛡️ Check password strength based on length, uppercase/lowercase letters, digits, and special characters. Provides real-time feedback and improvement suggestions. 💡</p>", unsafe_allow_html=True)

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("📏 Your password should be at least **8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔠 Use a mix of **uppercase & lowercase letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔢 Include at least **one number** (0-9) in your password.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔣 Add at least **one special character** (!@#$%^&*) for extra security.")

    # Display Password Strength Result
    if score == 4:
        st.success("🚀 Your password is **Strong**! Great job! 🔥")
    elif score == 3:
        st.info("⚠️ Your password is **Moderate**! Add more security features to make it stronger. 🔒")
    else:
        st.error("❌ Weak Password! Improve your security by following the tips below. 🔐")

    # Display Improvement Suggestions
    if feedback:
        with st.expander("💡 Improve Your Password"):
            st.markdown('<div class="suggestion-box">', unsafe_allow_html=True)
            for item in feedback:
                st.write("✅ " + item)
            st.markdown('</div>', unsafe_allow_html=True)

# Input field for password
password = st.text_input("🔏 Enter your password:", type="password", help="Make sure to use a strong password to stay secure.")

# Button
st.markdown("<br>", unsafe_allow_html=True)  
if st.button("🔍 Check Password"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
