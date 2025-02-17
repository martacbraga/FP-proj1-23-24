'''
FP: 1o projeto
Curso: LEIC-A 
Aluno: ist1110034 - Marta Costa Braga

Objetivo: Conjunto de funções que premitem obter algumas informações sobre o estado
de um território retangular formado por caminhos verticais e horizontais. 
As interseções dos caminhos de um território podem ou não ser ocupadas por montanhas
e formar cadeias de montanhas e vales.
'''

def eh_territorio(arg):
    '''Verifica se o argumento recebido é um teritório. 
    Um território válido é um tuplo de tuplos em que cada tuplo representa um caminho vertical.
    Cada caminho vertical corresponde a uma letra de 'A' até 'Z' e o tamanho do caminho
    não deve exceder os 99. Dentro de cada caminho só poderão existir 0s ou 1s
    que correspondem a espaços livres ou a montanhas, respetivamente. 
       
    Parâmetros:
        arg (universal)
    Retorna: 
        booleano
    '''

    #pelo menos 1 caminho vertical entre A e Z e pelo menos um horizontal e não mais que 99
    if not (type(arg) == tuple and 0 < len(arg) <= 26 and 
            type(arg[0]) == tuple and 0 < len(arg[0]) <= 99):
        return False

    for i in range(len(arg)): 
        #todos os caminhos têm o mesmo tamanho
        if not (type(arg[i]) == tuple and len(arg[i]) == len(arg[0])):
            return False
        
        for j in range(len(arg[0])):
            #so existem ou espaços livres ou montanhas (0 ou 1)
            if not (type(arg[i][j]) == int and (arg[i][j] == 0 or arg[i][j] == 1)):
                return False
                 
    return True

def obtem_ultima_intersecao(t):
    '''Retorna a interseção do extremo superior direito do território.

    Parâmetros:
        t (territorio)
    Retorna:
        intersecao
    '''

    return (chr(len(t) + 64), len(t[0]))

def eh_intersecao(arg):
    '''Verifica se o argumento é um tuplo válido do tipo ('letra', 'numero'), 
    em que 'letra' é uma unica letra maiúscula entre A e Z e 'numero' é um inteiro entre 1 e 99. 

    Parâmetro:
        arg (universal)
    Retorna:
        boolenao
    '''

    #verifica que o tuplo é do tipo ('letra', 'numero') e que o 'numero' está entre 1 e 99
    return (type(arg) == tuple and len(arg) == 2 and
            type(arg[0]) == str and len(arg[0]) == 1 and ord('A') <= ord(arg[0]) <= ord('Z') and
            type(arg[1]) == int and 1 <= arg[1] <= 99)

def eh_intersecao_valida(t,i):
    '''Verifica se a interseção fornecida corresponde a uma interseção no território.

    Parâmetros:
        t (territorio)
        i (intersecao)
    Retorna:
        boolenao
    '''

    ultima_intersec = obtem_ultima_intersecao(t)

    #interseção está entre ('A',1) e a última interseção do território fornecido
    if not (ord('A') <= ord(i[0]) <= ord(ultima_intersec[0]) 
            and 1 <= i[1] <= ultima_intersec[1]):
        return False
    
    return True

def eh_intersecao_livre(t,i):
    '''Verifica, tendo em conta o território fornecido, se a interseção corresponde
    a um espaço livre (espaço que não tem montanha).

    Parâmetros:
        t (territorio)
        i (intersecao)
    Retorna:
        booleano
    '''
    
    return t[ord(i[0]) - ord('A')][i[1] - 1] == 0
    
def obtem_intersecoes_adjacentes(t,i):
    '''Retorna o tuplo formado pelas interseções do território fornecido que são
    adjacentes à interseção fornecida.
     
    Parâmetros:
        t (territorio)  
        i (intersecao)
    Retorna:
        tuplo
    '''

    intersec_adj = ()

    #margem inferior
    if i[1] != 1:
        intersec_adj += ((i[0], i[1] - 1),)
    #margem esquerda
    if i[0] != 'A':
        intersec_adj += ((chr(ord(i[0]) - 1), i[1]),)
    #margem direita
    if i[0] != chr(len(t) + 64):
        intersec_adj += (((chr(ord(i[0]) + 1)), i[1]),)
    #margem superior
    if i[1] != len(t[0]):
        intersec_adj += ((i[0], i[1] + 1),)

    return intersec_adj

def ordena_intersecoes(tup):
    '''Recebe um tuplo e retorna-o ordenado pela ordem de leitura do território.

    Parâmetros:
        tup (tuplo)
    Retorna:
        tuplo
    '''

    #ordena por numeros e depois por letras -> (('B',1),('A',1))
    return tuple(sorted(list(tup), key = lambda x:(x[1],x[0])))

def territorio_para_str(t):
    '''Retorna a cadeia de caracteres que o representa o território recebido.

    Parâmetros:
        t (territorio)
    Retorna:
        cadeia de caracteres
    '''

    if eh_territorio(t) == False:
        raise ValueError ('territorio_para_str: argumento invalido')

    ultima_intersecao = obtem_ultima_intersecao(t)
    colunas = '  '
    linhas = '\n'
    coluna_atual = ord(ultima_intersecao[0]) - ord('A') + 2

    #primeira e última linha (' ' A B ... n)
    for i in range(ord('A'), ord(ultima_intersecao[0]) + 1):
        colunas += ' ' + chr(i)

    #percorre os números
    for num_atual in range(ultima_intersecao[1]):
        #percorre as colunas: (' ' A B ... n)
        for j in range(coluna_atual + 1):
            espaco = 1
            #verifica se o numero da linha tem mais que um dígito
            if ultima_intersecao[1] - num_atual > 9:
                espaco = 0
            #numero da esquerda
            if j == 0:    
                linhas += ' '*espaco + str(ultima_intersecao[1] - num_atual)
            #numero da direita
            elif j == coluna_atual:
                linhas += ' ' +  ' '*espaco + str(ultima_intersecao[1] - num_atual)
            #montanha ou livre (X ou .)
            elif t[j - 1][ultima_intersecao[1] -1 - num_atual] == 0:
                linhas += ' .'
            elif t[j - 1][ultima_intersecao[1] - 1 - num_atual] == 1:
                linhas += ' X'
        linhas += '\n'  

    return colunas + linhas + colunas

def obtem_cadeia(t,i):
    '''Retorna o tuplo formado por todas as interseções que estão conectadas à
    interseção dada, quer sejam montanhas ou não. 

    Parâmetros:
        t (territorio)
        i (intersecao)
    Retorna:
        tuplo
    '''

    if not (eh_territorio(t) and eh_intersecao(i) and eh_intersecao_valida(t,i)):
        raise ValueError('obtem_cadeia: argumentos invalidos')
    
    cadeia = [i]
    
    for n in cadeia:
        for adjacente_n in obtem_intersecoes_adjacentes(t, n):
            if adjacente_n not in cadeia and eh_intersecao_livre(t,i) == eh_intersecao_livre(t,adjacente_n):
                cadeia += [adjacente_n]
                
    return ordena_intersecoes(tuple(cadeia))

def obtem_vale(t,i):
    '''Recebe uma interseção ocupada por uma montanha e retorna um tuplo formado por 
    todas as interseções que fazem parte do vale da montanha fornecida.

    Parâmetros:
        t (territorio)
        i (intersecao)
    Retorna:
        tuplo
    '''

    #confirma o território e a interseção são válidos e que a interseção é uma montanha
    if not (eh_territorio(t) and eh_intersecao(i) and eh_intersecao_valida(t,i) and t[ord(i[0]) - ord('A')][i[1] - 1] == 1):
        raise ValueError('obtem_vale: argumentos invalidos')
    
    vale = ()

    for montanha in obtem_cadeia(t,i):
        for intersec in obtem_intersecoes_adjacentes(t,montanha):
            #confirma que a interseção que rordeia a montanha não é uma montanha
            if t[ord(intersec[0]) - ord('A')][intersec[1] - 1] == 0 and intersec not in vale:
                vale += (intersec,)

    return ordena_intersecoes(vale)

def verifica_conexao(t,i1,i2):
    '''Analisa duas interseções de um território e verifica se estão na mesma cadeia.

    Parâmetros:
        t (territorio)
        i1 (intersecao)
        i2 (intersecao)
    Retorna:
        booleano
    '''

    if not (eh_territorio(t) and eh_intersecao(i1) and eh_intersecao(i2) and
            eh_intersecao_valida(t,i1) and eh_intersecao_valida(t,i2)):
        raise ValueError('verifica_conexao: argumentos invalidos')
    
    return(i2 in obtem_cadeia(t,i1))

def calcula_numero_montanhas(t):
    '''Retorna o número de interseções correspondentes a montanhas no território.

    Parâmetros:
        t (territorio)
    Retorna:
        int
    '''

    if not eh_territorio(t):
        raise ValueError('calcula_numero_montanhas: argumento invalido')

    n_montanhas = 0

    #percorre todo o território e soma 1 a n_montanhas quando encontra uma montanha
    for i in range(len(t)):
        for j in t[i]:
            if j == 1:
                n_montanhas += 1

    return n_montanhas

def calcula_numero_cadeias_montanhas(t):
    '''Retorna o número de cadeias de montanhas contidas no território fornecido.

    Parâmetros:
        t (territorio)
    Retorna:
        int
    '''

    if not eh_territorio(t):
        raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')
    
    n_cadeias = 0
    montanhas = []
    
    for i in range(len(t)):
        for j in range(len(t[i])):

            intersecao = (chr(i + ord('A')), (j+1))

            #verifica se a interseção é uma montanha e se a cadeia a que pretence ainda não foi contabilizada
            if t[i][j] == 1 and intersecao not in montanhas:        
                montanhas += obtem_cadeia(t,intersecao)
                n_cadeias += 1

    return n_cadeias

def calcula_tamanho_vales(t):   	
    '''Retorna o número de interseções que correspondem a vales num dado território.
    Sabendo que um vale é qualquer espaço livre que tenha uma montanha adjacente a si. 

    Parâmetros:
        t (territorio)
    Retorna:
        int
    '''

    if not eh_territorio(t):
        raise ValueError('calcula_tamanho_vales: argumento invalido')
    
    count = 0

    #percorre todos os pontos do território
    for i in range(len(t)):
        for j in range(len(t[i])):
            #caso a interseção não seja uma montanha, verifica se à sua volta existem 
            #montanhas, caso positivo, contabiliza-a como sendo um vale
            if t[i][j] == 0:
                for k in obtem_intersecoes_adjacentes(t,(chr(i + ord('A')), j + 1)):
                    if not eh_intersecao_livre(t,k):
                        count += 1
                        break

    return count
