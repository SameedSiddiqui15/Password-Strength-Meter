import re
import streamlit as st

st.set_page_config(page_title="Password Strength Meter By Sameed Siddiqui",page_icon="🔑",layout="centered")

st.markdown("""
    <style>
    .main { text-align: center; }
    .stTextInput { width: 100% !important; margin: auto; }
    .stButton button { 
        width: 50%; 
        background-color: #4CAF50; 
        color: white; 
        font-size: 18px; 
    }
    .stButton button:hover { 
        background-color: #45a049; 
    }
</style>
""",unsafe_allow_html=True)
 
st.title("Password Strength Generator By Sameed Siddiqui🔐")
st.write("✍🏼 Type your password below to evaluate its strength.")

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) > 7 :
        score += 1
    else :
        feedback.append("❌ Password Should be **atleast Eight character Long**.")

    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score += 1
    else :
        feedback.append("❌ Password Should include **Both Upper Case (A-Z) & Lower Case (a-z) letter**.")

    if re.search(r"\d",password):
        score += 1 
    else:
        feedback.append("❌ Password Should be **atleast One Number (0-9)**.")

    if re.search(r"[!@#$%^&*]" ,password):
        score += 1 
    else:
        feedback.append("❌ Password Should be **atleast One Special Character (!@#$%^&*)**.")

    if not re.search(r"(.)\1{2,}", password):
        score += 1
    else:
        feedback.append("❌ Password should **avoid consecutive repeating characters (e.g., 'aaa' or '111')**.")

    if score == 5:
        st.success("✅ All Set! **Strong Password - Your password is secure.**")
    elif score == 4:
        st.info("⚠️ **Moderate Password** - Enhance security by adding extra protection.")
    elif score == 3:
        st.warning("⚠️ **Weak Password** - Consider improving it for better security.")
    else:
        st.error("❌ **Very Weak Password** - Your password is highly vulnerable! Change it immediately.")

    if feedback:
        with st.expander(" **Improve You Password** "):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter Your Password:" , type="password", help="Ensure That Your Password Is strong 🔒")

if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please Enter a Password First!")
