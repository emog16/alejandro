import streamlit as st

# Configuración de la página
st.set_page_config(page_title="La Cava Real - Licores Pro", page_icon="🍷", layout="wide")

# Inicializar carrito
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

# --- INVENTARIO DE BEBIDAS ---
inventario = {
    "Vinos y Tintos": [
        {"nombre": "Cabernet Sauvignon Reserva", "precio": 45, "origen": "Valle de Maipo, Chile", "desc": "Cuerpo intenso con notas de frutos rojos y roble."},
        {"nombre": "Chardonnay Gran Blanco", "precio": 38, "origen": "Mendoza, Argentina", "desc": "Equilibrado, con toques de vainilla y manzana verde."},
        {"nombre": "Espumante Brut Imperial", "precio": 65, "origen": "Champagne, Francia", "desc": "Burbuja fina y elegante para celebraciones especiales."},
        {"nombre": "Pinot Noir Selección", "precio": 52, "origen": "Oregon, USA", "desc": "Suave, sedoso y con final persistente."}
    ],
    "Destilados": [
        {"nombre": "Whisky Single Malt 12 años", "precio": 120, "grado": "40%", "desc": "Ahumado suave con notas de miel y brezo."},
        {"nombre": "Tequila Reposado Premium", "precio": 85, "grado": "38%", "desc": "100% Agave azul, reposado en barricas de roble americano."},
        {"nombre": "Gin Botánico Artesanal", "precio": 42, "grado": "43%", "desc": "Destilado con 12 botánicos incluyendo enebro y cítricos."},
        {"nombre": "Ron Añejo Solera", "precio": 75, "grado": "40%", "desc": "Mezcla de rones de hasta 23 años de envejecimiento."}
    ],
    "Cervezas Artesanales": [
        {"nombre": "Double IPA", "precio": 8, "estilo": "India Pale Ale", "desc": "Amargor potente con explosión de lúpulo tropical."},
        {"nombre": "Stout de Chocolate", "precio": 7, "estilo": "Porter/Stout", "desc": "Cuerpo denso, notas de café tostado y cacao."},
        {"nombre": "Belgian Tripel", "precio": 10, "estilo": "Ale Belga", "desc": "Alta graduación, especiada y frutal."},
        {"nombre": "Pilsner Checa", "precio": 6, "estilo": "Lager", "desc": "Limpia, refrescante y con final floral."}
    ],
    "Mixología y Accesorios": [
        {"nombre": "Set de Coctelería Pro", "precio": 55, "tipo": "Kit", "desc": "Incluye coctelera, jigger, strainer y cuchara de bar."},
        {"nombre": "Bitter de Angostura", "precio": 22, "tipo": "Insumo", "desc": "Esencial para equilibrar tus cócteles clásicos."},
        {"nombre": "Copas de Cristal (Par)", "precio": 35, "tipo": "Cristalería", "desc": "Diseñadas para maximizar la oxigenación del vino."},
        {"nombre": "Hielo de Lenta Fusión", "precio": 12, "tipo": "Insumo", "desc": "Esferas de hielo cristalino para destilados premium."}
    ]
}

# --- INTERFAZ ---
st.title("🍷 La Cava Real: Selección de Élite")
st.markdown("---")

# Barra lateral para el Carrito
with st.sidebar:
    st.header("🛒 Tu Carrito")
    if not st.session_state.carrito:
        st.write("El carrito está vacío.")
    else:
        for i, item in enumerate(st.session_state.carrito):
            col_txt, col_del = st.columns([4, 1])
            col_txt.write(f"**{item['nombre']}** (${item['precio']})")
            if col_del.button("❌", key=f"del_{i}"):
                st.session_state.carrito.pop(i)
                st.rerun()
        
        total = sum(item['precio'] for item in st.session_state.carrito)
        st.divider()
        st.subheader(f"Total: ${total}")
        if st.button("Finalizar Compra", use_container_width=True):
            st.balloons()
            st.success("Pedido recibido. Preparando despacho...")
            st.session_state.carrito = []

# Cuerpo principal con pestañas
tabs = st.tabs(list(inventario.keys()))

for i, categoria in enumerate(inventario.keys()):
    with tabs[i]:
        cols = st.columns(2)
        for idx, item in enumerate(inventario[categoria]):
            with cols[idx % 2]:
                with st.container(border=True):
                    # Título del producto
                    st.subheader(item['nombre'])
                    
                    # Detalles específicos según la categoría
                    if 'origen' in item: st.write(f"📍 **Origen:** {item['origen']}")
                    if 'grado' in item: st.write(f"🔥 **Graduación:** {item['grado']}")
                    if 'estilo' in item: st.write(f"🍺 **Estilo:** {item['estilo']}")
                    if 'tipo' in item: st.write(f"🛠️ **Tipo:** {item['tipo']}")
                    
                    st.write(f"💵 **Precio:** ${item['precio']}")
                    st.caption(item['desc']) # Texto más pequeño para la descripción
                    
                    if st.button(f"Añadir al carrito", key=f"add_{categoria}_{idx}"):
                        st.session_state.carrito.append(item)
                        st.toast(f"Añadido: {item['nombre']}", icon="✅")

st.markdown("---")
st.warning("⚠️ Beber en exceso es perjudicial para la salud. Venta prohibida a menores de 18 años.")
st.caption("E-Commerce desarrollado para Licorerías Premium © 2024")