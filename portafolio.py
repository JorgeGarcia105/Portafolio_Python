import streamlit as st
from PIL import Image
from datetime import datetime

# Configuración de página
st.set_page_config(
    page_title=f"Jorge García - Ingeniero de Sistemas",
    page_icon="💻",
    layout="wide"
)

# Datos estructurados
DATA = {
    "header": {
        "nombre": "Jorge Iván García Torres",
        "titulo": "Ingeniero de Sistemas y Computación | Desarrollador Backend | Analista de Datos",
        "resumen": "Especialista en soluciones escalables y seguras con enfoque en arquitecturas backend y análisis de datos",
        "foto": "./assets/perfil.jpg"
    },
    "contacto": {
        "email": "garciatorresjorgeivan10@gmail.com",
        "github": "https://github.com/JorgeGarcia105",
        "linkedin": "https://linkedin.com/in/JorgeGarcia105",
        "portafolio": "https://jorgegarcia105.github.io/Portafolio/"
    },
    "habilidades": {
        "Lenguajes": ["Java", "Python", "PL/SQL", "SQL"],
        "Backend": ["Spring Boot", "JPA/Hibernate", "REST APIs", "Microservicios"],
        "Bases de Datos": ["PostgreSQL", "MySQL", "Oracle SQL", "MongoDB"],
        "Análisis": ["Optimización algoritmos", "Evaluación de desempeño", "Pandas/Matplotlib"],
        "DevOps": ["Git/GitHub", "Docker", "CI/CD", "Trello"]
    },
    "formacion": {
        "universidad": {
            "titulo": "Ingeniería de Sistemas y Computación",
            "institucion": "Universidad de Caldas",
            "detalle": "7mo semestre - Cursos destacados: Arquitectura de Software, Bases de Datos Avanzadas"
        },
        "certificaciones": [
            "Oracle Next Education F2 T7 Back-end",
            "Especialización en Spring Boot - Alura",
            "Arquitectura de APIs REST - Alura"
        ]
    },
    "proyectos": [
        {
            "nombre": "Foro Hub - API REST",
            "stack": "Spring Boot | PostgreSQL | JWT",
            "logros": [
                "Implementación completa de operaciones CRUD",
                "Sistema de autenticación JWT",
                "Optimización de consultas SQL en 40%"
            ],
            "url": "https://github.com/tusuario/foro-hub"
        },
        {
            "nombre": "LiterAlura - Catálogo de Libros",
            "stack": "Java | PostgreSQL | API REST",
            "logros": [
                "Consumo de API externa Gutendex",
                "Sistema de persistencia eficiente",
                "Interfaz de línea de comandos"
            ],
            "url": "https://github.com/tusuario/literalura"
        },
        {
            "nombre": "Análisis de Estrategias Algorítmicas",
            "stack": "Python | Pandas | Matplotlib",
            "logros": [
                "Comparativa de tiempos de ejecución",
                "Generación automática de reportes",
                "Optimización de código en 35%"
            ],
            "url": "https://github.com/tusuario/analisis-algoritmos"
        }
    ],
    "objetivo": """Apasionado por resolver problemas complejos mediante arquitecturas software robustas. 
    Busco oportunidades para desarrollar sistemas escalables y participar en proyectos innovadores 
    que combinen backend sólido con análisis de datos estratégicos."""
}

# ===== HEADER =====
col1, col2 = st.columns([1, 3])
with col1:
    st.image(Image.open(DATA["header"]["foto"]), width=220)

with col2:
    st.title(f"**{DATA['header']['nombre']}**")
    st.markdown(f"#### {DATA['header']['titulo']}")
    st.markdown(f"""
    *{DATA['header']['resumen']}*
    
    <div style="margin-top:15px;">
        <a href="{DATA['contacto']['github']}" target="_blank">
            <img src="https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white">
        </a>
        <a href="{DATA['contacto']['linkedin']}" target="_blank">
            <img src="https://img.shields.io/badge/-LinkedIn-0077B5?logo=linkedin&logoColor=white">
        </a>
        <a href="mailto:{DATA['contacto']['email']}">
            <img src="https://img.shields.io/badge/-Email-D14836?logo=gmail&logoColor=white">
        </a>
    </div>
    """, unsafe_allow_html=True)

# ===== HABILIDADES =====
st.header("🛠 Stack Tecnológico", divider="blue")
cols = st.columns(5)

with cols[0]:
    st.subheader("**Lenguajes**")
    for item in DATA["habilidades"]["Lenguajes"]:
        st.markdown(f"- {item}")

with cols[1]:
    st.subheader("**Backend**")
    for item in DATA["habilidades"]["Backend"]:
        st.markdown(f"- {item}")

with cols[2]:
    st.subheader("**Bases de Datos**")
    for item in DATA["habilidades"]["Bases de Datos"]:
        st.markdown(f"- {item}")

with cols[3]:
    st.subheader("**Análisis**")
    for item in DATA["habilidades"]["Análisis"]:
        st.markdown(f"- {item}")

with cols[4]:
    st.subheader("**DevOps**")
    for item in DATA["habilidades"]["DevOps"]:
        st.markdown(f"- {item}")

# ===== FORMACIÓN =====
st.header("📚 Formación Académica", divider="green")
st.markdown(f"""
**🎓 {DATA['formacion']['universidad']['titulo']}**  
*{DATA['formacion']['universidad']['institucion']}*  
{DATA['formacion']['universidad']['detalle']}

**🏅 Certificaciones:**  
{"  \n".join(["• " + cert for cert in DATA['formacion']['certificaciones']])}
""")

# ===== PROYECTOS =====
st.header("🚀 Proyectos Destacados", divider="orange")

for proyecto in DATA["proyectos"]:
    with st.expander(f"**{proyecto['nombre']}** | {proyecto['stack']}", expanded=True):
        st.markdown("**Principales logros:**")
        for logro in proyecto["logros"]:
            st.markdown(f"- {logro}")
        st.markdown(f"[🔗 Repositorio del proyecto]({proyecto['url']})")

# ===== OBJETIVO =====
st.header("🎯 Objetivo Profesional", divider="violet")
st.markdown(f"""
*{DATA['objetivo']}*
""")

# ===== CONTACTO =====
st.header("📬 Contacto", divider="gray")
col1, col2 = st.columns(2)

with col1:
    st.subheader("**Información de Contacto**")
    st.markdown(f"""
    📧 {DATA['contacto']['email']}  
    🔗 [Portafolio Web]({DATA['contacto']['portafolio']})  
    🌐 [LinkedIn]({DATA['contacto']['linkedin']})  
    ⚙️ [GitHub]({DATA['contacto']['github']})
    """)

with col2:
    st.subheader("**Descargas**")
    st.download_button(
        label="📄 Descargar CV Completo",
        data=open("tu_cv.pdf", "rb").read(),
        file_name="tu_cv.pdf",
        mime="application/pdf"
    )

# Estilos CSS
st.markdown("""
<style>
    [data-testid="stExpander"] .streamlit-expanderHeader {
        background-color: #1a2639;
        color: white;
        border-radius: 8px;
        margin: 5px 0;
    }
    .stDownloadButton > button {
        width: 100%;
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        border: none;
        transition: transform 0.3s;
    }
    .stDownloadButton > button:hover {
        transform: scale(1.05);
    }
    .stMarkdown h3 {
        color: #2b5876;
    }
</style>
""", unsafe_allow_html=True)
