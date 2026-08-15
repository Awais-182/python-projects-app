# ⚡ AnimeVision AI

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://python-projects-app-sxbbemit4knqkgsruqdgj4.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-4285F4?logo=google&logoColor=white)](https://ai.google.dev/)
[![Plotly](https://img.shields.io/badge/Visualization-Plotly-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/)

> **Upload an anime character image and let AI analyze its identity, abilities, lore, and visual style.**

## 🚀 Live Demo

**[⚡ Try AnimeVision AI](https://python-projects-app-sxbbemit4knqkgsruqdgj4.streamlit.app/)**

---

## 🌟 Overview

**AnimeVision AI** is a multimodal AI web application built with **Python, Streamlit, and Google Gemini**.

Users can upload an anime character image and receive an AI-generated character dossier containing identity, anime/source, archetype, powers, role, backstory, and visual characteristics. The app also includes an interactive character-statistics section powered by Plotly.

---

## ✨ Features

- 🔍 **AI Character Analysis** — character name, anime/source, archetype, role, powers, abilities, and backstory.
- 🎨 **Visual Analysis** — hair and eye style, aesthetic vibe, and visual similarities.
- 📊 **Power Radar** — interactive five-axis radar visualization using Plotly.
- 🖼️ **Multiple Image Formats** — PNG, JPG, JPEG, JFIF, WEBP, and BMP.
- 🎉 **Interactive Effects** — optional celebration balloons and sound effects.
- 🔐 **Secure API Key Handling** — supports Streamlit Secrets, environment variables, and sidebar input.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Application logic |
| **Streamlit** | Web interface |
| **Google Gemini** | Multimodal AI analysis |
| **Google GenAI SDK** | Gemini API integration |
| **Pillow** | Image processing |
| **Plotly** | Character-stat visualization |

---

## 📁 Project Structure

```text
anime-vision-ai/
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
```

---

## 💻 Installation (Run Locally)

### 1. Clone the repository

```bash
git clone https://github.com/Awais-182/python-projects-app.git
cd python-projects-app/anime-vision-ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the Gemini API key

For the deployed Streamlit app, add your key through **Streamlit Cloud → App Settings → Secrets**:

```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
```

For local use, you can either set `GEMINI_API_KEY` as an environment variable or enter it through the app's sidebar when prompted.

> 🔒 **Never commit your API key to GitHub.**

### 4. Run the app

```bash
streamlit run app.py
```

---

## ⚠️ Note

AnimeVision AI uses generative AI, so character identification, lore, and other generated details may not always be accurate.

The current radar-chart values and labels such as **S-Rank**, **High Aura**, and **Iconic** are predefined in the application and are not dynamically calculated from Gemini's response.

---

## 🔮 Future Improvements

- [ ] Dynamic AI-generated character statistics
- [ ] Character comparison
- [ ] Confidence scores for identification
- [ ] Downloadable character reports
- [ ] Improved anime/source verification

---

## 👨‍💻 Author

**Awais**

[![GitHub](https://img.shields.io/badge/GitHub-Awais--182-181717?logo=github&logoColor=white)](https://github.com/Awais-182)

---

⭐ **If you like the project, try the live demo and explore the repository!**
