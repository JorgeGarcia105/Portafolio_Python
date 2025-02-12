import streamlit as st
from PIL import Image
from datetime import datetime

# Configuración de página
st.set_page_config(
    page_title=f"Portafolio {datetime.now().year} - Jorge García",
    page_icon="💻",
    layout="wide"
)

# Datos actualizados
DATA = {
    "nombre": "Jorge Iván García Torres",
    "universidad": "Universidad de Caldas (7mo semestre)",
    "alura": "Alura Latam - Backend (Abril-2024  21)",
    "contacto": {
        "email": "garciatorresjorgeivan10@gmail.com",
        "github": "https://github.com/JorgeGarcia105",
        "linkedin": "https://linkedin.com/in/JorgeGarcia105",
        "portafolio": "https://jorgegarcia105.github.io/Portafolio/"
    },
    "experiencia": [
        {
            "rol": "Desarrollador Backend - Digital Funeraria",
            "periodo": "Ene 2024 - Jun 2024",
            "logros": [
                "Implementación de seguridad con LoopBack 4 y MongoDB/Oracle",
                "Autenticación 2FA y sistema de notificaciones",
                "Optimización de consultas (+15% eficiencia)"
            ]
        },
        {
            "rol": "Desarrollador Full Stack - Gestión de Archivos",
            "periodo": "Ago 2023 - Dic 2023",
            "logros": [
                "Sistema de gestión con Python/Tkinter",
                "Integración de bibliotecas locales",
                "Mejoras UX/UI"
            ]
        }
    ],
    "proyectos": [
        {
            "nombre": "Conversor de Moneda",
            "tech": "Java, API ExchangeRate",
            "desc": "Conversor con tasas en tiempo real e histórico",
            "url": "https://github.com/JorgeGarcia105/ConversorMoneda"
        },
        {
            "nombre": "Solucionador de Laberintos",
            "tech": "Python, Pygame",
            "desc": "Visualización de algoritmos A* y BFS",
            "url": "https://github.com/JorgeGarcia105/SolucionadorLaberintos"
        }
    ],
    "certificaciones": [
        "Oracle Next Education (ONE) - 21 Enero 2025"
    ]
}

# ===== HEADER =====
col1, col2 = st.columns([1, 3])
with col1:
    st.image(Image.open("perfil.jpg"), width=200)

with col2:
    st.title(f"**{DATA['nombre']}**")
    st.markdown(f"""
    🎓 **{DATA['universidad']}** | 🏅 **{DATA['alura']}**
    
    🔧 Especializado en:
    - Arquitecturas Backend Seguras
    - Optimización de Sistemas
    - Soluciones Full Stack
    """)
    
    st.markdown(f"""
    <div style="margin-top:20px;">
        <a href="{DATA['contacto']['github']}" target="_blank"><img src="https://img.shields.io/badge/GitHub-Repos-black?logo=github" style="margin-right:10px;"></a>
        <a href="{DATA['contacto']['linkedin']}" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin"></a>
    </div>
    """, unsafe_allow_html=True)

# ===== HABILIDADES =====
st.header("🛠 Stack Tecnológico", divider="blue")
skills_cols = st.columns(3)

with skills_cols[0]:
    st.subheader("💻 Backend")
    st.markdown("""
    - Java • Spring Boot
    - Python • LoopBack
    - APIs REST/GraphQL
    - Oracle • MongoDB
    """)

with skills_cols[1]:
    st.subheader("🛠 DevOps")
    st.markdown("""
    - Docker • Kubernetes
    - Jenkins • Git
    - TDD • Scrum
    """)

with skills_cols[2]:
    st.subheader("📈 Data Science")
    st.markdown("""
    - Pandas • Matplotlib
    - Análisis de Rendimiento
    - Optimización Algorítmica
    """)

# ===== EXPERIENCIA =====
st.header("💼 Experiencia Relevante", divider="green")

for exp in DATA['experiencia']:
    with st.expander(f"**{exp['rol']}** | {exp['periodo']}", expanded=True):
        st.markdown("**Logros clave:**")
        for logro in exp['logros']:
            st.markdown(f"- {logro}")

# ===== PROYECTOS =====
st.header("🚀 Proyectos Destacados", divider="orange")

for proyecto in DATA['proyectos']:
    with st.expander(f"**{proyecto['nombre']}** | {proyecto['tech']}"):
        st.markdown(f"""
        {proyecto['desc']}
        [🔗 Repositorio]({proyecto['url']})
        """)

# ===== FORMACIÓN =====
st.header("📚 Educación y Certificaciones", divider="violet")

st.markdown(f"""
**🎓 {DATA['universidad']}**  
Cursos destacados: Arquitectura de Software, Bases de Datos Avanzadas

**🏅 {DATA['alura']}**  
Especialización en Desarrollo Backend con Java

**📜 Certificaciones:**  
- {DATA['certificaciones'][0]}
""")

# ===== CONTACTO =====
st.header("📬 Contacto Directo", divider="gray")

contact_cols = st.columns(2)
with contact_cols[0]:
    st.subheader("Formulario")
    st.markdown(f"""
    <form action="https://formsubmit.co/{DATA['contacto']['email']}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Nombre" required style="margin:5px; width:90%;">
        <input type="email" name="email" placeholder="Email" required style="margin:5px; width:90%;">
        <textarea name="message" placeholder="Mensaje" style="margin:5px; width:90%; height:100px;"></textarea>
        <button type="submit" style="margin:5px; background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px;">Enviar</button>
    </form>
    """, unsafe_allow_html=True)

with contact_cols[1]:
    st.subheader("Redes")
    st.markdown(f"""
    📧 **Email:**  
    {DATA['contacto']['email']}
    
    🔗 **Portafolio:**  
    [{DATA['contacto']['portafolio']}]({DATA['contacto']['portafolio']})
    
    ⚡ **Descarga mi CV:**  
    """)
    st.download_button(
        label="📄 Descargar CV Completo",
        data=open("CV_JorgeGarcia.pdf", "rb").read(),
        file_name="CV_JorgeGarcia.pdf",
        mime="application/pdf"
    )

# Estilos personalizados
st.markdown("""
<style>
    [data-testid="stExpander"] .streamlit-expanderHeader {
        background-color: #1a2639;
        padding: 15px;
        border-radius: 10px;
    }
    .stDownloadButton > button {
        width: 100%;
        transition: all 0.3s ease;
    }
    .stDownloadButton > button:hover {
        transform: scale(1.05);
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)