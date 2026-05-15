import streamlit as st

# Configuración de la página en modo ancho para disfrutar mejor los videos
st.set_page_config(page_title="Mi Cine sin Límites", page_icon="🎬", layout="wide")

st.title("🎬 Reproductor de Video Ilimitado")
st.write("Sube tus clips, películas o series favoritas y navega por tu lista de reproducción.")

# 1. Zona de carga de archivos de video (Sin límite de cantidad)
uploaded_files = st.file_uploader(
    "Arrastra o selecciona tus archivos de video (MP4, WEBM, MOV)", 
    type=["mp4", "webm", "mov"], 
    accept_multiple_files=True
)

# Inicializar el estado de la sesión para la lista de reproducción
if "video_playlist" not in st.session_state:
    st.session_state.video_playlist = []
if "current_video_index" not in st.session_state:
    st.session_state.current_video_index = 0

# Dividimos la pantalla en dos columnas: una para el video y otra para la lista
if uploaded_files:
    st.session_state.video_playlist = uploaded_files
    video_names = [file.name for file in st.session_state.video_playlist]
    
    col_video, col_lista = st.columns([3, 1])  # El video ocupa el 75% del ancho
    
    # --- COLUMNA DE LA DERECHA: LISTA DE REPRODUCCIÓN ---
    with col_lista:
        st.subheader("Lista de Videos")
        
        # Selector desplegable
        selected_video_name = st.selectbox(
            "Selecciona un video:", 
            options=video_names,
            index=st.session_state.current_video_index
        )
        
        # Actualizar índice si el usuario cambia el selector
        st.session_state.current_video_index = video_names.index(selected_video_name)
        
        st.write("---")
        
        # Controles de navegación de tipo Botón
        col_prev, col_next = st.columns(2)
        with col_prev:
            if st.button("⏮️ Anterior", use_container_width=True):
                if st.session_state.current_video_index > 0:
                    st.session_state.current_video_index -= 1
                    st.rerun()
                    
        with col_next:
            if st.button("Siguiente ⏭️", use_container_width=True):
                if st.session_state.current_video_index < len(st.session_state.video_playlist) - 1:
                    st.session_state.current_video_index += 1
                    st.rerun()
                    
        # Mostrar la lista completa abajo como referencia
        st.write("**En cola:**")
        for i, name in enumerate(video_names):
            if i == st.session_state.current_video_index:
                st.markdown(f"👉 **{name}** *(Reproduciendo)*")
            else:
                st.text(f"  {name}")

    # --- COLUMNA DE LA IZQUIERDA: EL REPRODUCTOR ---
    with col_video:
        current_file = st.session_state.video_playlist[st.session_state.current_video_index]
        
        st.markdown(f"### 📺 Viendo ahora: **{current_file.name}**")
        
        # Leer el archivo en bytes para el componente de video
        video_bytes = current_file.read()
        
        # Detectar el formato correcto
        extension = current_file.name.split('.')[-1].lower()
        format_type = f"video/{extension}" if extension != "mov" else "video/mp4" # Quicktime (.mov) a veces requiere mp4 para web
        
        # Renderizar el video
        st.video(video_bytes, format=format_type)

else:
    st.info("👋 Por favor, sube tus archivos de video en el panel de arriba para armar tu sala de cine.")