#define o valor de limiar 
limiar = 5

menores = [] # cria lista que receberá os valores menores 
maiores = [] # cria lista dos valores maiores que cinco

#Cria um lanço com os numéros de 1 a 10 e faz a divisão entre os maiores e menores 
for i in range(10):
    if(i<limiar):
        menores.append(i)
    elif (i >= limiar):
        maiores.append(i)

# imprime na tela os resultados das listas
print('Resultado final')
print('menores:', menores)
print('maiores:', maiores)
