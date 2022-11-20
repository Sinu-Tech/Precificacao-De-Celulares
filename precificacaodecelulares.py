# -*- coding: utf-8 -*-
"""PrecificacaoDeCelulares.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/Sinu-Tech/Precificacao-De-Celulares/blob/main/PrecificacaoDeCelulares.ipynb
"""

import pandas as pd
import os
import plotly.express as px
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import matplotlib.pyplot as plt

url_train = 'https://raw.githubusercontent.com/Sinu-Tech/Precificacao-De-Celulares/main/train.csv'
base_treino = pd.read_csv(url_train)

url_test = 'https://raw.githubusercontent.com/Sinu-Tech/Precificacao-De-Celulares/main/test.csv'
base_teste = pd.read_csv(url_test)

base_treino.describe()

base_treino.isnull().sum()

grafico = px.box(base_treino, y='battery_power')
grafico.show()

grafico = px.box(base_treino, y='clock_speed')
grafico.show()

grafico = px.box(base_treino, y='fc')
grafico.show()

grafico = px.box(base_treino, y='int_memory')
grafico.show()

grafico = px.box(base_treino, y='mobile_wt')
grafico.show()

grafico = px.box(base_treino, y='n_cores')
grafico.show()

grafico = px.box(base_treino, y='pc')
grafico.show()

grafico = px.box(base_treino, y='px_height')
grafico.show()

grafico = px.box(base_treino, y='px_width')
grafico.show()

grafico = px.box(base_treino, y='ram')
grafico.show()

grafico = px.box(base_treino, y='sc_h')
grafico.show()

grafico = px.box(base_treino, y='sc_w')
grafico.show()

grafico = px.box(base_treino, y='talk_time')
grafico.show()

grafico = px.box(base_treino, y='price_range')
grafico.show()

base_teste.drop(["id"], axis=1)

atributos = base_treino.iloc[:, :20]
print(atributos)

classes = base_treino.loc[:, ['price_range']]
print(classes)

def qt():
  qt = preprocessing.QuantileTransformer() 
  atributos_normalizados = qt.fit_transform(atributos)
  return  atributos_normalizados

def mas():
  mas = preprocessing.MaxAbsScaler()
  atributos_normalizados = mas.fit_transform(atributos)
  return  atributos_normalizados

def nm():
  nm = preprocessing.Normalizer()
  atributos_normalizados = nm.fit_transform(atributos)  
  return  atributos_normalizados

def ss():
  ss = preprocessing.StandardScaler()
  atributos_normalizados = ss.fit_transform(atributos)
  return  atributos_normalizados

def mms():
  mms = preprocessing.MinMaxScaler()
  atributos_normalizados = mms.fit_transform(atributos)
  return  atributos_normalizados

atributos_normalizados = mms()

"""Ericles"""

def decision_tree_classifier():

  modelo = DecisionTreeClassifier()
  modelo.fit(atributos_normalizados, classes)

  print(f'Acurácia: {modelo.score(atributos_normalizados, classes)*100}')

  pred = modelo.predict(atributos)

  print(f'Esperado: {classes}, resultado: {pred}')

def dtc(atributos_normalizados):
  modelo = DecisionTreeClassifier()
  modelo.fit(atributos_normalizados, classes)
  return modelo.score(atributos_normalizados, classes)*100

"""Joanne"""

def perceptron():

  modelo = Perceptron()
  modelo.fit(atributos_normalizados, classes)

  print(f'Acurácia: {modelo.score(atributos_normalizados, classes)*100}')

  pred = modelo.predict(atributos)

  print(f'Esperado: {classes}, resultado: {pred}')

def per(atributos_normalizados):
  modelo = Perceptron()
  modelo.fit(atributos_normalizados, classes)
  return modelo.score(atributos_normalizados, classes)*100

"""Milena"""

def naive_bayes():

  modelo = GaussianNB()
  modelo.fit(atributos_normalizados, classes)

  print(f'Acurácia: {modelo.score(atributos_normalizados, classes)*100}')

  pred = modelo.predict(atributos)

  print(f'Esperado: {classes}, resultado: {pred}')

def nai(atributos_normalizados):
  modelo = GaussianNB()
  modelo.fit(atributos_normalizados, classes)
  return modelo.score(atributos_normalizados, classes)*100

"""Kendy"""

def k_neighbors_classifier():

  modelo = KNeighborsClassifier(n_neighbors=3)
  modelo.fit(atributos_normalizados, classes)

  print(f'Acurácia: {modelo.score(atributos_normalizados, classes)*100}')

  pred = modelo.predict(atributos)

  print(f'Esperado: {classes}, resultado: {pred}')

def knn(atributos_normalizados):
  modelo = KNeighborsClassifier()
  modelo.fit(atributos_normalizados, classes)
  return modelo.score(atributos_normalizados, classes)*100

"""Thiago"""

def svc():

  modelo = SVC()
  modelo.fit(atributos_normalizados, classes)

  print(f'Acurácia: {modelo.score(atributos_normalizados, classes)*100}')

  pred = modelo.predict(atributos)

  print(f'Esperado: {classes}, resultado: {pred}')

def svm(atributos_normalizados):
  modelo = SVC()
  modelo.fit(atributos_normalizados, classes)
  return modelo.score(atributos_normalizados, classes)*100

"""Menu"""

def linha(tamanho=42):
    return '-' * tamanho


def cabecalho(menu):
    print(linha())
    print(menu.center(42))
    print(linha())


def algoritmos():
    print("1 - Árvore de decisão")
    print("2 - KNN")
    print("3 - Naive Bayes")
    print("4 - Perceptron")
    print("5 - SVC")
    print("6 - Comparar acurácia de todos os algoritmos")
    print("0 - Sair")


def opcoes():
    op = '1' 
    while op!='0':
      os.system('cls')
      algoritmos();
      op = input("Digite o respectivo número referente ao algoritmo: ")
      if op=='1':
        decision_tree_classifier()
      elif op=='2':
        k_neighbors_classifier()
      elif op=='3':
        naive_bayes()
      elif op=='4':
        perceptron()
      elif op=='5':
        svc()
      elif op=='6':
        comparar_resultados()
      elif op!='0':
        print('Opção inválida')
      input("Digite qualquer tecla para continuar: ")

"""Menu(FALTA IMPLEMENTAR A OPÇÃO DE COMPARAR OS RESULTADOS)"""

cabecalho("ALGORITMOS DE CLASSIFICAÇÃO");
opcoes();

"""Comparações"""

def comparar_resultados():
  resultados = {}

  resultados['DecisionTreeClassifier-QuantileTransformer'] = dtc(qt())
  resultados['Perceptron-QuantileTransformer'] = per(qt())
  resultados['NaiveBayes-QuantileTransformer'] = nai(qt())
  resultados['KNeighborsClassifier-QuantileTransformer'] = knn(qt())
  resultados['SupportVectorMachine-QuantileTransformer'] = svm(qt())

  resultados['DecisionTreeClassifier-MaxAbsScaler'] = dtc(mas())
  resultados['Perceptron-MaxAbsScaler'] = per(mas())
  resultados['NaiveBayes-MaxAbsScaler'] = nai(mas())
  resultados['KNeighborsClassifier-MaxAbsScaler'] = knn(mas())
  resultados['SupportVectorMachine-MaxAbsScaler'] = svm(mas())

  resultados['DecisionTreeClassifier-Normalizer'] = dtc(nm())
  resultados['Perceptron-Normalizer'] = per(nm())
  resultados['NaiveBayes-Normalizer'] = nai(nm())
  resultados['KNeighborsClassifier-Normalizer'] = knn(nm())
  resultados['SupportVectorMachine-Normalizer'] = svm(nm())

  resultados['DecisionTreeClassifier-StandardScaler'] = dtc(ss())
  resultados['Perceptron-StandardScaler'] = per(ss())
  resultados['NaiveBayes-StandardScaler'] = nai(ss())
  resultados['KNeighborsClassifier-StandardScaler'] = knn(ss())
  resultados['SupportVectorMachine-StandardScaler'] = svm(ss())

  resultados['DecisionTreeClassifier-MinMaxScaler'] = dtc(mms())
  resultados['Perceptron-MinMaxScaler'] = per(mms())
  resultados['NaiveBayes-MinMaxScaler'] = nai(mms())
  resultados['KNeighborsClassifier-MinMaxScaler'] = knn(mms())
  resultados['SupportVectorMachine-MinMaxScaler'] = svm(mms())


  resultados = sorted(resultados.items(), key=lambda x:x[1])
  resultados = dict(resultados)

  algoritmos = list(resultados.keys())
  acuracias = list(resultados.values())

  fig, ax = plt.subplots(figsize=(35,20), sharey=True)

  bars = ax.barh(algoritmos, acuracias)
  ax.set_title('Taxa de acurácia dos algoritmos testados', fontsize=35)

  acuracias_graph = []
  for acuracia in acuracias:
    acuracia = round(acuracia,2)
    acuracias_graph.append(acuracia)

  for i, v in enumerate(acuracias_graph):
    if v == 100:
      cor = 'green'
    elif v >= 70:
      cor = 'blue'
    elif v >= 50:
      cor = 'maroon'
    else:
      cor = 'red'

  ax.text(v + 1, i - 0.25 , str(v)+'%', color=cor, fontweight='bold', fontsize=16)

"""Teste para IphoneX e LG L3"""

iphoneX = [{'baterry_power': 2716, 'blue':1, 'clock_speed': 2.4, 'dual_sim': 0, 'fc': 12,'four_g': 1, 'int_memory':256, 'm_dep': 0.8, 'mobile_wt': 174, 'n_cores': 3, 'pc': 12, 'px_height': 2436, 'px_width': 1125, 'ram': 3064, 'sc_h': 14, 'sc_w': 7, 'talk_time': 21, 'three_g': 1, 'touch_screen': 1, 'wifi': 1}]
iphoneX = pd.DataFrame(iphoneX)
iphoneXClasse = [3]

modelo = DecisionTreeClassifier(max_depth = 5)
modelo.fit(atributos_normalizados, classes)

pred = modelo.predict(iphoneX)

print(f'esperado: {iphoneXClasse}, resultado: {pred}')

"""Mostra a porcentagem de acertos"""

accuracy_score(pred, iphoneXClasse)*100

lgL3 = [{'baterry_power': 1500, 'blue':1, 'clock_speed': 0.8, 'dual_sim': 0, 'fc': 0,'four_g': 0, 'int_memory':2, 'm_dep': 1.2, 'mobile_wt': 110, 'n_cores': 1, 'pc': 3, 'px_height':320, 'px_width':240, 'ram': 384, 'sc_h': 10, 'sc_w': 6, 'talk_time': 10, 'three_g': 1, 'touch_screen': 1, 'wifi': 1}]
lgL3 = pd.DataFrame(lgL3)
lgL3Classe = [1]

modelo = SVC()
modelo.fit(atributos_normalizados, classes)

pred = modelo.predict(lgL3)

print(f'esperado: {lgL3Classe}, resultado: {pred}')

"""Mostra a porcentagem de acertos"""

accuracy_score(pred, lgL3Classe)*100

"""FIGURA"""

from sklearn import tree
tree.plot_tree(modelo,feature_names = atributos.columns, 
               class_names=['0','1','2','3'],
               filled = True);