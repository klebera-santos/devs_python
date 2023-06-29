import math
print("Bem vindo, a Simulação Salarial")
pessoa = str(input("Digite seu nome: "))
print("Ok! " +pessoa+ " Precisaremos de algumas informações para continuar:")
salario = int(input("Digite o valor do salario CLT que deseja simular:?"))
horastrabalhadas = float(input("Digite a quantidade de horas trabalhadas na semama:?"))
horasmes = horastrabalhadas * 4 #  Calculando o total de horas do Mes 
#valorhora = math.ceil(salario/horasmes) # usando o classe math e a função ceil 
valorhora = round(salario/horasmes, 2) 
print("Suas horas totais no mes são:" + str(horasmes))
print("Seu valor hora é:" + str(valorhora))