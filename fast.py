import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact
from IPython.display import clear_output

#exportar a tabela

caminho_excel = r'C:\Users\joao.mmelo\Downloads\teste.xlsx'

dados_excel = pd.read_excel(caminho_excel)

display(dados_excel)

# Para usar datas

from datetime import datetime, time

#limitando tempo e filtros

dados_excel['DURATION'] = pd.to_datetime(dados_excel['DURATION'], format = '%H:%M:%S').dt.time

limite_tempo = time(0,0,10)


agosto = dados_excel[(dados_excel['SEGSTART'] <= '31/08/2023') & (dados_excel['SEGSTART'] >= '01/08/2023')]
setembro = dados_excel[(dados_excel['SEGSTART'] <= '30/09/2023') & (dados_excel['SEGSTART'] >= '01/09/2023')]
outubro = dados_excel[(dados_excel['SEGSTART'] <= '31/10/2023') & (dados_excel['SEGSTART'] >= '01/10/2023')]

dados_filtrados = dados_excel[(dados_excel['AGT_RELEASED'] == 1) & (dados_excel['TRANSFERRED'] == 0)&(dados_excel['DURATION'] < limite_tempo)]

display(dados_filtrados)

#trazer informações filtradas e consolidadas

contagem_nomes = dados_filtrados['ANSLOGIN'].value_counts()
display(contagem_nomes)


#Criar o grafico

# Crie um widget de seleção para escolher o mês
meses = list(range(1, 13))  # De janeiro a dezembro
import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact
from IPython.display import clear_output

# Suponha que 'dados_filtrados' seja o DataFrame com suas colunas 'SEGSTART' e 'ANSLOGIN'
# Certifique-se de que 'SEGSTART' seja uma coluna de data (caso contrário, você pode converter usando pd.to_datetime)

# Função para criar o gráfico de barras com filtro por mês e rótulos de contagem
def criar_grafico_mes(mes):
    clear_output()  # Limpa qualquer gráfico anterior
    dados_filtrados_mes = dados_filtrados[dados_filtrados['SEGSTART'].dt.month == mes]
    if not dados_filtrados_mes.empty: 
        contagem_nomes_mes = dados_filtrados_mes['ANSLOGIN'].value_counts() 

    else:
        print("Não há dados para o mês selecionado.")
        

 # Define o tamanho da figura (aumente os valores para fazer o gráfico maior)
    plt.figure(figsize=(35,9.8))  # Ajuste os valores de largura e altura conforme necessário

   
 # Crie um gráfico de barras
    ax = contagem_nomes_mes.plot(kind='bar')
 # Adicione rótulos de contagem acima de cada barra
    for i, v in enumerate(contagem_nomes_mes):
        ax.text(i, v + 1, str(v), ha='center', va='bottom')

    # Defina rótulos dos eixos
    plt.xlabel('ANSLOGIN')
    plt.ylabel('Contagem')
    plt.xlim(-0.5, len(contagem_nomes_mes) - 0.5)  # Ajuste os valores para os limites do eixo X
    plt.ylim(0, max(contagem_nomes_mes) + 5)  # Ajuste os valores para os limites do eixo Y

        # Exiba o gráfico
    plt.show()
        
# Crie um widget de seleção para escolher o mês
meses = list(range(1, 13))  # De janeiro a dezembro
interact(criar_grafico_mes, mes=widgets.Dropdown(options=meses, description='Mês:'))

________________________________________________________________________________________________________________________________________________________________________________________________________________

#Para criar o grafico HTML 

import pandas as pd
import plotly.express as px
import ipywidgets as widgets
from ipywidgets import interact
from IPython.display import display

def criar_grafico_interativo(meses_selecionados):
    dados_filtrados_meses = dados_filtrados[dados_filtrados['SEGSTART'].dt.month.isin(meses_selecionados)]
    contagem_nomes_meses = dados_filtrados_meses['ANSLOGIN'].value_counts()
    
    
    fig = px.bar(contagem_nomes_meses, x=contagem_nomes_meses.index, y=contagem_nomes_meses.values,
                 labels={'x': 'ANSLOGIN', 'y': 'Contagem'},
                 title=f'Contagem de ANSLOGIN para os meses selecionados')
    
  
    fig.show()

meses = list(range(1, 13))  # De janeiro a dezembro
meses_selecionados = widgets.SelectMultiple(options=meses, description='Meses:')
interact(criar_grafico_interativo, meses_selecionados=meses_selecionados)
