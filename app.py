import streamlit as str
import urllib.parse

# Configuración del diseño de la página
str.set_page_config(page_title="Calculadora de Promedios", page_icon="📊", layout="centered")

str.title("📊 Calculadora de Promedios")
str.write("Introduce tus notas aquí abajo para calcular tu promedio final y compartirlo.")

# Entradas numéricas interactivas
nota1 = str.number_input("Nota 1:", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
nota2 = str.number_input("Nota 2:", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
nota3 = str.number_input("Nota 3:", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

# Botón para calcular
if str.button("Calcular Promedio", type="primary"):
    promedio = (nota1 + nota2 + nota3) / 3
    promedio_redondeado = round(promedio, 2)
    
    # Mostrar el resultado de manera llamativa
    str.success(f"### El promedio final es: **{promedio_redondeado}**")
    
    # Crear el enlace de WhatsApp
    mensaje_wsp = f"¡Hola! Saqué un promedio final de: {promedio_redondeado}."
    texto_codificado = urllib.parse.quote(mensaje_wsp)
    url_wsp = f"https://whatsapp.com{texto_codificado}"
    
    # Botón de enlace para abrir WhatsApp
    str.link_button("📱 Compartir por WhatsApp", url_wsp)
