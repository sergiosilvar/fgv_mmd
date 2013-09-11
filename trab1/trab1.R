# Perguntas
# 4) Quais são as 5 maiores cadeias de influências (ex: A --> B --> C --> ...)?
# 5) Quais são os países que geraram os maiores influentes?
# 6) Quais são as áreas dos maiores influentes?

data = read.csv("p01_Influences.csv")


# 1) Quais são as 10 maiores personalidades, em termos de poder de gerar influências?
sort(table(data$influence),decreasing=T)[1:10]

# 2) Quais são as 10 personalidades que mais sofreram influências (maior número de influenciadores)?
sort(table(data$influenced),decreasing=T)[1:10]

# 3) Quais são os 5 maiores "clusters" de personalidades que foram influenciados por um grupo semelhante de influentes?