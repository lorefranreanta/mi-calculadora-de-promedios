import streamlit as str
import urllib.parse

# 1. Configuración de la página
str.set_page_config(page_title="Calculadora de Promedios", page_icon="📊", layout="centered")

# Inyectamos estilos CSS personalizados para el modo oscuro y el efecto 3D en las preguntas
str.markdown(
    """
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    /* Estilo premium con efecto 3D y relieve para las preguntas */
    .texto-3d {
        font-size: 24px !important;
        font-weight: bold !important;
        color: #00F2FE;
        text-shadow: 
            0px 1px 0px #0072FF,
            0px 2px 0px #0072FF,
            0px 3px 0px #0072FF,
            0px 4px 5px rgba(0,0,0,0.5);
        margin-bottom: -10px;
        margin-top: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

str.title("📊 Calculadora de Promedios")

# Función para reiniciar todos los campos limpiando el estado de la sesión
def limpiar_campos():
    for key in str.session_state.keys():
        del str.session_state[key]

# 2. Entrada para el nombre del usuario y la materia con títulos 3D gigantes
str.markdown('<p class="texto-3d">👤 ¿Cómo te llamas?</p>', unsafe_allow_html=True)
nombre = str.text_input("", placeholder="Escribe tu nombre aquí...", key="input_nombre")

str.markdown('<p class="texto-3d">📚 ¿Qué materia estás cursando?</p>', unsafe_allow_html=True)
materia = str.text_input("", placeholder="Ej. Matemáticas, Historia...", key="input_materia")

# 3. Saludo animado y dinámico basado en las respuestas
if nombre and materia:
    str.info(f"✨ ¡Hola, {nombre}! Vamos a calcular tu promedio para **{materia}**.")
elif nombre:
    str.warning(f"👋 ¡Hola, {nombre}! Ahora introduce el nombre de la materia para continuar.")
else:
    str.warning("👋 ¡Hola! Por favor, escribe tu nombre y la materia arriba para comenzar.")

str.write("---") # Línea divisoria

str.markdown('<p class="texto-3d">📝 Ingresa tus Notas (Hasta 6):</p>', unsafe_allow_html=True)
str.caption("Deja en 0.0 las casillas de las notas que no utilices. La aplicación solo promediará los campos con notas mayores a cero.")

# 4. Entradas numéricas chicas organizadas en Dos Filas de 3 Columnas (6 notas en total)
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

# Filtramos las notas para calcular el promedio de forma dinámica (solo contamos las notas mayores a 0)
todas_las_notas = [nota1, nota2, nota3, nota4, nota5, nota6]
notas_validas = [n for n in todas_las_notas if n > 0.0]

# 5. Botones de Acción (Calcular y Limpiar puestos lado a lado)
btn_col1, btn_col2 = str.columns([2, 1])

with btn_col1:
    click_calcular = str.button("🔥 Calcular Promedio Real", type="primary", use_container_width=True)

with btn_col2:
    str.button("🗑️ Limpiar Todo", on_click=limpiar_campos, use_container_width=True)

# 6. Ejecución del cálculo si se presiona el botón
if click_calcular:
    if len(notas_validas) == 0:
        str.error("❌ Por favor, ingresa al menos una nota mayor a 0.0 para poder calcular un promedio.")
    else:
        promedio = sum(notas_validas) / len(notas_validas)
        promedio_redondeado = round(promedio, 2)
        
        nombre_usuario = nombre if nombre else "Amigo"
        materia_nombre = materia if materia else "tu materia"
        
        # Mensaje de éxito personalizado
        str.success(f"### 🎉 ¡Listo {nombre_usuario}! Tu promedio en **{materia_nombre}** es: **{promedio_redondeado}**")
        str.caption(f"Calculado en base a {len(notas_validas)} nota(s) ingresada(s).")
        
        # Lógica de mensajes motivacionales según la nota final
        if promedio_redondeado >= 7.0:
            mensaje_motivacional = f"¡Excelente nota en {materia_nombre}! Sigue así, estás brillando. 🌟🚀"
            str.balloons() # Animación de globos festivos
        elif promedio_redondeado >= 4.0:
            mensaje_motivacional = f"¡Buen trabajo! Aprobaste {materia_nombre}, pero puedes mejorar aún más. 📈👍"
        else:
            mensaje_motivacional = f"¡A estudiar más para {materia_nombre}! Tú puedes hacerlo mejor la próxima. 📚💪"
        
        # Mostrar el mensaje motivacional en la pantalla
        str.write(f"**Comentario:** {mensaje_motivacional}")
        str.write("---")
        
        # Crear el enlace de WhatsApp incluyendo todo el reporte interactivo
        mensaje_wsp = f"¡Hola! Soy {nombre_usuario}. Saqué un promedio final de: {promedio_redondeado} en la materia {materia_nombre}. {mensaje_motivacional}"
        texto_codificado = urllib.parse.quote(mensaje_wsp)
        url_wsp = f"https://whatsapp.com{texto_codificado}"
        
        # Botón de enlace para abrir WhatsApp
        str.link_button("📱 Compartir por WhatsApp", url_wsp)
