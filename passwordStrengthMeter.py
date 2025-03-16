import re
import streamlit as st

st.set_page_config(page_title="Password Strength Meter By Sameed Siddiqui",page_icon="🔑",layout="centered")

st.markdown("""
    <style>
    /* Center the main container */
    .main { 
        text-align: center; 
        padding: 20px;
    }

    /* Input Field Styling */
    .stTextInput { 
        width: 100% !important; 
        max-width: 500px;/* Limits width on larger screens */
        margin : auto;
        padding: 12px;
        font-size: 16px;
        border: 2px solid #ccc;
        border-radius: 8px;
        transition: 0.3s ease-in-out;
    }

    /* Input Field Hover & Focus */
    .stTextInput:hover, .stTextInput:focus {
        border-color: #4CAF50;
        box-shadow: 0 0 8px rgba(76, 175, 80, 0.5);
        outline: none;
    }

    /* Button Styling */
    .stButton button { 
        width: 60%; 
        max-width: 300px; 
        background: linear-gradient(135deg, #4CAF50, #2E7D32); 
        color: white; 
        font-size: 18px; 
        font-weight: bold;
        padding: 12px;
        border-radius: 8px;
        transition: 0.3s ease-in-out;
        border: none;
        cursor: pointer;
    }

    /* Button Hover Effect */
    .stButton button:hover { 
        background: linear-gradient(135deg, #2E7D32, #4CAF50); 
        transform: scale(1.05);
        color: white;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .stTextInput, .stButton button {
            width: 80%;  /* Adjust width on smaller screens */
        }
    }

    @media (max-width: 480px) {
        .stTextInput, .stButton button {
            width: 90%;  
            font-size: 16px; /* Reduce font size for small screens */
        }
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
