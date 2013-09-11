setwd('C:/Users/hp/Dropbox/Mestrado/Modelagem e Mineracao de Dados/Trabalho 1')

require(igraph); require(plyr)

dados<-read.csv(file="p01_Influences.csv",stringsAsFactors=F)

# 10 maiores ...
sort(table(dados$Influnces))

# 10 maiores ...
sort(table(dados$Influenced))

# Quem Nietzsche influênciou
dados[which(dados[,1] == 'Friedrich Nietzsche'),]

# Quem influênciou Nietzsche
dados[which(dados[,2] == 'Friedrich Nietzsche'),]

all_people<-union(dados$Influnces, dados$Influenced) # União de todo mundo
all_people_inter<-intersect(dados$Influnces, dados$Influenced) # Pessoas que influenciaram e foram influenciadas

influnces_not_influenced<- setdiff(dados$Influnces,dados$Influenced) # Quem influenciou mas não conta como influenciado
influenced_not_influnces<- setdiff(dados$Influenced,dados$Influnces) # Quem foi influenciado mas não influenciou ninguém

matrix_adjacencias<-table(dados$Influnces, dados$Influenced)

########### TENTATIVA DE FAZER UM GRAFO ###########

# Adicionado todo mundo para poder ter uma matriz de adjacencias
fake_node<-data.frame(Influnces=all_people, Influenced=all_people)
dados_stacked<-rbind(dados, fake_node)


# Criando uma matriz de adjacências
# Cada linha é a influência, e a coluna quem foi influenciado
matrix_adjacencias_stacked<-table(dados_stacked$Influnces, dados_stacked$Influenced)

# Grafo. Não funciona direito. Muito grande.
grafo<-graph.adjacency(matrix_adjacencias_stacked, diag=F)

########### FIM ###########

# Análise do ponto de vista de quem influenciou, vou descobrir quem foi influenciado pelas mesmas pessoas

get_lista_adjacencias<-function(vetor_nomeado)
{
	indice_nomes<-which(vetor_nomeado == 1)
	return(names(vetor_nomeado)[indice_nomes])
}

get_lista<-function(matrix_adjacencias)
{
	return(apply(matrix_adjacencias, 1, get_lista_adjacencias))
}

Lista_adj<-get_lista(matrix_adjacencias)

get_vetor_comum<-function(vetor, lista_adjacencias)
{
	return(data.frame(lapply(lista_adjacencias, function(x)sum(x%in%vetor))))
}

get_vetor_comum(matrix_adjacencias[438,], Lista_adj)

get_matrix_comum<-function(matrix_adjacencias)
{
	lista_adjacencias<-get_lista(matrix_adjacencias)
	
	return(ldply(lista_adjacencias, function(x)get_vetor_comum(x, lista_adjacencias)))
}

get_matrix_comum(matrix_adjacencias)->teste

kmean<-kmeans(teste, 20)

kmean$cluster[kmean$cluster==3]