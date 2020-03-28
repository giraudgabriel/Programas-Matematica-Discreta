conjunto = input("Defina seu conjunto: (*Separado por virgula): \n").split(',')

pares = input("Defina seus pares: (*No formato x,y separados por espaco | exemplo:x,y k,l \n").split()

print('  '+' '.join(conjunto))

valores = {}

for c in conjunto:
        valores[c] = {':'.join(valores):'0'}

print(valores)

# for par in pares:
#         x,y = par.split(',')[0], par.split(',')[1]
#         if(x in conjunto):
#                 valores[x]["valores"].append()
#                 valores.append('1')
    