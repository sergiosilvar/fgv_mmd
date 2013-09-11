# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import networkx as nx
import pylab
import os
import codecs

def pasta():
	return os.path.dirname(os.path.abspath(__file__)) +'/'

def salvar(g,nome_arquivo):
	nx.draw(g)
	path = pasta()+nome_arquivo
	pylab.savefig(path)
	return path
	
arquivo = open(pasta()+'pred.txt', 'r')
for linha in arquivo:
	print linha.split(';')

arquivo.close()