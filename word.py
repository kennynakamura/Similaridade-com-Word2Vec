import gensim
import os
import nltk.data
import string
from nltk.corpus import stopwords
import itertools
nltk.download('stopwords')

model = gensim.models.Word2Vec.load('C:/Users/kenny.ksn/Desktop/vocabularynovo.model')

with open('C:/Users/kenny.ksn/Desktop/Word2Vec/Texto4.txt', 'r', encoding = 'utf-8-sig') as file:
      data = file.read().lower()
      data = data.split('\n')
      data = [x for x in data if x] 

lista = []
lista2 = []
lista3 = []
for item in data:
   ff = item.split()
   lista.append(ff)
'''
for item in lista:
   filtered_words = [word for word in item if word not in stopwords.words('portuguese')]
   lista2.append(filtered_words)

print(lista2)
'''

print(lista)
for item in lista:
    combinations = itertools.combinations(item, 2)
    for a, b in combinations:
      valor = model.similarity(a,b)
      print(valor, a, b)
      if valor < 0.2:
         lista3.append(a)
         lista3.append(b)
      
print(lista3)