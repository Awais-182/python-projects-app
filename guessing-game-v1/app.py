import streamlit as st
import random

# App Title & Description
st.title("🎯 Number Guessing Game (v1.0)")
st.write("Welcome! I have picked a secret number between **1 and 100**. Can you guess what it is?")

# Initialize the secret number and attempt count in Streamlit's memory
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0

# Number input widget (replaces standard input())
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, value=50)

# Submit Button
if st.button("Check Guess"):
    st.session_state.attempts += 1
    
    if user_guess < st.session_state.secret_number:
        st.warning("📉 Too low! Try guessing higher.")
    elif user_guess > st.session_state.secret_number:
        st.warning("📈 Too high! Try guessing lower.")
    else:
        st.balloons()  # Fun celebration animation!
        st.success(f"🎉 Spot on! You guessed it in {st.session_state.attempts} attempts.")

# Reset Button to start a new game
if st.button("🔄 Play Again"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.rerun()
