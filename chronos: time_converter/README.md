# ⏳ Chronos: Time Manipulation Engine

**Chronos** is an immersive, web-based time conversion application that breaks down raw seconds into a hierarchical, human-readable format: *Years, Months, Weeks, Days, Hours, Minutes, and Seconds*. 

It utilizes pure Python arithmetic (the `divmod()` function) to ensure calculation efficiency and zero mathematical drift, wrapped in a sleek, dark-themed UI.

## 🌟 Features

* **Mathematical Precision:** Employs a cascading `divmod()` logic utilizing a standardized 30-day month and 365-day year model.
* **Cyberpunk / Dark UI:** Custom CSS integration for styled metric cards and a modern dark-mode aesthetic.
* **Interactive Visual Analytics:**
  * **🧬 Lifespan Scale:** Compares your input to an average 2.5-billion-second human lifespan.
  * **📅 Cycle Progress:** Visualizes how close the remaining days are to completing a full 30-day month.
  * **📈 Component Matrix:** A dynamic bar chart showing the relative weight of the extracted time units.

## 🚀 Live Demo

You can try the application live here:streamlit run app.py
👉 **[https://python-projects-app-yl6nzpzwotrqck5ec3ngfq.streamlit.app/]**

## 💻 Local Installation & Setup

Want to run this project on your local machine? Follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-

2. **Install the required dependencies:**
    pip install -r requirements.txt
3.  **Run the Streamlit application:**
    streamlit run app.py

🛠️ Technology Stack
Language: Python 3

Framework: Streamlit

Deployment: Streamlit Community Cloud

Developed by Muhammad Awais.
