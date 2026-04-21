import streamlit as st
from PIL import Image
from api_calling import generate_response
import base64

def get_base64_image(image_path: str) -> str:
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_image = get_base64_image("background.png")

st.set_page_config(page_title="Medi Bondhu", page_icon="💊", layout="centered")

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300&display=swap');

    :root {{
        --green-deep:   #0d3d2f;
        --green-mid:    #1a5c45;
        --green-light:  #2a7d5f;
        --green-accent: #3fb489;
        --green-glow:   #5dd4a8;
        --cream:        #f0f7f4;
        --white:        #ffffff;
        --card-bg:      rgba(255,255,255,0.10);
        --card-border:  rgba(255,255,255,0.18);
        --shadow:       0 8px 40px rgba(0,0,0,0.25);
        --text-main:    #e8f5ef;
        --text-muted:   rgba(232,245,239,0.65);
    }}

    /* ── Global font ── */
    html, body,
    [data-testid="stAppViewContainer"],
    [data-testid="stSidebar"],
    .stMarkdown, .stButton, .stSpinner,
    h1, h2, h3, h4, h5, h6,
    p, span, div, label, input, textarea {{
        font-family: 'Sora', sans-serif !important;
    }}

    /* ── Background ── */
    [data-testid="stAppViewContainer"] {{
        background-image:
            radial-gradient(ellipse at 20% 30%, rgba(63,180,137,0.18) 0%, transparent 55%),
            radial-gradient(ellipse at 80% 70%, rgba(26,92,69,0.22) 0%, transparent 55%),
            url("data:image/png;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* ── Main overlay ── */
    [data-testid="stMain"] {{
        background: linear-gradient(
            160deg,
            rgba(10, 40, 28, 0.72) 0%,
            rgba(13, 61, 47, 0.65) 100%
        );
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
    }}

    /* ── Block container: centered with breathing room from toolbar ── */
    .block-container {{
        max-width: 760px !important;
        padding: 5rem 2rem 4rem !important;
        margin: 0 auto !important;
    }}

    /* ── Hero section ── */
    .hero-wrap {{
        text-align: center;
        padding: 2.8rem 2rem 2rem;
        background: linear-gradient(135deg, rgba(255,255,255,0.09) 0%, rgba(255,255,255,0.04) 100%);
        border: 1px solid var(--card-border);
        border-radius: 24px;
        box-shadow: var(--shadow), inset 0 1px 0 rgba(255,255,255,0.12);
        margin-bottom: 2rem;
        backdrop-filter: blur(6px);
    }}

    .hero-badge {{
        display: inline-block;
        background: linear-gradient(90deg, var(--green-accent), var(--green-glow));
        color: var(--green-deep) !important;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        padding: 0.3rem 0.85rem;
        border-radius: 100px;
        margin-bottom: 1.1rem;
        text-shadow: none !important;
    }}

    .hero-title {{
        font-size: clamp(1.9rem, 5vw, 2.9rem) !important;
        font-weight: 700 !important;
        letter-spacing: -0.03em;
        color: var(--white) !important;
        text-shadow: 0 2px 24px rgba(0,0,0,0.35) !important;
        line-height: 1.15;
        margin-bottom: 0.5rem !important;
    }}

    .hero-title span {{
        background: linear-gradient(90deg, var(--green-accent), var(--green-glow));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: none !important;
        color: unset !important;
    }}

    .hero-sub {{
        font-size: 0.95rem !important;
        color: var(--text-muted) !important;
        text-shadow: none !important;
        max-width: 480px;
        margin: 0 auto 0.4rem !important;
        font-weight: 300;
        line-height: 1.6;
    }}

    .hero-divider {{
        width: 48px;
        height: 3px;
        background: linear-gradient(90deg, var(--green-accent), var(--green-glow));
        border-radius: 4px;
        margin: 1.2rem auto 0;
        border: none;
    }}

    /* ── Upload card ── */
    [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {{
        background: linear-gradient(135deg, rgba(255,255,255,0.09) 0%, rgba(255,255,255,0.04) 100%);
        border: 1px solid var(--card-border);
        border-radius: 20px;
        padding: 1.8rem 1.8rem 1.5rem !important;
        box-shadow: var(--shadow);
        backdrop-filter: blur(4px);
    }}

    /* ── Section headings ── */
    h2 {{
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        color: var(--white) !important;
        text-shadow: none !important;
        letter-spacing: -0.01em;
    }}

    h3 {{
        font-size: 0.88rem !important;
        font-weight: 400 !important;
        color: var(--text-muted) !important;
        text-shadow: none !important;
        letter-spacing: 0.01em;
        margin-top: -0.4rem !important;
    }}

    /* ── File uploader ── */
    [data-testid="stFileUploader"] {{
        background: rgba(255,255,255,0.06) !important;
        border: 1.5px dashed rgba(93,212,168,0.35) !important;
        border-radius: 14px !important;
        padding: 0.6rem 1rem !important;
        transition: border-color 0.2s, background 0.2s;
    }}

    [data-testid="stFileUploader"]:hover {{
        border-color: rgba(93,212,168,0.65) !important;
        background: rgba(255,255,255,0.09) !important;
    }}

    [data-testid="stFileUploader"] span,
    [data-testid="stFileUploader"] p,
    [data-testid="stFileUploaderDropzone"] * {{
        color: var(--text-muted) !important;
        text-shadow: none !important;
        font-size: 0.85rem !important;
    }}

    /* ── "Browse files" button inside uploader ── */
    [data-testid="stFileUploaderDropzone"] button {{
        background: rgba(63,180,137,0.15) !important;
        border: 1px solid rgba(63,180,137,0.4) !important;
        color: var(--green-glow) !important;
        border-radius: 8px !important;
        font-size: 0.82rem !important;
        font-family: 'Sora', sans-serif !important;
        padding: 0.35rem 1rem !important;
        transition: background 0.2s !important;
    }}

    [data-testid="stFileUploaderDropzone"] button:hover {{
        background: rgba(63,180,137,0.28) !important;
    }}

    /* ── FIX: "uploadUpload" duplicate text bug ── */
    [data-testid="stFileUploaderDropzone"] button span {{
        display: none !important;
    }}
    [data-testid="stFileUploaderDropzone"] button::after {{
        content: "Browse Files";
        display: inline !important;
        color: var(--green-glow);
        font-family: 'Sora', sans-serif;
        font-size: 0.82rem;
    }}

    /* ── Primary Identify button ── */
    [data-testid="stButton"] > button {{
        background: linear-gradient(135deg, var(--green-accent) 0%, var(--green-glow) 100%) !important;
        color: var(--green-deep) !important;
        font-family: 'Sora', sans-serif !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important;
        letter-spacing: 0.04em !important;
        padding: 0.6rem 2.2rem !important;
        border: none !important;
        border-radius: 100px !important;
        box-shadow: 0 4px 20px rgba(63,180,137,0.4) !important;
        cursor: pointer !important;
        transition: transform 0.15s, box-shadow 0.15s !important;
        margin-top: 0.5rem !important;
    }}

    [data-testid="stButton"] > button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 28px rgba(63,180,137,0.55) !important;
    }}

    [data-testid="stButton"] > button:active {{
        transform: translateY(0) !important;
    }}

    /* ── Uploaded image display ── */
    [data-testid="stImage"] img {{
        border-radius: 12px !important;
        border: 1px solid var(--card-border) !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3) !important;
    }}

    /* ── Medicine details result card ── */
    [data-testid="stVerticalBlock"] [data-testid="stVerticalBlock"] + [data-testid="stVerticalBlock"] {{
        background: rgba(13, 61, 47, 0.55) !important;
        border: 1px solid rgba(93,212,168,0.2) !important;
    }}

    /* ── Markdown text ── */
    .stMarkdown p, .stMarkdown li {{
        color: var(--text-main) !important;
        text-shadow: none !important;
        line-height: 1.75;
        font-size: 0.93rem !important;
    }}

    .stMarkdown strong {{
        color: var(--green-glow) !important;
        text-shadow: none !important;
    }}

    /* ── Spinner ── */
    [data-testid="stSpinner"] p {{
        color: var(--text-muted) !important;
        text-shadow: none !important;
        font-size: 0.85rem !important;
    }}

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, rgba(8,28,20,0.95) 0%, rgba(13,61,47,0.92) 100%) !important;
        backdrop-filter: blur(12px) !important;
        border-right: 1px solid rgba(255,255,255,0.07) !important;
    }}

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] div,
    [data-testid="stSidebar"] label {{
        color: var(--text-main) !important;
        text-shadow: none !important;
    }}

    [data-testid="stSidebar"] .stMarkdown p {{
        font-size: 0.88rem !important;
        color: var(--text-muted) !important;
    }}

    /* ── Error message ── */
    [data-testid="stAlert"] {{
        border-radius: 10px !important;
        border: 1px solid rgba(255,80,80,0.3) !important;
        background: rgba(255,80,80,0.1) !important;
    }}

    /* ── Divider ── */
    hr {{
        border-color: rgba(255,255,255,0.10) !important;
        margin: 1rem 0 !important;
    }}

    /* ── Fade-in page animation ── */
    @keyframes fadeUp {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to   {{ opacity: 1; transform: translateY(0); }}
    }}

    .block-container > div {{
        animation: fadeUp 0.6s ease-out both;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="hero-wrap">
        <div class="hero-badge">💊 AI Medicine Assistant</div>
        <h1 class="hero-title">Medi<span>Bondhu</span></h1>
        <p class="hero-sub">
            Upload a photo of any medicine and instantly get its name,
            uses, side effects, and precautions.
        </p>
        <div class="hero-divider"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("How to use")
    st.divider()
    st.write("**1.** Click **Browse files** below.")
    st.write("**2.** Select up to **3** medicine images.")
    st.write("**3.** Hit **Identify** and wait for the AI analysis.")
    st.divider()
    st.markdown("_More features coming soon — stay tuned!_")

# ── Upload card ───────────────────────────────────────────────────────────────
with st.container(border=True):
    st.header("Upload Medicine Image")
    st.subheader("Supports JPG, JPEG, PNG · max 3 images")

    img = st.file_uploader(
        "Drop your image here or browse",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        label_visibility="collapsed",
    )
    press = st.button("Identify", type="primary")
    pil_img = [Image.open(x) for x in img]

    if img:
        if len(img) > 3:
            st.error("Please upload a maximum of 3 images at a time.")
        else:
            st.markdown("**Uploaded Images**")
            cols = st.columns(len(img))
            for i, image in enumerate(img):
                with cols[i]:
                    st.image(image, use_container_width=True)

            if press:
                with st.container(border=True):
                    st.header("Medicine Details")
                    with st.spinner("Analysing your medicine…"):
                        notes = generate_response(pil_img)
                    st.markdown(notes)
