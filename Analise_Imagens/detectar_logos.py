import os

def detect_logos(path):
    """Detects logos in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    print("Guardando rótulos em documento .txt...")
    arq_txt = open("marielle_50000_logos.txt", "a")
    indice = path.find("20")
    arq_txt.write("Análise de Imagem: " + path[indice:] + "\n")

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print('Logos:')

    for logo in logos:
        print(logo.description)
        arq_txt.write(str(logo.description) + "\n")

    arq_txt.write("\n")

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    arq_txt.close()

for imagem in os.listdir(r"C:\Users\vinic\Onedrive\Documentos\Pesquisa\Python\Download_Imagens_Instagram\marielle_50000"):
    if(imagem.endswith(".jpg") or imagem.endswith(".png") or imagem.endswith(".jpeg")):
        detect_logos(r"C:\Users\vinic\Onedrive\Documentos\Pesquisa\Python\Download_Imagens_Instagram\marielle_50000/" + imagem)
