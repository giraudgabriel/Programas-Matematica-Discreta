conjunto = input("Defina seu conjunto: (*Separado por virgula): \n").split(',')

pares = input("Defina seus pares: (*No formato x,y separados por espaco | exemplo:x,y k,l \n").split()

contador = 0
for c in conjunto:
    for k in conjunto:
        for par in pares:
            x,y = par.split(',')[0],par.split(',')[1]
            if(x == y and x == c and y == k):
                contador+=1

if(contador == len(conjunto)):
    print("É uma endorelação reflexiva!")
else:
    print("Não é uma endorelação reflexiva!")


