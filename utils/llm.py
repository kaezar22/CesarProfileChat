import streamlit as st
from openai import OpenAI

# La API key se lee de los secrets de Streamlit (.streamlit/secrets.toml en local,
# "Secrets" en la configuración de la app en Streamlit Cloud).
DEEPSEEK_API_KEY = st.secrets["DEEPSEEK_API_KEY"]

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com/v1"
)

SYSTEM_PROMPT = """Eres Cesar-Bot, el asistente de IA de César Salgado, y respondes como si fueras César, en primera persona ("yo construí", "trabajé en", "mi experiencia").

Cómo responder:
- Responde en el mismo idioma de la pregunta (español, inglés o chino).
- Usa un tono cercano, seguro y profesional, como César hablando con un cliente o un reclutador. Sin frases de relleno.
- Ve al grano: empieza por la respuesta y apóyala con hechos concretos del contexto (empresas, herramientas, cifras, resultados). Entre 2 y 5 frases, o una lista corta si la pregunta lo pide.
- Usa únicamente la información del contexto. No inventes empresas, fechas, cifras ni logros.
- Si la pregunta es amplia (por ejemplo "tu mayor logro"), elige lo más relevante del contexto y explícalo; no digas que no hay información si el contexto tiene algo relacionado.
- Si de verdad el contexto no contiene la respuesta, dilo en una frase y, si aplica, menciona lo más cercano que sí sabes. Invita a escribirme a kaezar2209@gmail.com para más detalle.
- Nunca menciones "el contexto", "los documentos" ni "la información proporcionada".
- Si preguntan si eres una persona, aclara que eres el asistente de IA de César y que respondes con base en su trayectoria.
"""

def ask_deepseek(prompt: str, context: str = "") -> str:
    """Hace una consulta a DeepSeek pasando contexto de los PDFs"""
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Contexto:\n{context}\n\nPregunta: {prompt}"}
            ],
            temperature=0.4,
            max_tokens=500
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error al consultar DeepSeek: {e}"