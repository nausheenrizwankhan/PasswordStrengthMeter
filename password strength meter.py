
# password_strength meter.py
import streamlit as st
import secrets
import string

# Function to generate secure password
def PasswordStrengthMeter(length, use_upper, use_lower, use_digits, use_special):
    characters = ''
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += '!@#$%^&*()_+-=[]{}|;:,.<>?'
    
    if not characters:
        return None  # Return None if no character types are selected
    
    return ''.join(secrets.choice(characters) for _ in range(length))

# Streamlit UI Configuration
st.set_page_config(
    page_title="Password-Strength-Meter",
    page_icon="🔒",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stSlider {
        color: #4CAF50;
    }
    .password-box {
        padding: 1rem;
        background-color: #f0f2f6;
        border-radius: 5px;
        margin: 1rem 0;
        font-family: monospace;
        font-size: 1.2rem;
    }
</style>
""", unsafe_allow_html=True)

# Main Application
st.title("🔐 Password Strength Meter")
st.markdown("---")

# Password Controls
col1, col2 = st.columns(2)
with col1:
    length = st.slider("Password Length", 8, 64, 12, help="Select password length (8-64 characters)")

with col2:
    num_passwords = st.number_input("Number of Passwords", 1, 10, 1, help="Generate multiple passwords at once")

# Character Options
st.subheader("Character Settings")
cols = st.columns(4)
with cols[0]:
    use_upper = st.checkbox("Uppercase (A-Z)", True)
with cols[1]:
    use_lower = st.checkbox("Lowercase (a-z)", True)
with cols[2]:
    use_digits = st.checkbox("Digits (0-9)", True)
with cols[3]:
    use_special = st.checkbox("Special Characters", True)

# Generate Button
if st.button("✨ Generate Secure Passwords"):
    passwords = []
    if not (use_upper or use_lower or use_digits or use_special):
        st.error("Error: At least one character type must be selected.")
    else:
        for _ in range(num_passwords):
            password = PasswordStrengthMeter(length, use_upper, use_lower, use_digits, use_special)
            if password:
                passwords.append(password)
        
        st.success("✅ Passwords generated successfully!")
        st.markdown("---")
        
        for pwd in passwords:
            # Display password with copy button
            col_a, col_b = st.columns([4, 1])
            with col_a:
                st.markdown(f"<div class='password-box'>{pwd}</div>", unsafe_allow_html=True)
            with col_b:
                st.code(pwd)  # Creates copy-able version
                if st.button("Copy", key=pwd):
                    st.experimental_set_query_params(password=pwd)
                    st.success("Copied to clipboard!")
            
# Security Tips
st.markdown("---")
st.subheader("🔒 Security Tips")
st.markdown("""
- Use passwords with at least 12 characters
- Always include multiple character types
- Avoid using personal information
- Use a password manager to store passwords
- Change passwords every 3-6 months
""")

# How to Run
st.sidebar.markdown("## 🚀 How to Use")
st.sidebar.markdown("""
1. Select password length
2. Choose character types
3. Click Generate
4. Copy your secure password
""")


st.write("Build With ❤️ by [NausheenRizwanKhan]")