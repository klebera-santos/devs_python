print("**************************************************************************************************************************************************")
print("Jogo da Adivinhação")
print("******************************************")
numero_secreto = 42
chute_str = input("Digite um número: ")
print("Voce digitou:" + chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto

if (acertou == chute):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (chute < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")