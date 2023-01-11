from pytube import YouTube
import movie.py.editor as mp
import re
import os 

#Digite o link do video e o local que deseja salvar o mp3 # 
link = input("Digite o link do video que deseja baixar:")
path = input("Digite o diretorio que deseja salvar o arquivo:")
yt = YouTube(link)

#Começa o Download #
print("Baixando ...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download Completo")

#Converte mp4 para mp3#

