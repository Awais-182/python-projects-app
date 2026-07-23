import random
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Guess the Number Game", page_icon="🎮", layout="centered")

st.title("🎮 Guess the Number: Web Edition")
st.caption("A Python-powered game with dynamic scoring and state management.")

DIFFICULTY_CONFIG = {
    "Easy": {"max_range": 50, "attempts": 10, "multiplier": 1},
    "Medium": {"max_range": 100, "attempts": 7, "multiplier": 2},
    "Hard": {"max_range": 200, "attempts": 5, "multiplier": 3}
}

if "total_score" not in st.session_state:
    st.session_state.total_score = 0

if "game_over" not in st.session_state:
    st.session_state.game_over = False

def start_new_game(difficulty_key):
    config = DIFFICULTY_CONFIG[difficulty_key]
    st.session_state.difficulty = difficulty_key
    st.session_state.secret_number = random.randint(1, config["max_range"])
    st.session_state.attempts_left = config["attempts"]
    st.session_state.game_over = False

if "secret_number" not in st.session_state:
    start_new_game("Easy")

with st.sidebar:
    st.header("⚙️ Game Settings")
    selected_diff = st.selectbox(
        "Select Difficulty Level:",
        options=list(DIFFICULTY_CONFIG.keys()),
        index=list(DIFFICULTY_CONFIG.keys()).index(st.session_state.get("difficulty", "Easy"))
    )
    if st.button("🔄 New Game / Reset"):
        start_new_game(selected_diff)
    st.markdown("---")
    st.metric(label="🏆 Total Score", value=st.session_state.total_score)

current_config = DIFFICULTY_CONFIG[st.session_state.difficulty]

col1, col2 = st.columns(2)
with col1:
    st.info(f"**Range:** 1 to {current_config['max_range']}")
with col2:
    st.warning(f"**Attempts Left:** {st.session_state.attempts_left}")

if not st.session_state.game_over:
    with st.form(key="guess_form", clear_on_submit=True):
        user_guess = st.number_input(
            "Enter your guess:",
            min_value=1,
            max_value=current_config["max_range"],
            step=1
        )
        submit_button = st.form_submit_button(label="Submit Guess")

    if submit_button:
        if user_guess == st.session_state.secret_number:
            points_won = st.session_state.attempts_left * current_config["multiplier"]
            st.session_state.total_score += points_won
            st.session_state.game_over = True
            st.balloons()
            st.success(f"🎉 **Correct!** The number was {st.session_state.secret_number}. You scored **+{points_won}** points!")
        else:
            st.session_state.attempts_left -= 1
            if st.session_state.attempts_left > 0:
                hint = "📈 Too High!" if user_guess > st.session_state.secret_number else "📉 Too Low!"
                st.error(f"{hint} Try again.")
            else:
                st.session_state.game_over = True
                st.error(f"💀 **Game Over!** You ran out of attempts. The secret number was **{st.session_state.secret_number}**.")
else:
    st.info("Click **'New Game / Reset'** in the sidebar to play another round!")
