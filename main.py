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
df = pd.read_csv(r'C:\Users\mateu\PycharmProjects\ProbEst_Atividade_ED\IDEB_2017.csv')

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


#   gráfico de dispersão inicio
IDEB_dispersao, IDEB = plt.subplots()

IDEB.scatter(df_ID, df_IDEB_anos_iniciais, edgecolors='black', alpha=0.75, label='Anos iniciais')
IDEB.scatter(df_ID, df_IDEB_anos_finais, edgecolors='black', alpha=0.75, label='Anos finais')

IDEB.axhline(media_IDEB_anos_iniciais, label='Média dos anos iniciais = 5.906', color='#5F9EA0', alpha=0.5)
IDEB.axhline(media_IDEB_anos_finais, label='Média dos anos finais = 4.654', color='#DC143C', alpha=0.5)

IDEB.legend(loc=(0.6, 0.83), fontsize='x-small', framealpha=1)

IDEB.set_title('Índice de Desenvolvimento da Educação Básica')
IDEB.set_xlabel('ID da cidade')
IDEB.set_ylabel('Nota no IDEB')
#   gráfico de dispersão fim


#   gráficos de barras horizontais relacionando as cidades e as médias iniciais

#   horizontal anos iniciais
#   acima da média
Cidades_acima_media_barras_ini_h, IDEB_acima_medias_ini = plt.subplots()

IDEB_acima_medias_ini.barh(nome_cidades_acima_media_anos_iniciais,
                           IDEB_cidades_acima_media_anos_iniciais, label='Cidades acima da média do IDEB anos iniciais')

IDEB_acima_medias_ini.set_yticks(nome_cidades_acima_media_anos_iniciais)
IDEB_acima_medias_ini.set_yticklabels(nome_cidades_acima_media_anos_iniciais, fontsize=10)

IDEB_acima_medias_ini.axvline(media_IDEB_anos_iniciais, label='Média anos iniciais = 5.906', color='#DC143C', alpha=1)

IDEB_acima_medias_ini.set_xticks(IDEB_cidades_acima_media_anos_iniciais)

IDEB_acima_medias_ini.legend(loc='lower right', framealpha=1)
IDEB_acima_medias_ini.set_title('Índice de Desenvolvimento da Educação Básica')
IDEB_acima_medias_ini.set_xlabel('Nota no IDEB')

#   horizontal anos iniciais
#   abaixo ou igual a média
Cidades_abaixo_ou_igual_media_barras_ini_h, IDEB_abaixo_ou_igual_medias_ini = plt.subplots()

IDEB_abaixo_ou_igual_medias_ini.barh(nome_cidades_menor_ou_igual_media_iniciais,
                                     IDEB_cidades_menor_ou_igual_media_iniciais,
                                     label='Cidades abaixo da média do IDEB anos iniciais')

IDEB_abaixo_ou_igual_medias_ini.set_yticks(nome_cidades_menor_ou_igual_media_iniciais)
IDEB_abaixo_ou_igual_medias_ini.set_yticklabels(nome_cidades_menor_ou_igual_media_iniciais, fontsize=10)

IDEB_abaixo_ou_igual_medias_ini.axvline(media_IDEB_anos_iniciais, label='Média anos iniciais = 5.906', color='#DC143C',
                                        alpha=1)

IDEB_abaixo_ou_igual_medias_ini.set_xticks(IDEB_cidades_menor_ou_igual_media_iniciais)

IDEB_abaixo_ou_igual_medias_ini.legend(loc='lower right', framealpha=1)
IDEB_abaixo_ou_igual_medias_ini.set_title('Índice de Desenvolvimento da Educação Básica')
IDEB_abaixo_ou_igual_medias_ini.set_xlabel('Nota no IDEB')

#   horizontal anos finais
#   acima da média
Cidades_acima_media_barras_fin_h, IDEB_acima_medias_fin = plt.subplots()

IDEB_acima_medias_fin.barh(nome_cidades_acima_media_anos_finais,
                           IDEB_cidades_acima_media_anos_finais, label='Cidades acima da média do IDEB anos finais')

IDEB_acima_medias_fin.set_yticks(nome_cidades_acima_media_anos_finais)
IDEB_acima_medias_fin.set_yticklabels(nome_cidades_acima_media_anos_finais, fontsize=10)

IDEB_acima_medias_fin.axvline(media_IDEB_anos_finais, label='Média anos finais = 4.654', color='#DC143C', alpha=1)

IDEB_acima_medias_fin.set_xticks(IDEB_cidades_acima_media_anos_finais)

IDEB_acima_medias_fin.legend(loc='lower right', framealpha=1)
IDEB_acima_medias_fin.set_title('Índice de Desenvolvimento da Educação Básica')
IDEB_acima_medias_fin.set_xlabel('Nota no IDEB')

#   horizontal anos finais
#   abaixo ou igual a média
Cidades_abaixo_ou_igual_media_barras_fin_h, IDEB_abaixo_ou_igual_medias_fin = plt.subplots()

IDEB_abaixo_ou_igual_medias_fin.barh(nome_cidades_menor_ou_igual_media_finais,
                                     IDEB_cidades_menor_ou_igual_media_finais,
                                     label='Cidades abaixo da média do IDEB anos finais')

IDEB_abaixo_ou_igual_medias_fin.set_yticks(nome_cidades_menor_ou_igual_media_finais)
IDEB_abaixo_ou_igual_medias_fin.set_yticklabels(nome_cidades_menor_ou_igual_media_finais, fontsize=10)

IDEB_abaixo_ou_igual_medias_fin.axvline(media_IDEB_anos_finais, label='Média anos finais = 4.654', color='#DC143C',
                                        alpha=1)

IDEB_abaixo_ou_igual_medias_fin.set_xticks(IDEB_cidades_menor_ou_igual_media_finais)

IDEB_abaixo_ou_igual_medias_fin.legend(loc='lower right', framealpha=1)
IDEB_abaixo_ou_igual_medias_fin.set_title('Índice de Desenvolvimento da Educação Básica')
IDEB_abaixo_ou_igual_medias_fin.set_xlabel('Nota no IDEB')
#   gráficos de barras horizontais relacionando as cidades e as médias fim


#   parte de frequência inicio
#   anos iniciais
num_classes_ini = round(pow(df['V6'].count(), 1 / 2))
amplitude_ini = (df['V6'].max() - df['V6'].min())
amplitude_ini = float(amplitude_ini)
amplitude_classes_ini = round(amplitude_ini / num_classes_ini, 2)
classes_ini_float = [float(df['V6'].min() - 0.01)]

for n in range(1, num_classes_ini):
    valor_classe = classes_ini_float[n - 1] + amplitude_classes_ini
    classes_ini_float.append(round(valor_classe, 2))

classes_ini_float.append(float(df['V6'].max()))

classes_ini_string = []
for n in range(num_classes_ini):
    texto = str(classes_ini_float[n]) + ' -| ' + str(classes_ini_float[n + 1])
    classes_ini_string.append(texto)

#   calcula a Frequência absoluta
frequencia_absoluta_ini = []
contador = 0
for i in range(1, num_classes_ini + 1):
    n = 0
    while n <= int(df['V6'].count() - 1):
        if classes_ini_float[i - 1] < float(df['V6'][n]) <= classes_ini_float[i]:
            contador += 1
        n += 1
    frequencia_absoluta_ini.append(contador)
    contador = 0

#   cria o dataframe
dados_dataframe_ini = {'Classe': classes_ini_string, 'Frequência absoluta': frequencia_absoluta_ini}
df_frequencia_ini = pd.DataFrame(dados_dataframe_ini)

#   calcula a Frequência relativa
frequencia_relativa_ini = []
for n in range(int(df_frequencia_ini['Frequência absoluta'].count())):
    frequencia_relativa_ini.append(round((float(df_frequencia_ini['Frequência absoluta'][n])
                                          / float(df_frequencia_ini['Frequência absoluta'].sum())) * 100, 2))

#   add ao dataframe
df_frequencia_ini['Frequência relativa (%)'] = frequencia_relativa_ini

#   calcula a Frequência acumulada
frequencia_acumulada_ini = [frequencia_absoluta_ini[0]]

for n in range(1, int(df_frequencia_ini['Frequência absoluta'].count())):
    frequencia_acumulada_ini.append(frequencia_acumulada_ini[n - 1] + frequencia_absoluta_ini[n])

#   add ao dataframe
df_frequencia_ini['Frequência acumulada'] = frequencia_acumulada_ini

#   calcula a Frequência acumulada relativa
frequencia_acumulada_relativa_ini = []
for n in range(int(df_frequencia_ini['Frequência absoluta'].count())):
    frequencia_acumulada_relativa_ini.append(round((float(df_frequencia_ini['Frequência acumulada'][n])
                                                    / float(df_frequencia_ini['Frequência absoluta'].sum())) * 100, 2))

#   add ao dataframe
df_frequencia_ini['Frequência acumulada relativa (%)'] = frequencia_acumulada_relativa_ini

#   anos finais
num_classes_fin = round(pow(df['V7'].count(), 1 / 2))
amplitude_fin = (df['V7'].max() - df['V7'].min())
amplitude_fin = float(amplitude_fin)
amplitude_classes_fin = round(amplitude_fin / num_classes_fin, 2)
classes_fin_float = [float(df['V7'].min() - 0.01)]

for n in range(1, num_classes_fin):
    valor_classe = classes_fin_float[n - 1] + amplitude_classes_fin
    classes_fin_float.append(round(valor_classe, 2))

classes_fin_float.append(float(df['V7'].max()))

classes_fin_string = []
for n in range(num_classes_fin):
    texto = str(classes_fin_float[n]) + ' -| ' + str(classes_fin_float[n + 1])
    classes_fin_string.append(texto)

#   calcula a Frequência absoluta
frequencia_absoluta_fin = []
contador = 0
for i in range(1, num_classes_fin + 1):
    n = 0
    while n <= int(df['V7'].count() - 1):
        if classes_fin_float[i - 1] < float(df['V7'][n]) <= classes_fin_float[i]:
            contador += 1
        n += 1
    frequencia_absoluta_fin.append(contador)
    contador = 0

#   cria o dataframe
dados_dataframe_fin = {'Classe': classes_fin_string, 'Frequência absoluta': frequencia_absoluta_fin}
df_frequencia_fin = pd.DataFrame(dados_dataframe_fin)

#   calcula a Frequência relativa
frequencia_relativa_fin = []
for n in range(int(df_frequencia_fin['Frequência absoluta'].count())):
    frequencia_relativa_fin.append(round((float(df_frequencia_fin['Frequência absoluta'][n])
                                          / float(df_frequencia_fin['Frequência absoluta'].sum())) * 100, 2))

#   add ao dataframe
df_frequencia_fin['Frequência relativa (%)'] = frequencia_relativa_fin

#   calcula a Frequência acumulada
frequencia_acumulada_fin = [frequencia_absoluta_fin[0]]

for n in range(1, int(df_frequencia_fin['Frequência absoluta'].count())):
    frequencia_acumulada_fin.append(frequencia_acumulada_fin[n - 1] + frequencia_absoluta_fin[n])

#   add ao dataframe
df_frequencia_fin['Frequência acumulada'] = frequencia_acumulada_fin

#   calcula a Frequência acumulada relativa
frequencia_acumulada_relativa_fin = []
for n in range(int(df_frequencia_fin['Frequência absoluta'].count())):
    frequencia_acumulada_relativa_fin.append(round((float(df_frequencia_fin['Frequência acumulada'][n])
                                                    / float(df_frequencia_fin['Frequência absoluta'].sum())) * 100, 2))

#   add ao dataframe
df_frequencia_fin['Frequência acumulada relativa (%)'] = frequencia_acumulada_relativa_fin
#   parte de frequencia fim


#   histograma das frequencias inicio
#   anos iniciais
histograma_freq_ini, freq_ini = plt.subplots()

freq_ini.axvline(media_IDEB_anos_iniciais, label='Média anos iniciais = 5.90', color='#DC143C', alpha=1)
freq_ini.hist(df['V6'], bins=classes_ini_float, edgecolor='black', label='Cidades')

freq_ini.set_xticks(classes_ini_float)
#   usando o annotate
bin_centers_x = 0.5 * np.diff(classes_ini_float) + classes_ini_float[:-1]
for freq, x, n in zip(frequencia_absoluta_ini, bin_centers_x, range(len(frequencia_absoluta_ini))):
    # Label the raw counts
    freq_ini.annotate(str(freq), xy=(x, 0), xycoords=('data', 'axes fraction'),
                      textcoords='offset points', va='top', ha='center', xytext=(0, 36))

    # Label the percentages
    percent = '%0.0f%%' % frequencia_relativa_ini[n]
    freq_ini.annotate(str(percent), xy=(x, 0), xycoords=('data', 'axes fraction'),
                      textcoords='offset points', va='top', ha='center', xytext=(0, 18))

freq_ini.set_title('Frequência absoluta e relativa nos anos iniciais')
freq_ini.set_xlabel('Notas IDEB anos iniciais')
freq_ini.set_ylabel('Total de cidades')

freq_ini.legend()
#   anos finais
histograma_freq_fin, freq_fin = plt.subplots()

freq_fin.axvline(media_IDEB_anos_finais, label='Média anos finais = 4.65', color='#DC143C', alpha=1)
freq_fin.hist(df['V7'], bins=classes_fin_float, edgecolor='black', label='Cidades')

freq_fin.set_xticks(classes_fin_float)
#   usando o annotate
bin_centers_x = 0.5 * np.diff(classes_fin_float) + classes_fin_float[:-1]
for freq, x, n in zip(frequencia_absoluta_fin, bin_centers_x, range(len(frequencia_absoluta_fin))):
    # Label the raw counts
    freq_fin.annotate(str(freq), xy=(x, 0), xycoords=('data', 'axes fraction'),
                      textcoords='offset points', va='top', ha='center', xytext=(0, 36))

    # Label the percentages
    percent = '%0.0f%%' % frequencia_relativa_fin[n]
    freq_fin.annotate(str(percent), xy=(x, 0), xycoords=('data', 'axes fraction'),
                      textcoords='offset points', va='top', ha='center', xytext=(0, 18))

freq_fin.set_title('Frequência absoluta e relativa nos anos finais')
freq_fin.set_xlabel('Notas IDEB anos finais')
freq_fin.set_ylabel('Total de cidades')

freq_fin.legend()
#   histograma das frequências fim


#   box plot inicio
box_plot, box_plot_ini_fin = plt.subplots()

bplot = box_plot_ini_fin.boxplot([df['V6'], df['V7']], labels=['Anos iniciais', 'Anos finais'])

box_plot_ini_fin.set_ylim(3.5, 7)
box_plot_ini_fin.set_title('Boxplot do IDEB')
box_plot_ini_fin.set_ylabel('Nota no IDEB')
#   box plot fim


plt.tight_layout()
plt.show()
