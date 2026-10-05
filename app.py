import streamlit as str
import urllib.parse

# 1. Configuración de la página
str.set_page_config(page_title="Calculadora de Promedios", page_icon="📊", layout="centered")

# Inyectamos estilos CSS corregidos para asegurar el fondo oscuro y textos claros
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

# 2. Entrada para el nombre del usuario
nombre = str.text_input("¿Cómo te llamas?", placeholder="Escribe tu nombre aquí...")

# 3. Saludo animado y dinámico si el usuario escribe su nombre
if nombre:
    str.info(f"✨ ¡Hola, {nombre}! Vamos a calcular tu promedio de notas.")
else:
    str.warning("👋 ¡Hola! Por favor, escribe tu nombre arriba para comenzar.")

str.write("---") # Línea divisoria

# 4. Entradas numéricas para las notas
nota1 = str.number_input("Nota 1:", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
nota2 = str.number_input("Nota 2:", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
nota3 = str.number_input("Nota 3:", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

# 5. Botón para calcular
if str.button("Calcular Promedio", type="primary"):
    promedio = (nota1 + nota2 + nota3) / 3
    promedio_redondeado = round(promedio, 2)
    
    # Mensaje de éxito personalizado con su nombre
    nombre_usuario = nombre if nombre else "Amigo"
    str.success(f"### 🎉 ¡Listo {nombre_usuario}! Tu promedio final es: **{promedio_redondeado}**")
    
    # Crear el enlace de WhatsApp incluyendo el nombre
    mensaje_wsp = f"¡Hola! Soy {nombre_usuario}. Saqué un promedio final de: {promedio_redondeado}."
    texto_codificado = urllib.parse.quote(mensaje_wsp)
    url_wsp = f"https://whatsapp.com{texto_codificado}"
    
    # Botón de enlace para abrir WhatsApp
    str.link_button("📱 Compartir por WhatsApp", url_wsp)

