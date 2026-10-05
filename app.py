import streamlit as str
import urllib.parse

# 1. Configuración de la página
str.set_page_config(page_title="Calculadora de Promedios", page_icon="📊", layout="centered")

# Inyectamos estilos CSS para asegurar el fondo oscuro y textos claros
str.markdown(
    """
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    </style>
    """,
    unsafe_allow_html=True
)

str.title("📊 Calculadora de Promedios")

# 2. Entrada para el nombre del usuario y la materia
nombre = str.text_input("¿Cómo te llamas?", placeholder="Escribe tu nombre aquí...")
materia = str.text_input("¿Qué materia o asignatura estás cursando?", placeholder="Ej. Matemáticas, Historia...")

# 3. Saludo animado y dinámico basado en las respuestas
if nombre and materia:
    str.info(f"✨ ¡Hola, {nombre}! Vamos a calcular tu promedio para **{materia}**.")
elif nombre:
    str.warning(f"👋 ¡Hola, {nombre}! Ahora introduce el nombre de la materia para continuar.")
else:
    str.warning("👋 ¡Hola! Por favor, escribe tu nombre y la materia arriba para comenzar.")

str.write("---") # Línea divisoria

# 4. Entradas numéricas chicas (Organizadas en 3 columnas más angostas)
col1, col2, col3 = str.columns(3)

with col1:
    nota1 = str.number_input("Nota 1:", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

with col2:
    nota2 = str.number_input("Nota 2:", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

with col3:
    nota3 = str.number_input("Nota 3:", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

str.write("---")

# 5. Botón para calcular
if str.button("Calcular Promedio", type="primary"):
    promedio = (nota1 + nota2 + nota3) / 3
    promedio_redondeado = round(promedio, 2)
    
    nombre_usuario = nombre if nombre else "Amigo"
    materia_nombre = materia if materia else "tu materia"
    
    # Mensaje de éxito personalizado
    str.success(f"### 🎉 ¡Listo {nombre_usuario}! Tu promedio en **{materia_nombre}** es: **{promedio_redondeado}**")
    
    # Lógica de mensajes personalizados según la nota
    if promedio_redondeado >= 7.0:
        mensaje_motivacional = f"¡Excelente nota en {materia_nombre}! Sigue así, estás brillando. 🌟🚀"
        str.balloons() # Animación de globos
    elif promedio_redondeado >= 4.0:
        mensaje_motivacional = f"¡Buen trabajo! Aprobaste {materia_nombre}, pero puedes mejorar aún más. 📈👍"
    else:
        mensaje_motivacional = f"¡A estudiar más para {materia_nombre}! Tú puedes hacerlo mejor la próxima. 📚💪"
    
    # Mostrar el mensaje motivacional en la pantalla
    str.write(f"**Comentario:** {mensaje_motivacional}")
    str.write("---")
    
    # Crear el enlace de WhatsApp incluyendo nombre, materia y promedio
    mensaje_wsp = f"¡Hola! Soy {nombre_usuario}. Saqué un promedio final de: {promedio_redondeado} en la materia {materia_nombre}. {mensaje_motivacional}"
    texto_codificado = urllib.parse.quote(mensaje_wsp)
    url_wsp = f"https://whatsapp.com{texto_codificado}"
    
    # Botón de enlace para abrir WhatsApp
    str.link_button("📱 Compartir por WhatsApp", url_wsp)
