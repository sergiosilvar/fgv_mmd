# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# performance: http://stackoverflow.com/questions/14259685/python-querying-wikipedia-performance
# wikitools:  http://stackoverflow.com/questions/15371505/parsing-wikipedia-stubs-using-python-wikitools
# howto: http://stackoverflow.com/questions/11471684/query-wikipedia-data-page
# exemplo http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=xml&titles=Friedrich_Nietzsche
# exemplo só com infobox: http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=xml&titles=Friedrich_Nietzsche&rvsection=0
import urllib
import urllib2
import simplejson 

# Consulta o wiki para uma única pessoa, em modo texto.
def __consulta_wiki(nome):
    url = 'http://en.wikipedia.org/w/api.php'
    values = {'action' : 'query',
        'prop' : 'revisions',
        'rvprop' : 'content',          
        'format' : 'txt',
        'titles' : nome,
        'rvsection':0}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    return response.read()
    
 
# Recupera as propriedades dentro de um texto de uma única pessoa.
def __propriedades(stream):
    token = 'Infobox '
    i = stream.find(token)+len(token)
    j = stream.find('\n',i)
    profissao = stream[i:j]
    return profissao    


# Recupera as propriedades para uma lista de nomes.    
def consulta_nomes(nomes):
    # Função auxiliar para aplicar no método map.Recuperar as propriedades de uma única pessoa.
    def map_prop(nome):
        return [nome,__propriedades(__consulta_wiki(nome))]

    return map(map_prop, nomes)

# <codecell>


nomes = ['Ferdinand de Saussure','Jacques Lacan','Georg Wilhelm Friedrich Hegel','Jacques Lacan']
#nome = 'Ferdinand de Saussure'
print consulta_nomes(nomes)
#json = simplejson.loads(stream)

