# Pandas_to_NLP
O objetivo deste código é permitir que você realize uma análise de NLP com facilidade a partir de um Dataframe Pandas.

## O que o código faz?
Remove pontuação, lematiza, tokeniza, remove stopwords, padroniza palavras e indentifica o tamanho de cada review em uma coluna de comentários.<br/>

## Retorno da Classe Pandas_to_NLP
![Retorno](https://user-images.githubusercontent.com/25333881/146276009-3b0bdb83-4716-47b7-a7f3-d545f8e1a2ad.png)

## Como rodar o programa?
Passo 1 - Instale os pacotes requiridos através do pip<br/>
Passo 2 - Colocar o arquivo Pandas_to_NLP.py na mesma pasta de seu código e importar a classe Pandas_to_NLP<br/>
Passo 3 - Indicar na variável 'coluna' a coluna do Dataframe que contem os comentários<br/>
Passo 4 - Indicar na variável 'idioma' o idioma da análise<br/>
Passo 5 - Chamar a classe passando os parâmetros iniciais<br/>
Passo 6 - Esperar alguns segundos e pronto! Você recebe o Dataframe novo já com as colunas dos comentários tratada e também uma coluna contendo o tamanho de cada comentário'<br/>

Obs: Verifique o Exemplo_1.py na pasta Exemplos para verificar como utilizar corretamente o código.<br/>

## Limitações do Programa
O arquivo deve ser importado pela biblioteca Pandas e ser do tipo Dataframe.

## Pacotes Requeridos
- python 3
- pandas
- numpy
- string
- nltk.corpus - stopwords
- nltk.stem.porter - PorterStemmer
- nltk.tokenize - word_tokenize
