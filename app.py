import streamlit as str

# 1. Configuración de la página
str.set_page_config(page_title="Calculadora de Promedios", page_icon="🧮", layout="centered")

# Inyectamos estilos CSS para el modo oscuro, efecto 3D, desvanecido y la animación que TITILA
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
    /* Animación para que la frase de ánimo titile (Blink) */
    @keyframes titilar {
        0% { opacity: 1; }
        50% { opacity: 0.3; }
        100% { opacity: 1; }
    }
    .frase-titilante {
        font-size: 20px !important;
        font-weight: bold !important;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
        animation: titilar 1.5s infinite ease-in-out;
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
        
        col1, col2, col3 = str.columns(3)
        with col1:
            nota1 = str.number_input("Nota 1:", min_value=0.0, max_value=10.0, value=0.0, step=0.1, key="n1")
        with col2:
            nota2 = str.number_input("Nota 2:", min_value=0.0, max_value=10.0, value=0.0, step=0.1, key="n2")
        with col3:
            nota3 = str.number_input("Nota 3:", min_value=0.0, max_value=10.0, value=0.0, step=0.1, key="n3")

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
                
                # --- NUEVA LÓGICA: Audios y Frases Titilantes ---
                if promedio_redondeado >= 9.0:
                    mensaje_motivacional = f"¡Sos un fuera de serie en {materia}! ¡Una ovación de pie para vos! 👑🏆"
                    color_frase = "#00FF66" # Verde brillante
                    # Enlace de sonido: Ovación / Cheering masivo
                    url_sonido = "https://mixkit.co"
                    str.balloons()
                elif promedio_redondeado >= 4.0:
                    mensaje_motivacional = f"¡Muy bien aprobado en {materia}! Todo esfuerzo da sus frutos. 📈👏"
                    color_frase = "#00F2FE" # Celeste neón
                    # Enlace de sonido: Aplausos estándar
                    url_sonido = "https://mixkit.co"
                else:
                    mensaje_motivacional = f"A no bajar los brazos en {materia}. ¡La próxima la rompés seguro! 📚💪"
                    color_frase = "#FF3333" # Rojo alerta
                    # Enlace de sonido: Efecto clásico de error / desaprobación (trombón triste o fail)
                    url_sonido = "https://mixkit.co"
                
                # REPRODUCTOR DE AUDIO OCULTO HTML (Se ejecuta solo al calcular)
                str.markdown(f'<iframe src="{url_sonido}" allow="autoplay" style="display:none;"></iframe>', unsafe_allow_html=True)
                
                # FRASE ANIMADA QUE TITILA EN PANTALLA
                str.markdown(f'<div class="frase-titilante" style="color: {color_frase};">✨ {mensaje_motivacional} ✨</div>', unsafe_allow_html=True)
else:
    str.warning("👋 ¡Bienvenido! Por favor ingresa tu nombre arriba para empezar.")
