import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Mobile Calc", page_icon="📱", layout="centered")

# 2. CSS personalizado para estilo de teléfono
st.markdown("""
    <style>
    /* Limitar el ancho para que parezca un teléfono */
    .block-container {
        max-width: 400px;
        padding-top: 2rem;
        padding-bottom: 2rem;
        background-color: #f0f2f6;
        border-radius: 30px;
        border: 8px solid #333;
        margin-top: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    
    /* Estilo para los botones */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border: none;
    }
    
    /* Centrar el título */
    h1 {
        text-align: center;
        color: #31333F;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Interfaz de usuario
st.title("📱 iCalc")
st.write("---")

# Entradas de datos (en vertical para móvil)
n1 = st.number_input("Número A", value=0.0, step=1.0)
n2 = st.number_input("Número B", value=0.0, step=1.0)

operacion = st.selectbox(
    "Operación",
    ["Suma", "Resta", "Multiplicación", "División", "Potencia"]
)

st.write("") # Espaciado

# 4. Lógica de cálculo
if st.button("CALCULAR"):
    resultado = 0
    error = False
    
    if operacion == "Suma":
        resultado = n1 + n2
    elif operacion == "Resta":
        resultado = n1 - n2
    elif operacion == "Multiplicación":
        resultado = n1 * n2
    elif operacion == "División":
        if n2 != 0:
            resultado = n1 / n2
        else:
            error = True
            st.error("❌ No se puede dividir por cero.")
    elif operacion == "Potencia":
        resultado = n1 ** n2

    if not error:
        st.balloons() # Animación para darle toque de app
        st.metric(label="Resultado", value=f"{resultado:g}")

st.markdown("---")
st.caption("Diseño optimizado para vista vertical")