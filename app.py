import streamlit as str

# 1. Configuración de la página
str.set_page_config(page_title="Calculadora de Promedios", page_icon="🧮", layout="centered")

# Inyectamos estilos CSS personalizados para el fondo azul, destellos blancos, letras doradas 3D y movimientos continuos
str.markdown(
    """
    <style>
    /* Fondo azul profundo con animación de destellos blancos simulando estrellas que titilan */
    .stApp {
        background: radial-gradient(circle, #0B1D3A 0%, #050C1A 100%);
        background-image: 
            radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
            radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px),
            radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 40px);
        background-size: 550px 550px, 350px 350px, 250px 250px;
        background-position: 0 0, 40px 60px, 130px 270px;
        animation: estrellasTitilando 4s linear infinite alternate;
        color: #FAFAFA;
        overflow-x: hidden;
    }

    @keyframes estrellasTitilando {
        0% { opacity: 0.8; background-position: 0 0, 40px 60px, 130px 270px; }
        50% { opacity: 1; background-position: 10px 20px, 55px 40px, 115px 290px; }
        100% { opacity: 0.9; background-position: -5px -10px, 30px 70px, 140px 250px; }
    }

    /* Estilo premium con efecto 3D dorado y relieve para las preguntas */
    .texto-3d {
        font-size: 25px !important;
        font-weight: bold !important;
        color: #FFD700; /* Oro Puro */
        text-shadow: 
            0px 1px 0px #D4AF37,
            0px 2px 0px #AA7C11,
            0px 3px 0px #805B00,
            0px 4px 6px rgba(0,0,0,0.7);
        margin-bottom: 5px;
        margin-top: 15px;
        display: inline-block;
    }

    /* Animación de desvanecido suave con leve balanceo (Fade-in + Motion) */
    @keyframes fadeInMovimiento {
        0% { opacity: 0; transform: translateY(15px) scale(0.98); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }
    
    .efecto-aparecer-pregunta {
        animation: fadeInMovimiento 1.4s ease-out forwards;
    }
    
    .efecto-aparecer-respuesta {
        animation: fadeInMovimiento 1.2s ease-out forwards;
        font-size: 19px;
        font-weight: bold;
        color: #00FFFF; /* Cian eléctrico para contraste */
        margin-top: 5px;
        margin-bottom: 15px;
    }

    /* Animación para que la frase de ánimo titile (Blink continuo) */
    @keyframes titilar {
        0% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.4; transform: scale(1.02); }
        100% { opacity: 1; transform: scale(1); }
    }
    
    .frase-titilante {
        font-size: 22px !important;
        font-weight: bold !important;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
        animation: titilar 1.8s infinite ease-in-out;
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

# --- BLOQUE 1: BIENVENIDA Y NOMBRE ---
str.markdown('<div class="efecto-aparecer-pregunta"><p class="texto-3d">👋 ¡Bienvenido! Escribe tu nombre para empezar...</p></div>', unsafe_allow_html=True)
nombre = str.text_input("", placeholder="Tu nombre va aquí...", key="input_nombre")

if nombre:
    str.markdown(f'<div class="efecto-aparecer-respuesta">✨ Hola {nombre} ✨</div>', unsafe_allow_html=True)
    str.write("---")
    
    # --- BLOQUE 2: LA MATERIA ---
    str.markdown('<div class="efecto-aparecer-pregunta"><p class="texto-3d">📚 ¿Qué materia quieres promediar?</p></div>', unsafe_allow_html=True)
    materia = str.text_input("", placeholder="Ej. Matemáticas, Historia...", key="input_materia")
    
    if materia:
        str.markdown(f'<div class="efecto-aparecer-respuesta">🚀 ¡Dale! Hagamos tu promedio para {materia}...</div>', unsafe_allow_html=True)
        str.write("---")
        
        # --- BLOQUE 3: LAS NOTAS ---
        str.markdown('<div class="efecto-aparecer-pregunta"><p class="texto-3d">📝 Ingresa tus Notas:</p></div>', unsafe_allow_html=True)
        str.caption("La app solo promediará los campos con notas mayores a cero.")
        
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
                
                # --- NUEVA REGLA: GLOBOS NATIVOS A PARTIR DE 6 PUNTOS ---
                if promedio_redondeado >= 6.0:
                    color_frase = "#00FF66" # Verde éxito
                    
                    if promedio_redondeado >= 9.0:
                        mensaje_motivacional = f"¡Sos un fuera de serie en {materia}! ¡Una ovación de pie para vos! 👑🏆"
                    else:
                        mensaje_motivacional = f"¡Muy bien aprobado en {materia}! Todo esfuerzo da sus frutos. 📈👏"
                    
                    # Soltar globos garantizados en pantalla
                    str.balloons()
                    
                else:
                    mensaje_motivacional = f"A no bajar los brazos en {materia}. ¡La próxima la rompés seguro! 📚💪"
                    color_frase = "#FF3333" # Rojo alerta
                
                # FRASE ANIMADA QUE TITILA CONTINUAMENTE ABAJO
                str.markdown(f'<div class="frase-titilante" style="color: {color_frase};">✨ {mensaje_motivacional} ✨</div>', unsafe_allow_html=True)
else:
    str.warning("👋 ¡Bienvenido! Por favor ingresa tu nombre arriba para empezar.")
