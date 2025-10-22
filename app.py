import streamlit as st
from utils.loader import load_files
from utils.vectorstore import create_vectorstore
from utils.llm import ask_deepseek

# 👉 Configuración de la página
st.set_page_config(
    page_title="I am Cesar!",
    page_icon="💬",
    layout="wide"
)

# -------------------------------
# 📌 Sidebar (About & Projects)
# -------------------------------
with st.sidebar:
    st.header("👋 About Cesar-Bot")
    st.write(
        """
        Welcome!  
        This chatbot is powered by **AI + my personal knowledge base**.  
        You can ask me about my background, experience, and projects. 
        """
    )
    st.markdown("[My LinkedIn](https://www.linkedin.com/in/cesar-salgado-274a2329/)")
    st.markdown("---")
    st.header("📂 My latest Projects")

    # Data Analysis Projects
    st.subheader("📊 Data Analysis")
    st.markdown("🍺 [Beer Locator](https://9x38iytgmep6yfz4hwtos3.streamlit.app/)")
    st.markdown("🎧 [Headphones Market Analyzer](https://headphones2-eop9mhkwycmwn9aukshggy.streamlit.app/)")
    st.markdown("🎶 [Music Recommender](https://musicex-cr2fvvcfyxkpz3xs8qbdgb.streamlit.app/)")
    st.markdown("⌨️ [Typy](https://cesartypy.streamlit.app/)")

    # AI Projects
    st.subheader("🤖 AI Projects")
    st.markdown("🈴 [Mandarin Assistant](https://mandarinasistant-iprh8589emshqy6oeoayte.streamlit.app/)")
    st.markdown("💹 [Tradex](https://tradexgit-kmwf9rlefbrvroiq7ukzrn.streamlit.app/)")
    st.markdown("📊 [AI + Spreadsheet analyzer](https://finan-analysis22.streamlit.app/)")
    
    

    # Music
    st.subheader("🎵 Other fun projects!")
    st.markdown("💎 [Emerald Portfolio Designing (Video)](https://vimeo.com/user83238836)")
    st.markdown("🎸 [My Music Channel](https://youtube.com/playlist?list=PLu6Srx39DksgbieLwZfEEdEGH6Od_NnIW&si=tuW7tz66p97z2p6g)")

# -------------------------------
# 📌 Main App (Chatbot)
# -------------------------------
st.title("📄 Cesar-Bot")

# Inicializar
FILE_PATHS = ["data/Profile.pdf", "data/summary.txt"]

if "vectorstore" not in st.session_state:
    st.write("🔄 Thinking...")
    docs = load_files(FILE_PATHS)
    st.session_state.vectorstore = create_vectorstore(docs)

# Entrada usuario
question = st.text_input("❓ Ask me a question")

if question:
    retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": 3})
    related_docs = retriever.invoke(question)

    context = "\n\n".join([d.page_content for d in related_docs])
    answer = ask_deepseek(question, context)

    st.subheader("💡 Answer:")
    st.write(answer)

    #with st.expander("📚 Contexto usado"):
    #   st.write(context)


