import io
import os

from google.cloud import vision

#Instancia um cliente
client = vision.ImageAnnotatorClient()

print("Acessando diretório...")
for file in os.listdir(r"C:\Users\vinic\Onedrive\Documentos\Pesquisa\Python\Download_Imagens_Instagram\testes_marielle_rotulos"):
    if(file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")):
        #Caminho da imagem a ser rotulada
        file_name = os.path.abspath(r"C:\Users\vinic\Onedrive\Documentos\Pesquisa\Python\Download_Imagens_Instagram\testes_marielle_rotulos/" + file)

        #Carrega imagem na memória
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        #Carrega conteúdo da imagem na API
        image = vision.Image(content=content)

        #Rotula imagem
        print("Rotulando imagem...")
        response = client.label_detection(image=image)
        labels = response.label_annotations

        #Escreve rótulos em .txt
        print("Guardando rótulos em documento .txt...")
        arq_txt = open("teste_marielle_rotulos.txt", "a")
        arq_txt.write("Análise de Imagem: " + file + "\n")
        for rotulo in labels:
            arq_txt.write(str(rotulo) + "\n")

        arq_txt.write("\n")
        arq_txt.close()

        print("Análise de Imagem Finalizada!")

print("Todas imagens no diretório foram analizadas!")
