import gensim
import os
import nltk.data
import string
import itertools

model = gensim.models.Word2Vec.load('C:/Users/kenny.ksn/Desktop/vocabularynovo.model')

with open('PATH/Texto.txt', 'r', encoding = 'utf-8-sig') as file:
      data = file.read().lower()
      data = data.split('\n')
      data = [x for x in data if x] 

lista = []
lista2 = []

for item in data:
   ff = item.split()
   lista.append(ff)

print(lista)
for item in lista:
    combinations = itertools.combinations(item, 2)
    for a, b in combinations:
      valor = model.similarity(a,b)
      print(valor, a, b)
      if valor < 0.2:
         lista2.append(a)
         lista2.append(b)
      
print(lista2)
