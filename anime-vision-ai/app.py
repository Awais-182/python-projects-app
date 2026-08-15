import os
import json
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

with st.sidebar:
    st.header("⚙️ App Settings")
    if not api_key:
        api_key = st.text_input(
            "Gemini API Key",
            type="password",
            help="Add GEMINI_API_KEY to your Streamlit Secrets for permanent access."
        )
    else:
        st.success("🔒 API Key loaded securely.")

    st.markdown("---")
    enable_fx = st.checkbox("🎉 Enable Celebration Effects", value=True)
    enable_sound = st.checkbox("🔊 Enable Sound Effects", value=True)

# ----------------------------------------------------
# 3. Dynamic Radar Chart Function
# ----------------------------------------------------
def render_radar_chart(stats):
    categories = ['Power Level', 'Aura / Vibe', 'Visual Design', 'Agility', 'Mystery']
    values = [
        stats.get('power_level', 80),
        stats.get('aura_vibe', 85),
        stats.get('visual_design', 90),
        stats.get('agility', 75),
        stats.get('mystery', 70)
    ]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
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
                    Analyze this anime character and output a strictly valid JSON object matching this schema:
                    {
                        "character_name": "string",
                        "anime_source": "string",
                        "archetype": "string",
                        "signature_quote": "string",
                        "primary_role": "string",
                        "powers_and_abilities": "string",
                        "bio_backstory": "string",
                        "hair_and_eye_style": "string",
                        "aesthetic_vibe": "string",
                        "lookalikes": "string",
                        "power_level": int (10-100),
                        "aura_vibe": int (10-100),
                        "visual_design": int (10-100),
                        "agility": int (10-100),
                        "mystery": int (10-100),
                        "power_tier": "string (e.g. S-Rank, Special Grade, High-Human, A-Rank)"
                    }
                    Ensure the numeric ratings accurately reflect this specific character's canonical strength and lore.
                    """

                    response = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=[image, prompt],
                        config={"response_mime_type": "application/json"}
                    )
                    
                    data = json.loads(response.text)
                    
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
                        st.markdown(f"""
                        ### 🎭 Character Identity
                        * **Character Name:** {data.get('character_name', 'Unknown')}
                        * **Anime / Source:** {data.get('anime_source', 'Unknown')}
                        * **Archetype / Trope:** {data.get('archetype', 'N/A')}
                        * **Signature Quote:** *"{data.get('signature_quote', '...')}"*

                        ### ⚡ Powers & Lore
                        * **Primary Role:** {data.get('primary_role', 'N/A')}
                        * **Powers & Abilities:** {data.get('powers_and_abilities', 'N/A')}
                        * **Bio & Backstory:** {data.get('bio_backstory', 'N/A')}

                        ### 🎨 Visual & Art Analysis
                        * **Hair & Eye Style:** {data.get('hair_and_eye_style', 'N/A')}
                        * **Aesthetic Vibe:** {data.get('aesthetic_vibe', 'N/A')}
                        * **Anime Lookalikes:** {data.get('lookalikes', 'N/A')}
                        """)
                    
                    with tab2:
                        tier_label = data.get('power_tier', 'S-Rank')
                        st.markdown(f"#### ⚡ Power Radar: **{tier_label}**")
                        st.plotly_chart(render_radar_chart(data), use_container_width=True)
                        
                        col_m1, col_m2 = st.columns(2)
                        with col_m1:
                            st.metric("Combat Power", f"{data.get('power_level', 50)} / 100")
                            st.metric("Aura Rating", f"{data.get('aura_vibe', 50)} / 100")
                        with col_m2:
                            st.metric("Agility Speed", f"{data.get('agility', 50)} / 100")
                            st.metric("Design Impact", f"{data.get('visual_design', 50)} / 100")
                            
                        st.markdown(f"""
                        <div class="stat-card">
                            <strong>🔥 Evaluated Tier:</strong> <span class="trope-chip">{tier_label}</span>
                            <span class="trope-chip">Mystery: {data.get('mystery', 50)}%</span>
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
