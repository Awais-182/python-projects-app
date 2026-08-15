import os
import streamlit as st
from PIL import Image
from google import genai
import plotly.graph_objects as go

# ----------------------------------------------------
# 1. Page & Layout Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="AnimeVision AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Glassmorphism & Vibrant Neon Highlights)
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgba(20, 24, 40, 0.95), rgba(10, 12, 22, 1));
        color: #F0F4F8;
    }
    .main-title {
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FF3366, #BA27FF, #00D4FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        text-align: center;
        color: #A0AEC0;
        margin-bottom: 1.8rem;
    }
    .stat-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }
    .trope-chip {
        display: inline-block;
        background: linear-gradient(135deg, #FF3366, #BA27FF);
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 2. Secure API Key Management
# ----------------------------------------------------
api_key = None
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
elif "GEMINI_API_KEY" in os.environ:
    api_key = os.environ["GEMINI_API_KEY"]

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ App Settings")
    if not api_key:
        api_key = st.text_input(
            "Gemini API Key",
            type="password",
            help="Add GEMINI_API_KEY to your Streamlit Secrets for permanent access."
        )
    else:
        st.success("🔒 API Key loaded securely from Secrets.")

    st.markdown("---")
    enable_fx = st.checkbox("🎉 Enable Celebration Effects", value=True)
    enable_sound = st.checkbox("🔊 Enable Sound Effects", value=True)

# ----------------------------------------------------
# 3. Radar Chart Helper Function
# ----------------------------------------------------
def render_radar_chart():
    categories = ['Power Level', 'Aura / Vibe', 'Visual Design', 'Agility', 'Mystery']
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[88, 92, 95, 84, 90],
        theta=categories,
        fill='toself',
        fillcolor='rgba(186, 39, 255, 0.35)',
        line=dict(color='#00D4FF', width=2),
        name='Character Profile'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], color="#A0AEC0"),
            bgcolor="rgba(0,0,0,0)"
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#F0F4F8"),
        margin=dict(l=30, r=30, t=20, b=20),
        height=280
    )
    return fig

# ----------------------------------------------------
# 4. Header UI
# ----------------------------------------------------
st.markdown('<div class="main-title">⚡ AnimeVision AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Upload any anime character image to detect identity, powers, archetype, and stats.</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# 5. Main Layout
# ----------------------------------------------------
col_upload, col_result = st.columns([1, 1], gap="large")

with col_upload:
    st.markdown("### 📤 Upload Character")
    uploaded_file = st.file_uploader(
        "Choose an anime image (PNG, JPG, JPEG, JFIF, WEBP)", 
        type=["png", "jpg", "jpeg", "jfif", "webp", "bmp"]
    )
    
    if uploaded_file is not None:
        raw_image = Image.open(uploaded_file)
        image = raw_image.convert("RGB")
        st.image(image, caption="Target Character", use_container_width=True)
        analyze_btn = st.button("🚀 Analyze Character", type="primary", use_container_width=True)
    else:
        st.info("💡 Upload an image above to start the analysis.")
        analyze_btn = False

with col_result:
    st.markdown("### 📊 Character Analysis")
    
    if uploaded_file is not None and analyze_btn:
        if not api_key:
            st.error("❌ API key not detected! Please provide your key in Streamlit Secrets or the sidebar.")
        else:
            with st.spinner("🔍 Scanning character traits, powers, and lore..."):
                try:
                    client = genai.Client(api_key=api_key)
                    
                    prompt = """
                    You are an expert anime character identifier and lore specialist.
                    Analyze this anime character image and provide the output formatted strictly with the following sections:

                    ### 🎭 Character Identity
                    * **Character Name:** [Name]
                    * **Anime / Source:** [Anime Series Name]
                    * **Character Archetype / Trope:** [e.g., Shonen Hero, Tsundere, Overpowered Mentor, Kuudere, Anti-Hero]
                    * **Signature Quote / Catchphrase:** "[A classic or generated fitting 1-line quote]"

                    ### ⚡ Powers & Lore
                    * **Powers & Abilities:** [Detailed breakdown]
                    * **Primary Role:** [Protagonist / Antagonist / Deuteragonist / Supporting]
                    * **Short Bio & Backstory:** [2-3 concise, engaging sentences]

                    ### 🎨 Visual & Art Analysis
                    * **Hair & Eye Style:** [Description]
                    * **Aesthetic Vibe:** [e.g., Cyberpunk Dark, Shonen Action, Pastel Fantasy]
                    * **Estimated Anime Lookalikes:** [List 2-3 characters with similar facial designs]
                    """

                    response = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=[image, prompt]
                    )
                    
                    if enable_fx:
                        st.balloons()
                    
                    if enable_sound:
                        st.audio(
                            "https://assets.mixkit.co/active_storage/sfx/2019/2019-preview.mp3",
                            format="audio/mp3",
                            autoplay=True
                        )

                    tab1, tab2 = st.tabs(["📜 Character Dossier", "📈 Power & Stats"])
                    
                    with tab1:
                        st.markdown(response.text)
                    
                    with tab2:
                        st.markdown("#### ⚡ Power Radar & Metrics")
                        st.plotly_chart(render_radar_chart(), use_container_width=True)
                        
                        st.markdown("""
                        <div class="stat-card">
                            <strong>🔥 Power Tier:</strong> <span class="trope-chip">S-Rank</span>
                            <span class="trope-chip">High Aura</span>
                            <span class="trope-chip">Iconic</span>
                        </div>
                        """, unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Error during analysis: {str(e)}")
    elif uploaded_file is None:
        st.markdown(
            """
            <div class="stat-card" style="text-align: center; color: #A0AEC0;">
                <p>Results will appear here after you upload an image and click <strong>Analyze Character</strong>.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
