'''Importação das bibliotecas'''
import string
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

class Pandas_to_NLP():
    def __init__(self, df, coluna, idioma):
        self.df = df
        self.coluna = coluna
        self.idioma = idioma

    def remove_pontuacao(self, review: str) -> str:
        '''Esta função remove a pontuação do texto e retorna o texto'''

        '''Identifica se o caracter é uma pontuação, caso seja é removido do texto'''
        review = "".join([char for char in review if char not in string.punctuation])

        return review

    def lematiza(self, review: str) -> str:
        '''Esta função lematiza a string'''

        porter = PorterStemmer()
        stemmed = [porter.stem(word) for word in review]
        return stemmed

    def tokeniza(self, review: str) -> list:
        '''Tokeniza os Reviews'''

        '''Esta função tokeniza a string contendo a análise'''
        tokens = word_tokenize(review)

        return tokens

    def remove_stopwords(self, texto: list) -> list:
        '''Esta função remove as stopwords'''

        '''Cria um vetor para armazenar o texto filtrado'''
        texto_filtrado = []

        '''Recebe a lista de stopwords em portugues'''
        stopWords = set(stopwords.words(self.idioma))

        '''Remove as spotwords em cada palavra'''
        for palavra in texto:
            if palavra not in stopWords:
                texto_filtrado.append(palavra)

        return texto_filtrado

    def padroniza_palavras(self, lista_de_palavras: list) -> list:
        '''Padroniza as palavras'''

        '''Cria uma lista para armazenar as palavras padronizadas'''
        lista_de_palavras_padronizada = []

        '''Transforma as palavras em minúsculas'''
        for palavra in lista_de_palavras:
            lista_de_palavras_padronizada.append(palavra.lower())

        return lista_de_palavras_padronizada

    def identifica_tamanho(self, lista_de_palavras: list) -> int:
        '''Esta função identifica o tamanho da análise'''

        return len(lista_de_palavras)

    def main(self) -> pd.DataFrame:
        '''Função principal que chama as outras funções em sequência e retorna o dataframe'''

        '''Remove a pontuação das frases'''
        self.df[self.coluna] = self.df[self.coluna].apply(lambda x: self.remove_pontuacao(x))

        '''Tokeniza os reviews'''
        self.df[self.coluna] = self.df[self.coluna].apply(lambda x: self.tokeniza(x))

        '''Padroniza as palavras'''
        self.df[self.coluna] = self.df[self.coluna].apply(lambda x: self.padroniza_palavras(x))

        '''Remove as stopwords'''
        self.df[self.coluna] = self.df[self.coluna].apply(lambda x: self.remove_stopwords(x))

        '''Lematiza as frases'''
        self.df[self.coluna] = self.df[self.coluna].apply(lambda x: self.lematiza(x))

        '''Identifica o tamanho dos reviews'''
        self.df['tamanho_review'] = self.df[self.coluna].apply(lambda x: self.identifica_tamanho(x))

        '''Retorna o dataframe'''
        return self.df