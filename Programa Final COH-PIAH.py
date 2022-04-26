import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def n_caracteres_total(lista_palavras):
    ''' Essa função recebe uma lista de palavras e devolve o numero de caracteres total'''
    soma = 0
    for i in lista_palavras:
        soma = soma + len(i)
    return soma    


        
def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i=0
    soma = 0
    while i<=5:
        print(i)
        soma = soma + abs(as_a[i] - as_b[i])
        i=i+1
    similaridade = soma/6
    print("similaridade", similaridade)

    return similaridade


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    return [tam_medio_palavra(texto),  type_token(texto), hapax_legomana(texto), tam_medio_sentenca(texto), complexidade_sentenca(texto), tam_medio_frase(texto)]



def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista = []
    lista2 = []
    lista3 = []
    lista_suporte =[]
    c = -1
    for n in textos:
        a=0
        c = c+1
        lista_suporte.append(calcula_assinatura(n))
        while a<=5:
            lista3.append(lista_suporte[c][a])
            a = a + 1
    w=len(lista3)
    while w>0:
        lista2 = lista3[0:6]
        lista.append(compara_assinatura(lista2, ass_cp))
        del lista3[0:6]
        w = len(lista3)
    comparativo = 10000000
    infectado = 0
    print(lista)
    for i in lista:
        if i < comparativo:
            comparativo = i
            infectado = lista.index(i)+1
    return infectado    



def tam_medio_palavra(texto):
    qtd_palavras = len(separa_palavras(texto))
    soma = 0
    lista = separa_palavras(texto)
    for x in lista:
        char = "'!?,.():;/+*"
        for y in range(len(char)):
            x=x.replace(char[y],"")   
        soma = soma + len(x)
    tamanho_medio = soma / qtd_palavras
    return tamanho_medio

def type_token(texto):
    texto = texto.lower()
    char = "'!?,.():;/+*-"
    for y in range(len(char)):
        texto=texto.replace(char[y],"")
    qtd_palavras = len(separa_palavras(texto))
    qtd_diferentes = n_palavras_diferentes(separa_palavras(texto))
    type_token = qtd_diferentes / qtd_palavras
    return type_token

def hapax_legomana(texto):
    texto=texto.lower()
    char = "'!?,.():;/+*-"
    for y in range(len(char)):
        texto=texto.replace(char[y],"")
    lista = separa_palavras(texto)
    qtd_palavras = len(lista)
    iguais = 0
    for i in lista:
        j = 0
        aux=0
        while j < (qtd_palavras):
            if i == lista[j]:
                aux=aux+1
                if aux==2:
                    iguais = iguais + 1
                    j=qtd_palavras
            j=j+1        
    hapax_legomana = (qtd_palavras - iguais) / qtd_palavras
    return hapax_legomana

def tam_medio_sentenca(texto):
    qtd_sentencas = len(separa_sentencas(texto))
    texto=texto.lower()
    char = "'!?."
    for y in range(len(char)):
        texto=texto.replace(char[y],"")
    qtd_caracter = n_caracteres_total(texto)
    tam_medio_sentenca = qtd_caracter / qtd_sentencas
    return tam_medio_sentenca

def complexidade_sentenca(texto):
    lista = separa_sentencas(texto)
    frases=0
    for i in lista:
        frases = frases + len(separa_frases(i))
    complexidade = frases / len(lista)
    return complexidade


def tam_medio_frase(texto):
    lista = separa_sentencas(texto)
    frases = 0
    caracter = 0
    for i in lista:
        frases = frases + len(separa_frases(i))
        caracter = caracter + n_caracteres_total(separa_frases(i))
    tam_medio_frase = caracter / frases
    return tam_medio_frase


    
assinatura = le_assinatura()
print(assinatura)
textos = le_textos()
resposta = avalia_textos(textos, assinatura)
print("O autor do texo", resposta , "está infectado com COH-PIAH")

           







