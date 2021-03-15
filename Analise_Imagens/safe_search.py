import os

def detect_safe_search(path):
    """Detects unsafe features in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.safe_search_detection(image=image)
    safe = response.safe_search_annotation

    print("Guardando rótulos em documento .txt...")
    arq_txt = open("marielle_iconicas_safe_search.txt", "a")
    indice = path.find("20")
    arq_txt.write("Análise de Imagem: " + path[indice:] + "\n")

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Safe search:')

    print('adult: {}'.format(likelihood_name[safe.adult]))
    arq_txt.write(str('adult: {}'.format(likelihood_name[safe.adult])) + "\n")
    print('medical: {}'.format(likelihood_name[safe.medical]))
    arq_txt.write(str('medical: {}'.format(likelihood_name[safe.medical])) + "\n")
    print('spoofed: {}'.format(likelihood_name[safe.spoof]))
    arq_txt.write(str('spoofed: {}'.format(likelihood_name[safe.spoof])) + "\n")
    print('violence: {}'.format(likelihood_name[safe.violence]))
    arq_txt.write(str('violence: {}'.format(likelihood_name[safe.violence])) + "\n")
    print('racy: {}'.format(likelihood_name[safe.racy]))
    arq_txt.write(str('racy: {}'.format(likelihood_name[safe.racy])) + "\n")

    arq_txt.write("\n\n")
    print("\n")

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    arq_txt.close()

for imagem in os.listdir(r"C:\Users\vinic\Onedrive\Documentos\Pesquisa\Python\Download_Imagens_Instagram\marielle_iconicas"):
    if(imagem.endswith(".jpg") or imagem.endswith(".png") or imagem.endswith(".jpeg")):
        detect_safe_search(r"C:\Users\vinic\Onedrive\Documentos\Pesquisa\Python\Download_Imagens_Instagram\marielle_iconicas/" + imagem)
