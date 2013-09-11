# Este método foi DEPRECIADO pois trabalhar com matrizes neste tamanho leva 4 minutos.
# Deixei-o aqui somente como histórico.
def monta_matrizes_influencias(dataset, l_pessoas):
    # INICIALIZAÇÃO DE MATRIZES.
    n = len(l_pessoas)
    l_influenciados, l_influencias = monta_listas_adj_influencias(dataset)
    
    # # Matriz onde elemento 'a_ij' é uma lista de índices de inflenciados em comum por pessoas 'i' e 'j'.\n",
    m_influenciados_comum = np.empty((n,3),dtype=object)
    for i in range(n):
        for j in range(i,n):
                m_influenciados_comum[i][j] = []
                m_influenciados_comum[j][i] = []

    
    # Matriz onde elemento 'a_ij' é uma lista de índices de influencias em comum das pessoas 'i' e 'j'.
    m_influencias_comum = np.empty((n,n),dtype=object)
    for i in range(n):
        for j in range(i,n):
                m_influencias_comum[i][j] = []
                m_influencias_comum[j][i] = []

    
    # Matriz onde elemento 'a_ij' é a quantidade de influenciados em comum por pessoas 'i' e 'j'.
    m_qtd_influenciados_comum = np.zeros((n,n),dtype=int)
    
    # Matriz onde elemento 'a_ij' é a quantidade de influências em comum das pessoas 'i' e 'j'.
    m_qtd_influencias_comum = np.zeros((n,n),dtype=int)
    
    # CONSTRUÇÃO DAS MATRIZES.
    for i in range(n):

        # Indicador de progresso.
        # FIXME: Ao refatorar o código para usar simetria no loop abaixo, não dá tempo de ler.
        #prog = int((float(i)/n)*100)
        #if prog%10==0:  
         #   s = "Progresso: %d%% " % prog
         #   pt = prog%10 + 1
         #   s = s + ('.' * pt)
         #   IPython.core.display.clear_output()
         #   IPython.core.display.display_html("Progresso: " + s  )

        
        l_influenciados_i = l_influenciados[i]
        l_influencias_i = l_influencias[i]

        for j in range(i+1,n): # As matrizes são simétricas.
            if i!=j: 
                l_influenciados_j = l_influenciados[j]
                l_influencias_j = l_influencias[j]
                
                m_influenciados_comum[i,j] = intersec(l_influenciados_i,l_influenciados_j)
                m_qtd_influenciados_comum[i,j] = len(m_influenciados_comum[i,j])            
                m_influenciados_comum[j,i] = m_influenciados_comum[i,j]
                m_qtd_influenciados_comum[j,i] = m_qtd_influenciados_comum[i,j]
                
                m_influencias_comum[i,j] = intersec(l_influencias_i,l_influencias_j)
                m_qtd_influencias_comum[i,j] = len(m_influencias_comum[i,j])
                m_influencias_comum[j,i] = m_influencias_comum[i,j]
                m_qtd_influencias_comum[j,i] = m_qtd_influencias_comum[i,j]
                
    return m_influenciados_comum,m_influencias_comum,m_qtd_influenciados_comum,m_qtd_influencias_comum
                
# DEPRECIADO
# Opções para montar, salvar e carregar matrizes.
# Se primeira vez que roda o notebook, deve-se pelo menos montar as matrizes.
# Opcionalmente, pode-se salvar para evitar processo de montagem em uma nova execução.
# Em meu notebook os tempos de montar, salvar e carregar são próximos. A complexidade é O(n^2).

montar_matrizes = False
salvar_matrizes = False
carregar_matrizes = False

if montar_matrizes:
    # Executar montagem das matrizes. Leva alguns minutos.
    t1 = dt.datetime.now()
    m_influenciados_comum,m_influencias_comum, \
        m_qtd_influenciados_comum,m_qtd_influencias_comum \
        = monta_matrizes_influencias(dataset, pessoas)
    t2 = dt.datetime.now()
    delta = t2 - t1
    print 'Montar matrizes terminado em %.2f min(s).' %(delta.seconds/60.0)
    # Tempo em meu notebook: 3.65 min.
    
if salvar_matrizes :
    t1 = dt.datetime.now()
    np.save('m_influenciados_comum.npy', m_influenciados_comum)
    np.save('m_influencias_comum.npy', m_influencias_comum)
    np.savetxt('m_qtd_influenciados_comum.txt', m_qtd_influenciados_comum, delimiter=';', fmt='%d')
    np.savetxt('m_qtd_influencias_comum.txt', m_qtd_influencias_comum, delimiter=';', fmt='%d')
    t2 = dt.datetime.now()
    delta = t2 - t1
    print 'Salvar matrizes terminado em %.2f min(s).' %(delta.seconds/60.0)
    # Tempo em meu notebook: 3.67 min.
    
if carregar_matrizes:
    t1 = dt.datetime.now()
    m_influenciados_comum = np.load('m_influenciados_comum.npy')
    m_influencias_comum = np.load('m_influencias_comum.npy')
    m_qtd_influenciados_comum = np.loadtxt('m_qtd_influenciados_comum.txt', delimiter=';', dtype=int)
    m_qtd_influencias_comum = np.loadtxt('m_qtd_influencias_comum.txt', delimiter=';', dtype=int)
    t2 = dt.datetime.now()
    delta = t2 - t1
    print 'Carregar matrizes terminado em %.2f min(s).' %(delta.seconds/60.0)
    # Tempo em meu notebook: 3.48 min.