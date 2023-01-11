usuario = input("Qual o usuário?" ).strip()

usuario1 = usuario == "Kleber"
usuario2 = usuario == "Re"
usuario3 = usuario == "Gui"
usuario4 = usuario == "Ana"

if(usuario1 or usuario2 or usuario3 or usuario4):
    print(f"Seja bem-vindo {usuario}!")
else:
    print("Usuario não encontrado!")