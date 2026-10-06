import base64
from html import escape
from pathlib import Path

import streamlit as st

from content import CV_FILES, EMAIL, FUN, GITHUB, LINKEDIN, MUSIC, PROJECTS, T

ROOT = Path(__file__).parent

st.set_page_config(
    page_title="César Salgado | RPA, Data Analytics & AI Architecture",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------------------
# 🌐 Language (EN / ES)
# -------------------------------
if "lang" not in st.session_state:
    requested = st.query_params.get("lang", "en")
    st.session_state.lang = requested if requested in ("en", "es") else "en"


@st.cache_data(show_spinner=False)
def image_uri(name: str) -> str:
    data = (ROOT / "assets" / name).read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(data).decode()


@st.cache_data(show_spinner=False)
def file_bytes(path: str) -> bytes:
    return (ROOT / path).read_bytes()


def html(markup: str) -> None:
    st.markdown(markup, unsafe_allow_html=True)


# -------------------------------
# 🎨 Styles
# -------------------------------
html(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=IBM+Plex+Sans:wght@400;500;600&display=swap');
:root{--ink:#14212E;--muted:#55636F;--line:#E2DED4;--paper:#F7F5F0;--card:#FFFFFF;--accent:#0F7B5F;--accent-dark:#0B5F49;--navy:#0F1E2E;}
html,body,.stApp,[data-testid="stAppViewContainer"]{background:var(--paper);}
.stApp,.stApp p,.stApp li,.stApp label,.stApp input,.stApp button{font-family:'IBM Plex Sans',-apple-system,'Segoe UI',sans-serif;}
.stApp{color:var(--ink);}
[data-testid="stSidebar"],[data-testid="stSidebarCollapsedControl"],[data-testid="collapsedControl"]{display:none;}
[data-testid="stHeader"]{background:transparent;}
.block-container{max-width:1140px;padding:1.4rem 1.5rem 3rem;}
html{scroll-behavior:smooth;}
.cs-anchor{display:block;position:relative;top:-70px;visibility:hidden;}

.cs-brand{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:1.3rem;color:var(--ink);letter-spacing:-.01em;line-height:2.4rem;}
.cs-brand span{color:var(--accent);}
.cs-nav{display:flex;gap:1.6rem;justify-content:flex-end;align-items:center;height:2.4rem;flex-wrap:wrap;}
.cs-nav a{color:var(--ink);text-decoration:none;font-size:.95rem;font-weight:500;}
.cs-nav a:hover{color:var(--accent);}

.cs-hero{padding:3rem 0 1.4rem;display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:3.5rem;align-items:center;}
.cs-photo{position:relative;}
.cs-photo:before{content:"";position:absolute;inset:14px -14px -14px 14px;border:2px solid var(--accent);border-radius:18px;}
.cs-photo img{position:relative;display:block;width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:18px;box-shadow:0 22px 50px rgba(15,30,46,.22);}
.stApp .cs-hero p.cs-tagline{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:clamp(1.3rem,2.3vw,1.75rem);line-height:1.25;letter-spacing:-.01em;color:var(--ink);margin:0 0 1.1rem;max-width:640px;}
.cs-eyebrow{font-size:.8rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin-bottom:1rem;}
.cs-hero h1{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:clamp(2.9rem,7vw,5.2rem);line-height:1;letter-spacing:-.03em;color:var(--ink);margin:0 0 1.1rem;padding:0;}
.cs-lead{font-size:1.08rem;line-height:1.65;color:var(--muted);max-width:640px;margin:0;}

.cs-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin:2.2rem 0 1rem;border-top:1px solid var(--line);border-bottom:1px solid var(--line);}
.cs-stat{padding:1.4rem 1.2rem 1.4rem 0;}
.cs-stat + .cs-stat{padding-left:1.4rem;border-left:1px solid var(--line);}
.cs-stat b{display:block;font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:2.1rem;line-height:1;color:var(--ink);margin-bottom:.5rem;}
.cs-stat span{font-size:.9rem;line-height:1.45;color:var(--muted);display:block;}

.cs-section{padding-top:4rem;}
.cs-kicker{font-size:.8rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin-bottom:.6rem;}
.cs-section h2{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:clamp(1.6rem,3vw,2.2rem);letter-spacing:-.015em;line-height:1.15;color:var(--ink);margin:0 0 .6rem;padding:0;}
.cs-note{color:var(--muted);font-size:.95rem;margin:0 0 1.6rem;}

.cs-services{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem;margin-top:1.6rem;}
.cs-service{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:1.6rem 1.5rem;}
.cs-service .n{font-family:'Fraunces',Georgia,serif;color:var(--accent);font-size:1rem;margin-bottom:.9rem;}
.cs-service h3{font-family:'IBM Plex Sans',sans-serif;font-size:1.15rem;font-weight:600;color:var(--ink);margin:0 0 .5rem;padding:0;}
.cs-service p{color:var(--muted);font-size:.97rem;line-height:1.55;margin:0 0 1rem;}
.cs-service ul{margin:0;padding:1rem 0 0;list-style:none;border-top:1px solid var(--line);}
.cs-service li{font-size:.93rem;line-height:1.45;color:var(--ink);padding:.28rem 0 .28rem 1.2rem;position:relative;margin:0;}
.cs-service li:before{content:"";position:absolute;left:0;top:.82em;width:7px;height:2px;background:var(--accent);}

.cs-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem;}
a.cs-card,div.cs-card{display:flex;flex-direction:column;background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;text-decoration:none !important;color:var(--ink) !important;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease;}
a.cs-card:hover{transform:translateY(-4px);box-shadow:0 18px 40px rgba(15,30,46,.14);border-color:#cfd6d2;}
a.cs-card:focus-visible{outline:3px solid var(--accent);outline-offset:3px;}
.cs-img{position:relative;aspect-ratio:16/10;background:var(--navy);overflow:hidden;}
.cs-img img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .35s ease;}
a.cs-card:hover .cs-img img{transform:scale(1.035);}
.cs-badge{position:absolute;left:.8rem;top:.8rem;background:rgba(15,30,46,.82);color:#fff;font-size:.74rem;font-weight:600;letter-spacing:.04em;padding:.3rem .65rem;border-radius:999px;}
.cs-body{padding:1.25rem 1.3rem 1.3rem;display:flex;flex-direction:column;flex:1;}
.cs-tag{font-size:.74rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);margin-bottom:.45rem;}
.cs-card h3{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:1.28rem;line-height:1.2;color:var(--ink);margin:0 0 .85rem;padding:0;}
.cs-label{font-size:.72rem;font-weight:600;letter-spacing:.09em;text-transform:uppercase;color:#8A8F8B;margin:0 0 .2rem;}
.cs-card p{font-size:.93rem;line-height:1.55;color:var(--muted);margin:0 0 .9rem;}
.cs-cta{margin-top:auto;padding-top:.3rem;font-weight:600;font-size:.95rem;color:var(--accent);}
a.cs-card:hover .cs-cta{color:var(--accent-dark);}
.cs-cta i{font-style:normal;display:inline-block;transition:transform .18s ease;margin-left:.25rem;}
a.cs-card:hover .cs-cta i{transform:translateX(4px);}

a.cs-music{display:flex;flex-direction:column;background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;text-decoration:none !important;color:var(--ink) !important;transition:transform .18s ease,box-shadow .18s ease;}
a.cs-music:hover{transform:translateY(-4px);box-shadow:0 18px 40px rgba(15,30,46,.14);}
a.cs-music:focus-visible{outline:3px solid var(--accent);outline-offset:3px;}
.cs-wave{position:relative;height:150px;display:flex;align-items:center;gap:4px;padding:0 1.4rem;background:var(--navy);}
.cs-wave i{flex:1;border-radius:3px;background:var(--wave);opacity:.9;}
.cs-music-techno .cs-wave{--wave:#5EE6D0;background:radial-gradient(420px 220px at 90% 0%,rgba(110,80,230,.75),transparent 65%),#0D1626;}
.cs-music-moombahton .cs-wave{--wave:#FFC857;background:radial-gradient(420px 220px at 90% 0%,rgba(230,70,110,.75),transparent 65%),#24121C;}
.cs-music-lofi .cs-wave{--wave:#BFD9F2;background:radial-gradient(420px 220px at 90% 0%,rgba(70,130,190,.7),transparent 65%),#14263A;}
.cs-music-lofi .cs-wave i{transform:scaleY(.55);}
.cs-play{z-index:2;position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:54px;height:54px;border-radius:50%;background:#fff;color:var(--navy);display:flex;align-items:center;justify-content:center;font-size:1.1rem;padding-left:4px;box-shadow:0 8px 22px rgba(0,0,0,.35);transition:transform .18s ease;}
a.cs-music:hover .cs-play{transform:translate(-50%,-50%) scale(1.1);}
a.cs-music h3{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:1.28rem;line-height:1.2;color:var(--ink);margin:0 0 .5rem;padding:0;}
a.cs-music p{font-size:.93rem;line-height:1.55;color:var(--muted);margin:0 0 .9rem;}
a.cs-music:hover .cs-cta i{transform:translateX(4px);}
.cs-fun{display:grid;grid-template-columns:1fr;gap:1.2rem;margin-top:1.2rem;}
a.cs-funitem{display:flex;justify-content:space-between;align-items:center;gap:1rem;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:1.1rem 1.3rem;text-decoration:none !important;color:var(--ink) !important;transition:border-color .18s ease,box-shadow .18s ease;}
a.cs-funitem:hover{border-color:var(--accent);box-shadow:0 10px 24px rgba(15,30,46,.08);}
.cs-funitem b{display:block;font-weight:600;font-size:1.02rem;}
.cs-funitem span{font-size:.86rem;color:var(--muted);}
.cs-funitem i{font-style:normal;color:var(--accent);font-size:1.2rem;}

.cs-contact{margin-top:4rem;background:var(--navy);border-radius:18px;padding:2.6rem 2.4rem 1.2rem;}
.cs-contact h2{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:clamp(1.6rem,3vw,2.2rem);color:#fff;margin:0 0 .6rem;padding:0;letter-spacing:-.015em;}
.cs-contact p{color:#B8C4CF;font-size:1.05rem;margin:0 0 1.4rem;max-width:640px;}
.cs-contact a.cs-mail{display:inline-block;color:#fff;font-size:1.25rem;font-weight:500;text-decoration:none;border-bottom:2px solid var(--accent);padding-bottom:.15rem;margin-right:1.6rem;margin-bottom:1.4rem;}
.cs-contact a.cs-mail:hover{border-color:#fff;}
.cs-contact a.cs-ext{color:#B8C4CF;text-decoration:none;font-weight:500;margin-right:1.4rem;}
.cs-contact a.cs-ext:hover{color:#fff;}
.cs-footer{text-align:center;color:#8A8F8B;font-size:.85rem;padding:2rem 0 0;}

/* Streamlit widgets */
.stButton button,.stDownloadButton button,.stLinkButton a{border-radius:10px;font-weight:600;padding:.6rem 1.1rem;border:1px solid #CFCABD;}
.stDownloadButton button,.stLinkButton a[kind="secondary"]{background:#fff;color:var(--ink);}
.stDownloadButton button:hover,.stLinkButton a[kind="secondary"]:hover{border-color:var(--accent);color:var(--accent);}
.stLinkButton a[kind="primary"]{background:var(--accent);border-color:var(--accent);color:#fff;}
.stLinkButton a[kind="primary"]:hover{background:var(--accent-dark);border-color:var(--accent-dark);color:#fff;}
div[role="radiogroup"]{justify-content:flex-end;gap:.9rem;}
.st-key-chatbox [data-baseweb="input"],.st-key-chatbox [data-baseweb="base-input"]{background:var(--paper);}
.st-key-chatbox [data-baseweb="input"]{border:1px solid #CFCABD;border-radius:10px;}
.st-key-chatbox [data-baseweb="input"]:focus-within{border-color:var(--accent);}
.st-key-chatbox h3{font-family:'IBM Plex Sans',sans-serif;font-size:1.05rem;font-weight:600;padding-bottom:.2rem;}
.st-key-chatbox{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:1.5rem 1.5rem 1.2rem;margin-top:1.2rem;}

@media (max-width:900px){
  .cs-hero{grid-template-columns:1fr;gap:2rem;}
  .cs-photo{order:-1;max-width:260px;}
  .cs-services,.cs-grid{grid-template-columns:1fr 1fr;}
  .cs-stats{grid-template-columns:1fr 1fr;}
  .cs-stat:nth-child(3){padding-left:0;border-left:0;}
  .cs-stat:nth-child(n+3){border-top:1px solid var(--line);}
}
@media (max-width:640px){
  .block-container{padding-left:1rem;padding-right:1rem;}
  .cs-services,.cs-grid,.cs-fun{grid-template-columns:1fr;}
  .cs-nav{justify-content:flex-start;gap:1.1rem;}
  .cs-hero{padding-top:1.8rem;}
  .cs-photo{max-width:230px;margin-right:14px;}
  .cs-contact{padding:2rem 1.4rem .8rem;}
}
</style>
"""
)

# -------------------------------
# 📌 Top bar
# -------------------------------
bar_left, bar_mid, bar_right = st.columns([3, 6, 2], vertical_alignment="center")
with bar_right:
    st.radio(
        "Language / Idioma",
        ["en", "es"],
        key="lang",
        format_func=lambda code: {"en": "English", "es": "Español"}[code],
        horizontal=True,
        label_visibility="collapsed",
    )

lang = st.session_state.lang
st.query_params["lang"] = lang
t = T[lang]

with bar_left:
    html('<div class="cs-brand">César Salgado<span>.</span></div>')
with bar_mid:
    html(
        '<nav class="cs-nav">'
        f'<a href="#services" target="_self">{t["nav_services"]}</a>'
        f'<a href="#projects" target="_self">{t["nav_projects"]}</a>'
        f'<a href="#chat" target="_self">{t["nav_chat"]}</a>'
        f'<a href="#contact" target="_self">{t["nav_contact"]}</a>'
        "</nav>"
    )


def cta_row(prefix: str) -> None:
    """Contact buttons and CV downloads."""
    c1, c2, c3, c4, _ = st.columns([1.5, 1, 1.75, 1.75, 0.6])
    with c1:
        st.link_button(t["cta_mail"], f"mailto:{EMAIL}", type="primary", use_container_width=True)
    with c2:
        st.link_button(t["cta_linkedin"], LINKEDIN, use_container_width=True)
    for col, code in ((c3, "en"), (c4, "es")):
        path = CV_FILES[code]
        if (ROOT / path).exists():
            with col:
                st.download_button(
                    t[f"cv_{code}"],
                    data=file_bytes(path),
                    file_name=Path(path).name,
                    mime="application/pdf",
                    key=f"{prefix}_cv_{code}",
                    use_container_width=True,
                )


# -------------------------------
# 📌 Hero
# -------------------------------
photo = (
    f'<div class="cs-photo"><img src="{image_uri("profile.jpg")}" alt="César Salgado"></div>'
    if (ROOT / "assets" / "profile.jpg").exists()
    else ""
)
html(
    '<section class="cs-hero">'
    "<div>"
    f'<div class="cs-eyebrow">{t["eyebrow"]}</div>'
    '<h1>César Salgado</h1>'
    f'<p class="cs-tagline">{t["h1"]}</p>'
    f'<p class="cs-lead">{t["lead"]}</p>'
    "</div>"
    f"{photo}"
    "</section>"
)
cta_row("hero")

html(
    '<div class="cs-stats">'
    + "".join(f'<div class="cs-stat"><b>{n}</b><span>{label}</span></div>' for n, label in t["stats"])
    + "</div>"
)

# -------------------------------
# 📌 Services
# -------------------------------
services = "".join(
    f'<div class="cs-service"><div class="n">0{i}</div><h3>{title}</h3><p>{text}</p>'
    + "<ul>"
    + "".join(f"<li>{item}</li>" for item in items)
    + "</ul></div>"
    for i, (title, text, items) in enumerate(t["services"], start=1)
)
html(
    '<span id="services" class="cs-anchor"></span>'
    '<section class="cs-section">'
    f'<div class="cs-kicker">{t["services_kicker"]}</div>'
    f'<h2>{t["services_title"]}</h2>'
    f'<div class="cs-services">{services}</div>'
    "</section>"
)


# -------------------------------
# 📌 Projects
# -------------------------------
def project_card(project: dict) -> str:
    p = project[lang]
    url = project.get("url")
    is_video = project.get("video", False)
    internal = bool(url) and url.startswith("#")

    if "body" in p:
        text = f'<p>{p["body"]}</p>'
    else:
        text = (
            f'<div class="cs-label">{t["problem"]}</div><p>{p["problem"]}</p>'
            f'<div class="cs-label">{t["solution"]}</div><p>{p["solution"]}</p>'
        )

    if is_video:
        cta = t["watch"]
    elif internal:
        cta = t["open_chat"]
    else:
        cta = t["open"]

    badge = f'<span class="cs-badge">▶ {t["video_badge"]}</span>' if is_video else ""
    inner = (
        f'<div class="cs-img"><img src="{image_uri("projects/" + project["image"])}" alt="{escape(p["title"])}" loading="lazy">{badge}</div>'
        '<div class="cs-body">'
        f'<div class="cs-tag">{p["tag"]}</div><h3>{p["title"]}</h3>{text}'
        + (f'<div class="cs-cta">{cta}<i>{"↓" if internal else "→"}</i></div>' if url else "")
        + "</div>"
    )
    if not url:
        return f'<div class="cs-card">{inner}</div>'
    target = 'target="_self"' if internal else 'target="_blank" rel="noopener"'
    return f'<a class="cs-card" href="{escape(url)}" {target}>{inner}</a>'


html(
    '<span id="projects" class="cs-anchor"></span>'
    '<section class="cs-section">'
    f'<div class="cs-kicker">{t["projects_kicker"]}</div>'
    f'<h2>{t["projects_title"]}</h2>'
    f'<p class="cs-note">{t["projects_note"]}</p>'
    f'<div class="cs-grid">{"".join(project_card(p) for p in PROJECTS)}</div>'
    "</section>"
)

bars = "".join(f'<i style="height:{18 + (i * 37) % 71}%"></i>' for i in range(28))
music_cards = "".join(
    f'<a class="cs-music cs-music-{item["style"]}" href="{escape(item["url"])}" target="_blank" rel="noopener">'
    f'<div class="cs-wave"><span class="cs-play">▶</span>{bars}</div>'
    '<div class="cs-body">'
    f'<div class="cs-tag">{item[lang][2]}</div><h3>{item[lang][0]}</h3><p>{item[lang][1]}</p>'
    f'<div class="cs-cta">{t["listen"]}<i>→</i></div>'
    "</div></a>"
    for item in MUSIC
)
html(
    '<span id="music" class="cs-anchor"></span>'
    '<section class="cs-section">'
    f'<div class="cs-kicker">{t["music_kicker"]}</div>'
    f'<h2>{t["music_title"]}</h2>'
    f'<p class="cs-note">{t["music_lead"]}</p>'
    f'<div class="cs-grid">{music_cards}</div>'
    "</section>"
)

fun_items = "".join(
    f'<a class="cs-funitem" href="{escape(item["url"])}" target="_blank" rel="noopener">'
    f"<div><b>{item[lang][0]}</b><span>{item[lang][1]}</span></div><i>→</i></a>"
    for item in FUN
)
html(
    '<section class="cs-section" style="padding-top:2.2rem">'
    f'<h2 style="font-size:1.4rem">{t["fun_title"]}</h2>'
    f'<div class="cs-fun">{fun_items}</div>'
    "</section>"
)

# -------------------------------
# 📌 Chatbot (Cesar-Bot)
# The page reserves its place here and fills it at the end of the script,
# so the rest of the site is visible while the knowledge base loads.
# -------------------------------
html(
    '<span id="chat" class="cs-anchor"></span>'
    '<section class="cs-section">'
    f'<div class="cs-kicker">{t["chat_kicker"]}</div>'
    f'<h2>{t["chat_title"]}</h2>'
    f'<p class="cs-note" style="margin-bottom:0">{t["chat_lead"]}</p>'
    "</section>"
)
chat_slot = st.container(key="chatbox")

# -------------------------------
# 📌 Contact
# -------------------------------
html(
    '<span id="contact" class="cs-anchor"></span>'
    '<section class="cs-contact">'
    f'<h2>{t["contact_title"]}</h2>'
    f'<p>{t["contact_lead"]}</p>'
    f'<a class="cs-mail" href="mailto:{EMAIL}">{EMAIL.replace("@", "<span>@</span>")}</a>'
    f'<a class="cs-ext" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a>'
    f'<a class="cs-ext" href="{GITHUB}" target="_blank" rel="noopener">GitHub ↗</a>'
    "</section>"
)
html(f'<div class="cs-footer">© César Salgado · {t["footer"]}</div>')

# -------------------------------
# 📌 Chatbot logic (unchanged)
# -------------------------------
with chat_slot:
    from utils.loader import load_files
    from utils.vectorstore import create_vectorstore
    from utils.llm import ask_deepseek

    # Inicializar
    FILE_PATHS = ["data/Profile.pdf", "data/summary.txt", "assets/cv/CV_Cesar_Salgado_EN.pdf"]

    if "vectorstore" not in st.session_state:
        with st.spinner(t["chat_loading"]):
            docs = load_files(FILE_PATHS)
            st.session_state.vectorstore = create_vectorstore(docs)

    # Entrada usuario
    question = st.text_input(t["chat_input"])

    if question:
        retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": 5})
        related_docs = retriever.invoke(question)

        context = "\n\n".join([d.page_content for d in related_docs])
        answer = ask_deepseek(question, context)

        st.subheader(t["chat_answer"])
        st.write(answer)
