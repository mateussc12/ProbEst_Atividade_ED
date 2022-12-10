"""
Para rodar o código são necessárias as seguintes bibliotecas : matplotlib, numpy, pandas.
Caso alguma delas não esteja instalada, ir no terminal e escrever:
pip install *nome da biblioteca*
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

#   Lendo os dados
df = pd.read_csv('IDEB_2017.csv')

pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 15)

df_ID = df['ID']
df_cidades = df['V1']
df_IDEB_anos_iniciais = df['V6']
df_IDEB_anos_finais = df['V7']
df_V6_crescente_IDEB = df.sort_values(by='V6')
df_V7_crescente_IDEB = df.sort_values(by='V7')

#   estatísticas

#   anos iniciais
media_IDEB_anos_iniciais = df_IDEB_anos_iniciais.mean()
describe_IDEB_anos_iniciais = df_IDEB_anos_iniciais.describe()
variancia_IDEB_anos_iniciais = df_IDEB_anos_iniciais.var()
#   78 termos
#   média = 5.906
#   variância = 0.187
#   desvio padrão = 0.432
#   min = 4.9
#   Q1 = 25% = 5.6
#   Q2 = 50% = mediana = 5.8
#   Q3 = 75% = 6.2
#   max = 6.8
filt_ini_maior = (df_V6_crescente_IDEB['V6'] > media_IDEB_anos_iniciais)
cidades_acima_media_anos_iniciais = df_V6_crescente_IDEB.loc[filt_ini_maior][['ID', 'V1', 'V6']]
IDs_cidades_acima_media_anos_iniciais = cidades_acima_media_anos_iniciais['ID']
nome_cidades_acima_media_anos_iniciais = cidades_acima_media_anos_iniciais['V1']
IDEB_cidades_acima_media_anos_iniciais = cidades_acima_media_anos_iniciais['V6']
#   32 cidades com o IDEB acima da média
filt_ini_menor_ou_igual_media_iniciais = (df_V6_crescente_IDEB['V6'] <= media_IDEB_anos_iniciais)
cidades_menor_ou_igual_media_iniciais = df_V6_crescente_IDEB.loc[filt_ini_menor_ou_igual_media_iniciais][
    ['ID', 'V1', 'V6']]
IDs_cidades_menor_ou_igual_media_iniciais = cidades_menor_ou_igual_media_iniciais['ID']
nome_cidades_menor_ou_igual_media_iniciais = cidades_menor_ou_igual_media_iniciais['V1']
IDEB_cidades_menor_ou_igual_media_iniciais = cidades_menor_ou_igual_media_iniciais['V6']
#   46 cidades com o IDEB abaixo ou igual a média

#   anos finais
media_IDEB_anos_finais = df_IDEB_anos_finais.mean()
describe_IDEB_anos_finais = df_IDEB_anos_finais.describe()
variancia_IDEB_anos_finais = df_IDEB_anos_finais.var()
#   78 termos
#   média 4.654
#   variância = 0.256
#   desvio padrão 0.506
#   min = 3.7
#   Q1 = 25% = 4.3
#   Q2 = 50% = mediana = 4.6
#   Q3 = 75% = 5
#   max = 5.7
filt_fin_maior = (df_V7_crescente_IDEB['V7'] > media_IDEB_anos_finais)
cidades_acima_media_anos_finais = df_V7_crescente_IDEB.loc[filt_fin_maior][['ID', 'V1', 'V7']]
IDs_cidades_acima_media_anos_finais = cidades_acima_media_anos_finais['ID']
nome_cidades_acima_media_anos_finais = cidades_acima_media_anos_finais['V1']
IDEB_cidades_acima_media_anos_finais = cidades_acima_media_anos_finais['V7']
#   36 cidades com o IDEB acima da média
filt_fin_menor_ou_igual_media_finais = (df_V7_crescente_IDEB['V7'] <= media_IDEB_anos_finais)
cidades_menor_ou_igual_media_finais = df_V7_crescente_IDEB.loc[filt_fin_menor_ou_igual_media_finais][['ID', 'V1', 'V7']]
IDs_cidades_menor_ou_igual_media_finais = cidades_menor_ou_igual_media_finais['ID']
nome_cidades_menor_ou_igual_media_finais = cidades_menor_ou_igual_media_finais['V1']
IDEB_cidades_menor_ou_igual_media_finais = cidades_menor_ou_igual_media_finais['V7']
#   42 cidades com o IDEB abaixo ou igual a média


#   box plot inicio
box_plot, box_plot_ini_fin = plt.subplots()

bplot = box_plot_ini_fin.boxplot([df['V6'], df['V7']], labels=['Anos iniciais', 'Anos finais'])

box_plot_ini_fin.set_ylim(3.5, 7)
#   box plot fim

plt.tight_layout()
plt.show()
