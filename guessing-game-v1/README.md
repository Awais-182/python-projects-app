# 🎯 Number Guessing Game — Streamlit App

An interactive, web-based Number Guessing Game built with Python and Streamlit. Test your intuition against the computer in a clean, real-time UI!

🚀 [Click Here to Play the Live App!](https://python-projects-app-522mr7fymyhcwf4bm2hjbg.streamlit.app/)

---

## 👤 Author & Developer

- Developer: Muhammad Awais ([@Awais-182](https://github.com/Awais-182))

---

## ✨ Features

- Dynamic Feedback: Instant visual cues indicating whether your guess is too high, too low, or correct.
- Attempt Tracking: Keeps track of how many turns you take to guess the right number.
- Session State Management: Clean resets and persistent game states powered by Streamlit.
- Responsive Layout: Works smoothly on desktop, tablet, and mobile browsers.

---

## ⚡ Advantages

- Zero Installation Needed: Users can play the game directly in their browser via Streamlit Cloud without needing Python installed locally.
- Real-Time Interactivity: Instant response upon submitting guesses without requiring page reloads.
- Clean UI: Built with modern, user-friendly components instead of a plain command-line interface (CLI).

---

## ⚠️ Limitations

- Single Session Memory: Refreshing or closing the browser tab resets the current game state and target number.
- Single-Player Only: Designed for individual users; does not support multi-player leaderboards or global high scores.
- Fixed Range: The target random number range is fixed (e.g., 1 to 100) unless adjusted in the source code.

---

## 🛠️ Tech Stack & Tools

- Language: Python
- Framework: Streamlit
- Core Library: random (for target number generation)

---

## 🚀 Local Setup & Installation

To clone and run this project locally on your machine:

1. Clone the repository:
   git clone https://github.com/Awais-182/python-projects-apps.git
   cd python-projects-apps/guessing-game-v1

2. Install dependencies:
   pip install streamlit

3. Run the application:
   streamlit run app.py

---

## 📁 Project Structure

guessing-game-v1/
├── app.py          # Main Streamlit web application script
└── README.md       # Project documentation, credits & live link
