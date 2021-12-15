import Pandas_to_NLP
import pandas as pd
import numpy as np

'''Importa o dataframe inicial'''
df_inicial = pd.read_csv('review_e_comentarios.csv', sep=';', encoding='UTF-8')

'''Pré-tratamento de dados'''

'''Define a coluna que será analisada e que contem os comentários'''
coluna = 'others'

'''Preenche os dados nulos com 'Não preenchido' '''
df_inicial.fillna('Não preenchido', inplace=True)

'''Cria um dataframe filtrado sem nenhum caso de não preenchimento na coluna escolhida'''
df_filtrado = df_inicial[df_inicial[coluna] != "Não preenchido"]

'''Reseta o índice'''
df_filtrado.index = np.arange(len(df_filtrado))

'''Define o idioma da análise'''
idioma = 'portuguese'

'''Atualiza o dataframe filtrado com o novo dataframe'''
df_filtrado = Pandas_to_NLP.Pandas_to_NLP(df_filtrado.copy(), coluna, idioma).main().copy()

'''Imprime as colunas que foram criadas'''
print(df_filtrado.tail())