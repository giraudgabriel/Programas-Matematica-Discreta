#programa sobre transitividade
def gerarTransitividade(conjunto, pares):
    transitividade = []
    for i in range(len(pares)):
        a,b = pares[i].split(',')[0],pares[i].split(',')[1]
        x,y = pares[i].split(',')[0],pares[i].split(',')[1]
        if(x in conjunto):
            if(x+','+y not in pares):
             transitividade.append(x+y)
    return transitividade
def sort(valor):
    return valor[0]

def definirPares(conjunto):
    pares = {}
    for c in conjunto:
        pares[str(c)]={'filhos':[]}
    return pares
    
def definirConjunto(conjunto):
    conjunto = conjunto.split(',')
    valores = []
    for c in conjunto:
        valores.append(int(c))
    return valores

def definirTransitividade(relacoes):
    relacoes = relacoes.split()
    for relacao in relacoes:
        x,y = relacao.split(',')[0],relacao.split(',')[1]
        pares[x]["filhos"].append(y)
    print (pares)

conjunto = input("Digite seu conjunto: (*valores separados por virgula) \n")

conjunto = definirConjunto(conjunto)

pares = definirPares(conjunto)

relacoes = input('Digite as relações: (* formato x,y separado por espaço (exemplo: x,y a,b)) \n')

definirTransitividade(relacoes)


# transitividade = gerarTransitividade(conjunto, pares)

# print(transitividade)