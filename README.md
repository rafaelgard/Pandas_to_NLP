# Pandas_to_NLP
O objetivo deste repositório é permitir que você realize uma análise de NLP com facilidade

## Retorno da Classe Pandas_to_NLP
![Retorno](![Screenshot_6](https://user-images.githubusercontent.com/25333881/146276009-3b0bdb83-4716-47b7-a7f3-d545f8e1a2ad.png))

## Como rodar o programa?
Passo 1 - Instale os pacotes requiridos através do pip<br/>
Passo 2 - Indicar na variável 'coluna' a coluna do Dataframe que contem os comentários<br/>
Passo 3 - Indicar na variável 'idioma' o idioma da análise<br/>
Passo 4 - Chamar a classe passando os parâmetros'<br/>
Passo 5 - Esperar alguns segundos e pronto! Você recebe o Dataframe novo já com as colunas dos comentários tratada e também uma coluna contendo o tamanho de cada comentário'<br/>

## Limitações do Programa
O arquivo deve ser importado pela biblioteca Pandas.

## Pacotes Requeridos
- python 3
- pandas
- numpy
- string
- nltk.corpus - stopwords
- nltk.stem.porter - PorterStemmer
- nltk.tokenize - word_tokenize
