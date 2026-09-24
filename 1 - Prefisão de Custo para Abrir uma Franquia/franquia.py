# Para a exibição das informações
import streamlit as st
# Para tratamento e importação dos dados
import pandas as pd
# Criar o modelo de Regressão Linear
from sklearn.linear_model import LinearRegression
# Gerar os gráficos
import matplotlib.pyplot as plt


# Muda o estilo da página para 'wide' e configurar o nome da guia do navegador
st.set_page_config(layout="wide", page_title="Previsão Custo Franquia", page_icon=":man_student:")

# Título para a aplicação
st.title("Previsão Inicial de Custo para Franquia")

# Leitura do arquivo CSV
dados = pd.read_csv("./1 - Prefisão de Custo para Abrir uma Franquia/bdFranquia.csv", sep=";")

# Separar os dados do target
x = dados[['FrqAnual']]
y = dados['CusInic']

# Criação do Modelo de Regressão Linear
modelo = LinearRegression().fit(x, y)

# Organização das colunas do Streamlit
col1, col2 = st.columns(2)

# Cria a col1
with col1:
    # Cria uma header para a col1
    st.header("Dados")

    # Cria uma tabela mostrando as 10 primeiras linhas
    st.table(dados.head(10))


# Cria a col2
with col2:
    # Cria um header para a col2
    st.header("Gráfico de Dispersão")

    # Cria um gráfico de dispersão
    fig, ax = plt.subplots()
    # Define que 'x', sendo uma variável independente e 'y' como variável dependente, estará na cor Azul
    ax.scatter(x, y, color='blue')
    # Define a linha de regressão na cor vermelha
    ax.plot(x, modelo.predict(x), color='red')
    # Exibe/Imprime o Gráfico
    st.pyplot(fig)


# Parte preditiva para o usuário
# Header para separar
st.header("Valor Anual da Franquia: ")

# Campo para o usuário informar o valor
novo_valor = st.number_input("Insira Novo Valor", min_value=1.0, value=1500.0, step=0.01)

# Botão que realiza o processo de processar a ação, encaminhando o valor inserido em 'novo_valor' para a previsão
processar = st.button("Processar")


# Se o usuário clicar em processar
if processar:
    # Converte o dado obtido em 'novo_valor' para o mesmo formato, pois o modelo só aceita dados de mesmo tipo, com coluna no mesmo nome
    dados_novo_valor = pd.DataFrame([[novo_valor]], columns=['FrqAnual'])

    # Aqui, é usado o modelo treinado anteriormente, encaminha o valor recebido e convertido, gerando uma previsão
    prev = modelo.predict(dados_novo_valor)

    # Mostra o resultado da previsão, de acordo com o valor informado e os dados do modelo
    #st.header(f"Previsão de Custo Inicial R$: {prev[0]:.2f}")
    # Mesma coisa da linha anterior, mas aqui, realizei uma pequena tratativa, mudando o separador decimal e de milhar
    st.header(f"Previsão de Custo Inicial R$: {prev[0]:,.2f}".replace(".", "@").replace(",", ".").replace("@", ","))