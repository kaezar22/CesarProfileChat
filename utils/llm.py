import streamlit as st
from openai import OpenAI

# La API key se lee de los secrets de Streamlit (.streamlit/secrets.toml en local,
# "Secrets" en la configuración de la app en Streamlit Cloud).
DEEPSEEK_API_KEY = st.secrets["DEEPSEEK_API_KEY"]

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com/v1"
)

def ask_deepseek(prompt: str, context: str = "") -> str:
    """Hace una consulta a DeepSeek pasando contexto de los PDFs"""
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "Eres un asistente que responde únicamente usando la información de los documentos proporcionados."},
                {"role": "user", "content": f"Contexto:\n{context}\n\nPregunta: {prompt}"}
            ],
            temperature=0.4,
            max_tokens=500
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error al consultar DeepSeek: {e}"