import streamlit as str
import urllib.parse

# 1. Configuración de la página
str.set_page_config(page_title="Calculadora de Promedios", page_icon="🧮", layout="centered")

# Inyectamos estilos CSS avanzados para el modo oscuro, efecto 3D y diseño de botones móviles
str.markdown(
    """
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .texto-3d {
        font-size: 24px !important;
        font-weight: bold !important;
        color: #00F2FE;
        text-shadow: 
            0px 1px 0px #0072FF,
            0px 2px 0px #0072FF,
            0px 3px 0px #0072FF,
            0px 4px 5px rgba(0,0,0,0.5);
        margin-bottom: 5px;
        margin-top: 15px;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .efecto-aparecer-pregunta {
        animation: fadeIn 1.5s ease-out forwards;
    }
    .efecto-aparecer-respuesta {
        animation: fadeIn 1.2s ease-out forwards;
        font-size: 18px;
        font-weight: 500;
        color: #FF007F;
        margin-top: 5px;
        margin-bottom: 15px;
    }
    /* Botones web nativos premium compatibles con Android/iOS */
    .boton-wsp-movil {
        display: block;
        width: 100%;
        text-align: center;
        background-color: #25D366;
        color: white !important;
        padding: 12px 0px;
        font-weight: bold;
        font-size: 16px;
        border-radius: 8px;
        text-decoration: none;
        margin-top: 8px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.3);
        transition: transform 0.1s ease-in-out;
    }
    .boton-wsp-movil:active {
        transform: scale(0.98);
    }
    </style>
    """,
    unsafe_allow_html=True
)

str.title("🧮 Calculadora de Promedios")
str.write("---")

def limpiar_campos():
    for key in str.session_state.keys():
        del str.session_state[key]

# --- BLOQUE 1: EL NOMBRE ---
str.markdown('<div class="efecto-aparecer-pregunta"><p class="texto-3d">👋 Hola, ¿cómo te llamas?</p></div>', unsafe_allow_html=True)
nombre = str.text_input("", placeholder="Escribe tu nombre aquí y presiona Enter...", key="input_nombre")

if nombre:
    str.markdown(f'<div class="efecto-aparecer-respuesta">✨ ¡Hola, {nombre}! ✨</div>', unsafe_allow_html=True)
    str.write("---")
    
    # --- BLOQUE 2: LA MATERIA ---
    str.markdown('<div class="efecto-aparecer-pregunta"><p class="texto-3d">📚 ¿Qué materia quieres promediar?</p></div>', unsafe_allow_html=True)
    materia = str.text_input("", placeholder="Ej. Matemáticas, Historia...", key="input_materia")
    
    if materia:
        str.markdown(f'<div class="efecto-aparecer-respuesta">🚀 ¡Dale! Hagamos tu promedio para {materia}...</div>', unsafe_allow_html=True)
        str.write("---")
        
        # --- BLOQUE 3: LAS NOTAS ---
        str.markdown('<div class="efecto-aparecer-pregunta"><p class="texto-3d">📝 Ingresa tus Notas:</p></div>', unsafe_allow_html=True)
        str.caption("Deja en 0.0 las casillas que no uses. La app solo promediará los campos con notas mayores a cero.")
        
        # Fila 1
        col1, col2, col3 = str.columns(3)
        with col1:
            nota1 = str.number_input("Nota 1:", min_value=0.0, max_value=10.0, value=0.0, step=0.1, key="n1")
        with col2:
            nota2 = str.number_input("Nota 2:", min_value=0.0, max_value=10.0, value=0.0, step=0.1, key="n2")
        with col3:
            nota3 = str.number_input("Nota 3:", min_value=0.0, max_value=10.0, value=0.0, step=0.1, key="n3")

        # Fila 2
        col4, col5, col6 = str.columns(3)
        with col4:
            nota4 = str.number_input("Nota 4:", min_value=0.0, max_value=10.0, value=0.0, step=0.1, key="n4")
        with col5:
            nota5 = str.number_input("Nota 5:", min_value=0.0, max_value=10.0, value=0.0, step=0.1, key="n5")
        with col6:
            nota6 = str.number_input("Nota 6:", min_value=0.0, max_value=10.0, value=0.0, step=0.1, key="n6")

        str.write("---")

        todas_las_notas = [nota1, nota2, nota3, nota4, nota5, nota6]
        notas_validas = [n for n in todas_las_notas if n > 0.0]

        btn_col1, btn_col2 = str.columns(2)
        with btn_col1:
            click_calcular = str.button("🔥 Calcular Promedio Real", type="primary", use_container_width=True)
        with btn_col2:
            str.button("🗑️ Limpiar Todo", on_click=limpiar_campos, use_container_width=True)

        if click_calcular:
            if len(notas_validas) == 0:
                str.error("❌ Por favor, ingresa al menos una nota mayor a 0.0.")
            else:
                promedio = sum(notas_validas) / len(notas_validas)
                promedio_redondeado = round(promedio, 2)
                
                str.success(f"### 🎉 ¡Listo {nombre}! Tu promedio en **{materia}** es: **{promedio_redondeado}**")
                
                if promedio_redondeado >= 7.0:
                    mensaje_motivacional = f"¡Excelente nota en {materia}! Sigue así, estás brillando. 🌟🚀"
                    str.balloons()
                elif promedio_redondeado >= 4.0:
                    mensaje_motivacional = f"¡Buen trabajo! Aprobaste {materia}, pero puedes mejorar aún más. 📈👍"
                else:
                    mensaje_motivacional = f"¡A estudiar más para {materia}! Tú puedes hacerlo mejor la próxima. 📚💪"
                
                str.write(f"**Comentario:** {mensaje_motivacional}")
                str.write("---")
                
                # --- SOLUCIÓN DE ENLACE COMPATIBLE CON MÓVILES ---
                wsp_col1, wsp_col2 = str.columns(2)
                url_de_tu_app = "https://streamlit.app"
                
                with wsp_col1:
                    msg_nota = f"¡Hola! Soy {nombre}. Saqué un promedio final de: {promedio_redondeado} en la materia {materia}. {mensaje_motivacional}"
                    # Usamos el enlace wa.me nativo para celulares
                    url_nota = f"https://wa.me{urllib.parse.quote(msg_nota)}"
                    str.markdown(f'<a href="{url_nota}" target="_blank" class="boton-wsp_movil" style="background-color: #25D366;">📱 Compartir mi Promedio</a>', unsafe_allow_html=True)
                
                with wsp_col2:
                    msg_app = f"¡Hola! Te comparto esta Calculadora de Promedios interactiva hecha en Python. ¡Calcula tus notas aquí de forma simple! 👉 {url_de_tu_app}"
                    # Usamos el enlace wa.me nativo para celulares
                    url_app = f"https://wa.me{urllib.parse.quote(msg_app)}"
                    str.markdown(f'<a href="{url_app}" target="_blank" class="boton-wsp_movil" style="background-color: #0072FF;">🌐 Compartir esta Aplicación</a>', unsafe_allow_html=True)
else:
    str.warning("👋 ¡Bienvenido! Por favor ingresa tu nombre arriba para empezar.")
