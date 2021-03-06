import argparse
import io
import os

from google.cloud import vision

def annotate(path):
    """Returns web annotations given the path to an image."""
    client = vision.ImageAnnotatorClient()

    if path.startswith('http') or path.startswith('gs:'):
        image = vision.Image()
        image.source.image_uri = path

    else:
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

    web_detection = client.web_detection(image=image).web_detection

    return web_detection

def report(annotations, imagem):
    """Prints detected features in the provided web annotations."""

    print("Guardando resultados num arquivo .txt...")
    arq_txt = open("biroliro_teste_web.txt", "a")
    arq_txt.write("Análise de Imagem: " + imagem + "\n")
    arq_txt.write("\n")
    print(imagem)

    if annotations.pages_with_matching_images:
        #print('\n{} Pages with matching images retrieved'.format(
        #    len(annotations.pages_with_matching_images)))

        for page in annotations.pages_with_matching_images:
            #print('Url   : {}'.format(page.url)
            print("\n")

    if annotations.full_matching_images:
        print('\n{} Full Matches found: '.format(
              len(annotations.full_matching_images)))

        arq_txt.write("Pares Totais:\n")
        for image in annotations.full_matching_images:
            print('Url  : {}'.format(image.url))
            arq_txt.write(str('Url  : {}'.format(image.url)) + "\n")

        arq_txt.write("\n")

    if annotations.partial_matching_images:
        print('\n{} Partial Matches found: '.format(
              len(annotations.partial_matching_images)))

        arq_txt.write("Pares Parciais:\n")
        for image in annotations.partial_matching_images:
            print('Url  : {}'.format(image.url))
            arq_txt.write(str('Url  : {}'.format(image.url)) + "\n")

        arq_txt.write("\n")

    if annotations.web_entities:
        print('\n{} Web entities found: '.format(
              len(annotations.web_entities)))

        for entity in annotations.web_entities:
            print('Score      : {}'.format(entity.score))
            arq_txt.write(str('Score      : {}'.format(entity.score)))
            arq_txt.write("\n")
            print('Description: {}'.format(entity.description))
            arq_txt.write(str('Description: {}'.format(entity.description.encode("utf-8"))))
            arq_txt.write("\n")

        arq_txt.write("\n")
        arq_txt.close()

if __name__ == '__main__':
    #parser = argparse.ArgumentParser(
    #    description=__doc__,
    #    formatter_class=argparse.RawDescriptionHelpFormatter)
    #path_help = str('The image to detect, can be web URI, '
    #                'Google Cloud Storage, or path to local file.')
    #parser.add_argument('image_url', help=path_help)
    #args = parser.parse_args()

    for imagem in os.listdir(r"C:\Users\vinic\Onedrive\Imagens\Teste_opiniao"):
        if(imagem.endswith(".jpg") or imagem.endswith(".png") or imagem.endswith(".jpeg")):
            print("Analisando imagem através de dados da internet...")
            report(annotate(r"C:\Users\vinic\Onedrive\Imagens\Teste_opiniao/" + imagem), imagem)
            print("Análise Finalizada!")
            print("\n")

    print("Script Finalizado!")
