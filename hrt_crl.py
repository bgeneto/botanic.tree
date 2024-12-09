import streamlit as st
import math

st.header("Universidade de Brasília")
st.subheader("Faculdade UnB de Planaltina")
st.subheader("Desenvolvimento em Computação Ciêntífica.")
st.text("Olá, bem vindo. Você está na plataforma Inov Up Botanic. Supondo que você está em campo,\
aqui você obter medidas mais precisas das árvores. O nosso algoritimo necessita do uso de astrolábio além do conhecimento da sua própria altura.")

st.header("Calculadora :material/forest:")

dist = st.number_input("Digite a distancia em metros:", min_value=0.0, step=0.1)

altura = st.number_input("Digite a sua altura em metros:", min_value=0.0, step=0.1)

angulo = st.number_input("Digite o ângulo aferido no astrolábio (em graus):", min_value=0.0, step=0.1)

 
h = None

def calcula_altura():
    h = math.tan(math.radians(angulo))*dist + altura
    return round(h, 2)
    
if st.button("A altura aproximada é...", icon=":material/calculate:"):
    st.success(f"A altura da árvore :material/forest: medida é de {calcula_altura()} metros.", icon=":material/thumb_up:")

