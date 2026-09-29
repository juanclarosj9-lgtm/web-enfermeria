import streamlit as st
from PIL import Image
import io

# 1. Configuración de la página
# 1. Configuración de la página
st.set_page_config(
    page_title="Cuidados Integrales de Salud",
    page_icon="🩺",
    layout="wide",
)

# 2. Estilos (Colores Verde Menta y Naranja)
st.markdown("""
<style>
    :root {
        --verde: #2E7D32;
        --verde-oscuro: #1B5E20;
        --naranja: #F7941D;
        --naranja-claro: #FFA940;
        --fondo: #F4FAF5;
    }

    /* Fondo general */
    .stApp {
        background-color: var(--fondo);
    }

    /* Título principal en degradado verde-naranja */
    h1 {
        color: var(--verde);
        font-weight: 800;
    }
    h2, h3 {
        color: var(--verde-oscuro);
    }

    /* Botones naranjas */
    .stButton > button {
        background: linear-gradient(90deg, var(--naranja), var(--naranja-claro));
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0 4px 12px rgba(247, 148, 29, 0.4);
        color: white;
    }

    /* Menú lateral verde */
    [data-testid="stSidebar"] {
        background-color: var(--verde);
    }
    [data-testid="stSidebar"] .stSidebarHeader,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: white !important;
    }

    /* Cajas de éxito/info coordinadas */
    .stSuccess {
        background-color: #E8F5E9;
        border-left: 5px solid var(--verde);
        color: var(--verde-oscuro);
    }
    .stInfo {
        background-color: #FFF3E0;
        border-left: 5px solid var(--naranja);
        color: #E65100;
    }

    /* Expanders (catálogo de servicios) */
    .streamlit-expanderHeader {
        background-color: #E8F5E9;
        color: var(--verde-oscuro) !important;
        font-weight: bold;
        border-radius: 8px;
    }
        /* Lista de servicios en negro */
    .streamlit-expanderContent p,
    .streamlit-expanderContent li,
    .streamlit-expanderContent ul,
    [data-testid="stExpander"] details p,
    [data-testid="stExpander"] details li {
        color: #000000 !important;
    }

    /* Asegurar texto negro en todo el contenido principal */
    .stApp [data-testid="stMarkdownContainer"] p {
        color: #1a1a1a;
    }
     .stApp [data-testid="stMarkdownContainer"] *,
    .stApp p,
    .stApp div {
        color: #1a1a1a !important;
    }

    /* Asegurar que los marcadores (bullets) también sean negros */
    .stApp ul li,
    .stApp ol li {
        color: #1a1a1a !important;
    }
</style>
""", unsafe_allow_html=True)

# TÍTULO ÚNICO


# Aplicar tema verde menta y naranja
st.markdown("""
<style>
    :root {
        --primary-color: #20c997;
        --secondary-color: #FF9F1C;
    }
    .stButton>button {
        background-color: var(--secondary-color);
        color: white;
        font-weight: bold;
    }
    .stSuccess {
        background-color: #d4edda;
        color: #155724;
    }
</style>
""", unsafe_allow_html=True)

# Estilos personalizados para botones y secciones
st.markdown("""
<style>
    .stButton>button {
        background-color: #FF9F1C;
        color: white;
        font-weight: bold;
    }
    .stSuccess {
        background-color: #d4edda;
        color: #155724;
    }
</style>
""", unsafe_allow_html=True)

# 2. Encabezado e Imagen Principal
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    st.image("logo.jpg", use_container_width=True, width=120)
with col_titulo:
    st.title("Cuidados Integrales de Salud")
    st.markdown("<h3 style='color:#F7941D;'>Servicios de Enfermería en General</h3>", unsafe_allow_html=True)

# Imagen del grupo (Usamos una de placeholder, cámbiala por tu foto real: "grupo_enfermeros.jpg")
# 2. Imagen Principal desde internet
imagen_url = "https://images.unsplash.com/photo-1551076805-e1869033e561?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80"
# 2. Imagen Principal desde tu PC
st.image("IMG_1234.JPG.jpg", use_container_width=True)
st.markdown("""
**Atención profesional, cálida y especializada.**
Tu salud en las mejores manos.

- 🩺 Solicitá una valoración de Enfermería.
- 💬 Contanos qué necesitás y te orientamos.
""")

# 3. Menú Lateral

# =========================================================
# NAVEGACIÓN INTEGRADA EN LA PÁGINA PRINCIPAL
# C.I.S. - Cuidados Integrales de Salud
# =========================================================

st.divider()

st.header("¿Cómo podemos ayudarte?")
st.write(
    "Conocé nuestros servicios de Enfermería, "
    "las modalidades de atención y las opciones de contacto."
)

# =========================================================
# 1. SERVICIOS DE ENFERMERÍA
# =========================================================

with st.expander("🩺 SERVICIOS DE ENFERMERÍA", expanded=False):

    st.write(
        "Prestaciones de Enfermería orientadas al cuidado, "
        "la prevención y el acompañamiento de la salud."
    )

    servicios = {
        "Control de signos vitales": [
            "Control de presión arterial.",
            "Control de frecuencia cardíaca y pulso.",
            "Control de frecuencia respiratoria.",
            "Control de temperatura corporal.",
            "Control de saturación de oxígeno.",
            "Control de glucemia capilar, según indicación y contexto.",
            "Registro de los parámetros y comunicación de valores relevantes."
        ],

        "Curaciones y cuidado de heridas": [
            "Curaciones simples.",
            "Curaciones de heridas quirúrgicas.",
            "Curaciones de heridas traumáticas.",
            "Cuidado de lesiones por presión.",
            "Cuidado de heridas crónicas, según valoración.",
            "Cambio de apósitos y vendajes.",
            "Observación y registro de la evolución de la herida.",
            "Educación sobre el cuidado de la piel."
        ],

        "Administración de medicación indicada": [
            "Administración de medicación por vía oral.",
            "Administración de medicación por vía subcutánea.",
            "Administración de medicación por vía intramuscular.",
            "Administración de tratamientos prescritos, según competencia.",
            "Administración de insulina indicada.",
            "Control de horarios y registro de la medicación administrada.",
            "Observación de posibles reacciones y comunicación al equipo tratante."
        ],

        "Higiene y confort": [
            "Baño en cama.",
            "Higiene corporal parcial o completa.",
            "Higiene bucal y perineal.",
            "Cambio de pañales.",
            "Cambio de ropa y ropa de cama.",
            "Cuidado de la piel.",
            "Cambios posturales.",
            "Acomodación y posicionamiento en cama.",
            "Asistencia para vestirse y desvestirse."
        ],

        "Cuidados de adultos mayores": [
            "Asistencia en actividades básicas de la vida diaria.",
            "Ayuda para movilizarse y realizar transferencias.",
            "Prevención de caídas.",
            "Acompañamiento durante rutinas cotidianas.",
            "Observación de cambios en el estado general.",
            "Educación a familiares sobre cuidados seguros.",
            "Apoyo al mantenimiento de la autonomía."
        ],

        "Cuidados posoperatorios": [
            "Control de signos vitales durante la recuperación.",
            "Curaciones de heridas quirúrgicas.",
            "Administración de medicación prescrita.",
            "Observación de signos de alarma.",
            "Asistencia en higiene y confort.",
            "Ayuda para movilizarse de manera segura.",
            "Educación sobre cuidados posteriores al alta."
        ],

        "Cuidados de pacientes con enfermedades crónicas": [
            "Seguimiento de personas con hipertensión arterial.",
            "Control de glucemia en personas con diabetes.",
            "Cuidados de personas con movilidad reducida.",
            "Seguimiento de personas con enfermedades respiratorias.",
            "Observación de cambios en el estado general.",
            "Educación sobre autocuidado y adherencia al tratamiento indicado."
        ]
    }

    for categoria, prestaciones in servicios.items():
        with st.expander(categoria, expanded=False):
            for prestacion in prestaciones:
                st.markdown(f"- {prestacion}")


# =========================================================
# 2. MODALIDADES DE ATENCIÓN
# =========================================================

with st.expander("🏠 MODALIDADES DE ATENCIÓN", expanded=False):

    st.subheader("Visitas de Enfermería")
    st.write(
        "Atención programada en el domicilio para realizar "
        "controles, curaciones y otras prestaciones indicadas."
    )

    st.divider()

    st.subheader("Planes de cuidados domiciliarios")
    st.write(
        "Organización de prestaciones de acuerdo con las "
        "necesidades de la persona y la valoración de Enfermería."
    )

    st.divider()

    st.subheader("Guardias de Enfermería")
    st.write(
        "Atención por turnos, sujeta a evaluación de las "
        "necesidades del paciente y disponibilidad del equipo."
    )

    st.divider()

    st.subheader("Acompañamiento domiciliario")
    st.write(
        "Compañía y asistencia en actividades cotidianas, "
        "diferenciadas de los procedimientos profesionales de Enfermería."
    )


# =========================================================
# 3. SOLICITAR ATENCIÓN
# =========================================================

with st.expander("📋 SOLICITAR ATENCIÓN", expanded=False):

    st.write(
        "Completá los siguientes datos para consultar por "
        "un servicio de C.I.S."
    )

    nombre = st.text_input("Nombre y apellido", key="sol_nombre")
    telefono = st.text_input("Teléfono de contacto", key="sol_telefono")

    localidad = st.selectbox(
        "Localidad",
        [
            "Seleccionar localidad",
            "Capital",
            "Angaco",
            "San Martín",
            "Rivadavia",
            "Otra localidad"
        ],
        key="sol_localidad"
    )

    servicio_solicitado = st.selectbox(
        "Servicio de interés",
        [
            "Control de signos vitales",
            "Curaciones",
            "Administración de medicación indicada",
            "Higiene y confort",
            "Cuidados de adultos mayores",
            "Cuidados posoperatorios",
            "Cuidados de enfermedades crónicas",
            "Visita de Enfermería",
            "Plan de cuidados domiciliarios",
            "Guardia de Enfermería",
            "Acompañamiento domiciliario",
            "Otro servicio"
        ],
        key="sol_servicio"
    )

    detalle = st.text_area(
        "Contanos brevemente qué servicio necesitás (opcional)",
        key="sol_detalle"
    )

    if st.button("Consultar por WhatsApp", key="btn_consulta"):

        if nombre.strip() and telefono.strip():

            import urllib.parse

            mensaje = (
                f"Hola, soy {nombre}. "
                f"Teléfono: {telefono}. "
                f"Localidad: {localidad}. "
                f"Servicio: {servicio_solicitado}. "
                f"Consulta: {detalle}"
            )

            mensaje_url = urllib.parse.quote(mensaje)

            enlace = (
                "https://wa.me/5492645115399?text="
                + mensaje_url
            )

            st.success(
                "Ya podés enviar tu consulta al equipo de C.I.S."
            )

            st.link_button(
                "Abrir WhatsApp",
                enlace
            )

        else:
            st.warning(
                "Completá tu nombre y teléfono para continuar."
            )


# =========================================================
# 4. NUESTRO EQUIPO
# =========================================================

with st.expander("👩‍⚕️ NUESTRO EQUIPO", expanded=False):

    st.write(
        "En C.I.S. trabajamos para brindar una atención "
        "profesional, cercana y personalizada."
    )

    st.info(
        "En este apartado incorporaremos la presentación "
        "del equipo, sus títulos y matrículas profesionales."
    )


# =========================================================
# 5. EDUCACIÓN PARA LA SALUD
# =========================================================

with st.expander("💚 EDUCACIÓN PARA LA SALUD", expanded=False):

    st.write(
        "Un espacio de información y prevención para "
        "promover hábitos saludables y el autocuidado."
    )

    st.markdown(
        "- Consejos de prevención y promoción de la salud."
    )
    st.markdown(
        "- Información sobre enfermedades frecuentes."
    )
    st.markdown(
        "- Recomendaciones para el cuidado en el hogar."
    )
    st.markdown(
        "- Material educativo elaborado por C.I.S."
    )


# =========================================================
# 6. CONTACTO Y COBERTURA
# =========================================================

with st.expander("📍 CONTACTO Y COBERTURA", expanded=False):

    st.subheader("Zonas de atención")

    st.markdown(
        """
        - **Capital:** 264 5171736
        - **Angaco:** 264 4730674
        - **San Martín:** 264 5035679
        - **Rivadavia:** 264 5115399
        """
    )

    st.divider()

    st.subheader("Contacto general")

    st.write("Correo electrónico: ecissalud@gmail.com")

    st.link_button(
        "Escribinos por WhatsApp",
        "https://wa.me/5492645115399"
    )


# =========================================================
# PIE DE PÁGINA
# =========================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center; padding:15px;">
        <strong style="color:#2E7D32;">
            C.I.S. - Cuidados Integrales de Salud
        </strong>
        <br>
        <span style="color:#777;">
            Promovemos bienestar, prevenimos enfermedades
            y acompañamos tu recuperación.
        </span>
    </div>
    """,
    unsafe_allow_html=True
)
