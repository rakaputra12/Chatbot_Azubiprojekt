from newspaper import article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')


from newspaper.source import Article
#Get Datenbank
article = Article('https://de.wikipedia.org/wiki/Andrew_Tate')
article.download()
article.parse()
article.nlp()
corpus = article.text

print(corpus)

text = corpus
sentence_list = nltk.sent_tokenize(text)

print(sentence_list)