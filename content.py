"""Texts and project data for the site, in English and Spanish.

To change wording, edit the strings here. To add a project, add an entry to
PROJECTS and drop its picture (16:10, e.g. 1200x750) in assets/projects/.
"""

EMAIL = "kaezar2209@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/cesar-salgado-274a2329/"
GITHUB = "https://github.com/kaezar22"

CV_FILES = {
    "en": "assets/cv/CV_Cesar_Salgado_EN.pdf",
    "es": "assets/cv/CV_Cesar_Salgado_ES.pdf",
}

T = {
    "en": {
        "nav_services": "Services",
        "nav_projects": "Projects",
        "nav_chat": "Ask my AI",
        "nav_contact": "Contact",
        "eyebrow": "RPA · Data Analytics · AI Architecture",
        "h1": "I turn manual processes into automated ones, and data into decisions.",
        "lead": (
            "I'm César Salgado, an industrial engineer and consultant with more than seven years "
            "in finance, the public sector, e-commerce and international trade. "
            "I design and build automation, analytics and AI systems, and I work in "
            "Spanish, English and Mandarin."
        ),
        "cta_mail": "Start a conversation",
        "cta_linkedin": "LinkedIn",
        "cv_en": "Download CV (English)",
        "cv_es": "Download CV (Spanish)",
        "stats": [
            ("7+", "years in data, automation and AI"),
            ("53,000", "corporate clients profiled by an LLM engine I built at StoneX"),
            ("4 days", "for a process that took a five-person team weeks to months"),
            ("3", "working languages: Spanish, English and Mandarin"),
        ],
        "services_kicker": "Consulting",
        "services_title": "What I can do for your company",
        "services": [
            (
                "RPA & process automation",
                "Repetitive work in spreadsheets, reports and web portals, handed over to software.",
                [
                    "Automation of manual processes with Python",
                    "Scheduled workflows and alerts",
                    "API integrations and web scraping",
                    "Automated reporting",
                ],
            ),
            (
                "Data analytics",
                "One reliable view of the business, built from data that is scattered today.",
                [
                    "SQL models and data pipelines",
                    "Power BI and Streamlit dashboards",
                    "Data quality and migration checks",
                    "Forecasting and machine learning",
                ],
            ),
            (
                "AI architecture",
                "Language models applied where they pay for themselves, from pilot to daily use.",
                [
                    "LLM data enrichment at scale",
                    "Chatbots that answer from your own documents (RAG)",
                    "Model, cost and architecture decisions",
                    "Sentiment and text analysis",
                ],
            ),
        ],
        "projects_kicker": "Selected work",
        "projects_title": "Projects you can open and try",
        "projects_note": "The live demos are hosted on a free tier, so a demo may take up to a minute to wake up.",
        "problem": "The problem",
        "solution": "What it does",
        "open": "Open project",
        "open_chat": "Try it below",
        "watch": "Watch the video",
        "video_badge": "Video showcase",
        "fun_title": "Other fun projects",
        "chat_kicker": "Cesar-Bot",
        "chat_title": "Ask my AI about my background",
        "chat_lead": "A chatbot that answers from my CV and profile. Ask about my experience, skills or projects.",
        "chat_loading": "Loading the knowledge base…",
        "chat_input": "❓ Ask me a question",
        "chat_answer": "💡 Answer:",
        "contact_title": "Have a process that should run by itself?",
        "contact_lead": "Tell me what your team does by hand today. I'll reply with how I would approach it.",
        "footer": "Bogotá, Colombia · Available for remote projects",
    },
    "es": {
        "nav_services": "Servicios",
        "nav_projects": "Proyectos",
        "nav_chat": "Pregúntale a mi IA",
        "nav_contact": "Contacto",
        "eyebrow": "RPA · Analítica de datos · Arquitectura de IA",
        "h1": "Convierto procesos manuales en procesos automatizados, y datos en decisiones.",
        "lead": (
            "Soy César Salgado, ingeniero industrial y consultor con más de siete años "
            "en finanzas, sector público, comercio electrónico y comercio internacional. "
            "Diseño y construyo sistemas de automatización, analítica e IA, y trabajo en "
            "español, inglés y mandarín."
        ),
        "cta_mail": "Conversemos",
        "cta_linkedin": "LinkedIn",
        "cv_en": "Descargar CV (inglés)",
        "cv_es": "Descargar CV (español)",
        "stats": [
            ("7+", "años en datos, automatización e IA"),
            ("53.000", "clientes corporativos perfilados por un motor LLM que construí en StoneX"),
            ("4 días", "para un proceso que a un equipo de cinco personas le tomaba de semanas a meses"),
            ("3", "idiomas de trabajo: español, inglés y mandarín"),
        ],
        "services_kicker": "Consultoría",
        "services_title": "Lo que puedo hacer por su empresa",
        "services": [
            (
                "RPA y automatización de procesos",
                "El trabajo repetitivo en hojas de cálculo, reportes y portales web, en manos del software.",
                [
                    "Automatización de procesos manuales con Python",
                    "Flujos programados y alertas",
                    "Integraciones por API y web scraping",
                    "Reportes automatizados",
                ],
            ),
            (
                "Analítica de datos",
                "Una vista confiable del negocio, construida con datos que hoy están dispersos.",
                [
                    "Modelos SQL y pipelines de datos",
                    "Tableros en Power BI y Streamlit",
                    "Calidad de datos y control de migraciones",
                    "Pronósticos y machine learning",
                ],
            ),
            (
                "Arquitectura de IA",
                "Modelos de lenguaje aplicados donde se pagan solos, del piloto al uso diario.",
                [
                    "Enriquecimiento de datos con LLM a gran escala",
                    "Chatbots que responden con sus propios documentos (RAG)",
                    "Decisiones de modelo, costo y arquitectura",
                    "Análisis de sentimiento y de texto",
                ],
            ),
        ],
        "projects_kicker": "Trabajo seleccionado",
        "projects_title": "Proyectos que puede abrir y probar",
        "projects_note": "Las demos están en un plan gratuito, así que una demo puede tardar hasta un minuto en despertar.",
        "problem": "El problema",
        "solution": "Qué hace",
        "open": "Abrir proyecto",
        "open_chat": "Pruébelo abajo",
        "watch": "Ver el video",
        "video_badge": "Demostración en video",
        "fun_title": "Otros proyectos por gusto",
        "chat_kicker": "Cesar-Bot",
        "chat_title": "Pregúntale a mi IA sobre mi trayectoria",
        "chat_lead": "Un chatbot que responde con base en mi CV y mi perfil. Pregunte por mi experiencia, habilidades o proyectos.",
        "chat_loading": "Cargando la base de conocimiento…",
        "chat_input": "❓ Hazme una pregunta",
        "chat_answer": "💡 Respuesta:",
        "contact_title": "¿Tiene un proceso que debería funcionar solo?",
        "contact_lead": "Cuénteme qué hace hoy su equipo a mano. Le respondo con la forma en que lo abordaría.",
        "footer": "Bogotá, Colombia · Disponible para proyectos remotos",
    },
}

# Each project: image file in assets/projects/, link (None = no link), and texts per language.
PROJECTS = [
    {
        "image": "nutrienti.jpg",
        "url": "https://prediccion-hort.streamlit.app/",
        "en": {
            "tag": "Predictive analytics",
            "title": "Nutrienti: vegetable price forecast",
            "problem": "Wholesale vegetable prices swing sharply from one month to the next, so buyers plan purchases and promotions without knowing where prices are heading.",
            "solution": "Forecasts next month's price per kilo at Corabastos from official SIPSA-DANE data, with a likely range and a plain signal for each product: likely drop, likely rise or no clear signal.",
        },
        "es": {
            "tag": "Analítica predictiva",
            "title": "Nutrienti: predicción de precios de hortalizas",
            "problem": "Los precios mayoristas de las hortalizas cambian con fuerza de un mes a otro, y los compradores planean compras y ofertas sin saber hacia dónde van.",
            "solution": "Pronostica el precio por kilo del próximo mes en Corabastos con datos oficiales de SIPSA-DANE, con un rango probable y una señal clara por producto: baja probable, alza probable o sin señal clara.",
        },
    },
    {
        "image": "tradex.jpg",
        "url": "https://tradexgit-kmwf9rlefbrvroiq7ukzrn.streamlit.app/",
        "en": {
            "tag": "Finance · AI",
            "title": "Tradex: market analyzer",
            "problem": "Reviewing dozens of instruments by hand, across charts, indicators and news, takes hours before any decision is made.",
            "solution": "Screens up to 30 Yahoo Finance tickers, charts technical indicators, forecasts prices with ARIMA and scores news sentiment with a language model.",
        },
        "es": {
            "tag": "Finanzas · IA",
            "title": "Tradex: analizador de mercados",
            "problem": "Revisar a mano decenas de instrumentos, entre gráficos, indicadores y noticias, toma horas antes de decidir cualquier cosa.",
            "solution": "Evalúa hasta 30 tickers de Yahoo Finance, grafica indicadores técnicos, pronostica precios con ARIMA y califica el sentimiento de las noticias con un modelo de lenguaje.",
        },
    },
    {
        "image": "analyzer.jpg",
        "url": "https://finan-analysis22.streamlit.app/",
        "en": {
            "tag": "AI · Business intelligence",
            "title": "AI financial analyzer",
            "problem": "Income and expenses end up in a spreadsheet that nobody analyzes, and every answer means building formulas or asking an analyst.",
            "solution": "Record each movement in a form, follow income and spending in a dashboard, and ask questions in a chat that answers with a chart. The data lives in Google Sheets. The demo runs on fictional numbers.",
        },
        "es": {
            "tag": "IA · Inteligencia de negocios",
            "title": "Analizador financiero con IA",
            "problem": "Los ingresos y gastos terminan en una hoja de cálculo que nadie analiza, y cada respuesta exige armar fórmulas o pedírsela a un analista.",
            "solution": "Registre cada movimiento en un formulario, siga ingresos y gastos en un tablero y haga preguntas en un chat que responde con un gráfico. Los datos viven en Google Sheets. La demo usa cifras ficticias.",
        },
    },
    {
        "image": "mandarin.jpg",
        "url": "https://mandarinasistant-iprh8589emshqy6oeoayte.streamlit.app/",
        "en": {
            "tag": "AI · Education",
            "title": "Mandarin Assistant",
            "problem": "Generic translators answer with words a beginner has not studied yet, which confuses students more than it helps them.",
            "solution": "Translates phrases and answers grammar questions using only the vocabulary of the Chinese course, so every answer is something the student can already read.",
        },
        "es": {
            "tag": "IA · Educación",
            "title": "Asistente de Mandarín",
            "problem": "Los traductores genéricos responden con palabras que un principiante todavía no ha estudiado, y eso confunde más de lo que ayuda.",
            "solution": "Traduce frases y resuelve dudas de gramática usando solo el vocabulario del curso de chino, de modo que el estudiante puede leer cada respuesta.",
        },
    },
    {
        "image": "music.jpg",
        "url": "https://www.youtube.com/watch?v=5pa0DTHWSxY",
        "video": True,  # showcase only: the card opens the video, not the app
        "en": {
            "tag": "Machine learning · Music",
            "title": "Music automation",
            "body": "An app that automates music creation with machine learning. The training set is made only of my own compositions. The video shows how it works; the app itself is not open to the public because the music is my own work.",
        },
        "es": {
            "tag": "Machine learning · Música",
            "title": "Automatización musical",
            "body": "Una aplicación que automatiza la creación de música con machine learning. El conjunto de entrenamiento está formado únicamente por mis propias composiciones. El video muestra cómo funciona; la aplicación no está abierta al público porque la música es obra mía.",
        },
    },
    {
        "image": "cesarbot.jpg",
        "url": "#chat",
        "en": {
            "tag": "RAG chatbot",
            "title": "Cesar-Bot",
            "problem": "A CV cannot answer follow-up questions, and recruiters and clients always have them.",
            "solution": "A retrieval-augmented chatbot that answers questions about my background from my own documents. It runs on this page.",
        },
        "es": {
            "tag": "Chatbot RAG",
            "title": "Cesar-Bot",
            "problem": "Un CV no puede responder preguntas de seguimiento, y los reclutadores y clientes siempre las tienen.",
            "solution": "Un chatbot con recuperación de documentos que responde preguntas sobre mi trayectoria a partir de mis propios documentos. Funciona en esta página.",
        },
    },
]

FUN = [
    {
        "url": "https://vimeo.com/user83238836",
        "en": ("Emerald Portfolio Designing", "Video · Vimeo"),
        "es": ("Diseño de portafolio de esmeraldas", "Video · Vimeo"),
    },
    {
        "url": "https://youtube.com/playlist?list=PLu6Srx39DksgbieLwZfEEdEGH6Od_NnIW&si=tuW7tz66p97z2p6g",
        "en": ("My Music Channel", "Playlist · YouTube"),
        "es": ("Mi canal de música", "Lista de reproducción · YouTube"),
    },
]
