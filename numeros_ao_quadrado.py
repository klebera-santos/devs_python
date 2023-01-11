# Lista vazia para armazenar os resultados
quadrados = []

#Loop pelo range de números.

#for i in range(1,11):
#    quadrados.append(i * i)

#print(quadrados)

###
#Forma mais expert de fazer 

quadrados = [i * i for i in range(1,11)]

print(quadrados)