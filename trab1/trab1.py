# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# 1) Quais são as 10 maiores personalidades, em termos de poder de gerar influências?
# 
# 2) Quais são as 10 personalidades que mais sofreram influências (maior número de influenciadores)?
# 
# 3) Quais são os 5 maiores "clusters" de personalidades que foram influenciados por um grupo semelhante de influentes?
# 
# 4) Quais são as 5 maiores cadeias de influências (ex: A --> B --> C --> ...)?
# 
# 5) Quais são os países que geraram os maiores influentes?
# 
# 6) Quais são as áreas dos maiores influentes?

# <codecell>

import numpy as np
from collections import Counter
from scipy.cluster.vq import kmeans
import networkx as nx

# <markdowncell>

# O arquivo original foi modificado:
#     
# 1. Nome das colunas alterados.  
# 1. Aspas removidas.  
# 1. Removido o espaço ao final na segunda coluna.

# <codecell>

# Carregar arquivo.
dataset = np.genfromtxt('p01_Influences_cleaned.csv', dtype=None, names=True, delimiter=';')
#dataset = np.genfromtxt('p01_Influences.csv', dtype=None, names=True, delimiter=',',usecols=(1,2))

# <markdowncell>

# #### Quais são as 10 maiores personalidades, em termos de poder de gerar influências?
# R: Contar os 10 nomes que mais repetem na coluna "influences".

# <codecell>

Counter(dataset['influences']).most_common()[0:10]

# <markdowncell>

# #### Quais são as 10 personalidades que mais sofreram influências (maior número de influenciadores)?

# <codecell>

Counter(dataset['influenced']).most_common()[0:10]

# <markdowncell>

# #### Quais são os 5 maiores "clusters" de personalidades que foram influenciados por um grupo semelhante de influentes?

# <markdowncell>

# Sobre tipos de variáveis: https://statistics.laerd.com/statistical-guides/types-of-variable.php
#         
# Cluster Analysis: http://www.bus.utk.edu/stat/Stat579/Introduction%20to%20Cluster%20Analysis.pdf

# <markdowncell>

# ##### Abordagem Matriz e K-means.

# <codecell>

''' Montar matriz de similaridade onde as linhas identificam uma pessoa 
e as colunas identificam quem a influenciou.'''
# Função para retornar o índice de uma pessoa no vetor pessoa.
def index(s) : return np.where(pessoas==s)[0][0]

pessoas = union1d(unique(dataset['influenced']), unique(dataset['influences']))
n = len(pessoas)
influencia = zeros((n,n),dtype=int)
for influenciador, influenciado in dataset:
    i = index(influenciado)
    j = index(influenciador)
    influencia[i,j] = 1

# Executa o algoritmo k-means para alguns k arbitrários.
codebook5 = kmeans(influencia,5)

# Quem são essas pessoas? O centro dos centróides?
codebook = codebook5
for i in range(len(codebook[0])):
    a = codebook[0][i]==1
    if len(pessoas[a])>0:
        print pessoas[a][0]
    
    

# <markdowncell>

# ##### Abordagem por Grafo

# <codecell>

# Abordagem por Grafo.
g = nx.DiGraph()
g.add_edges_from(dataset)

# <codecell>

outdegrees = {}
for node in g.nodes():
    degree = g.out_degree(node)
    if not outdegrees.has_key(degree):
        outdegrees[degree] = []
    outdegrees[degree].append(node)

# <codecell>

sort(outdegrees)

