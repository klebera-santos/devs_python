
#Instalando o pacote 
from gettext import install

"""
en(English, default)
am(Amharic)
ar(Arabic)
cz(Czech)
de (German)
dk(Danish)
it(Lithuanian)
lv(Latvian)
no(Norwegian)
pl(Polish)
pt(Portuguese)
pt_br(Portuguese - Brazilian)

"""


#!pip -q install num2words #type: ignore

#Importando o pacote
from num2words import num2words

#Coletando o número do usuário
#Neste exemplo usaremos o número 
numero = int(input('Digite um número: '))

#Utilizando a função num2words para gerar o número por extenso
num_pt_br = num2words(numero, lang = 'pt-br')
num_en = num2words(numero, lang = 'en')

#Imprimindo o resultado na tela 
print(f'Em Portugues: {num_pt_br}')
print(f'Em Ingles: {num_en}')