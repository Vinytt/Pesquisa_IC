import urllib.request
import os

arq = open("marielle_50000_rotulos_web.txt", "r")
n = 1

print("Codigo Iniciado\n")
for linha in arq:
    if(linha.startswith("A")):
        indice_corte1 = linha.find("20")
        linha_editada = linha.replace("\n", "")
        indice_corte2 = linha.find(".jpg")
        pasta = linha_editada[indice_corte1:indice_corte2]
        print("Analise da Imagem: " + pasta + "\n")

        os.system(r"mkdir C:\Users\vinic\OneDrive\Imagens\prints_analises\50000_rotulacao_web" + "\\" + pasta)

        n = 1
    elif(linha.startswith("Url")):
        indice_corte = linha.find("https")
        linha_editada = linha.replace("\n", "")
        url = linha_editada[indice_corte:]

        print("Baixando URL: " + url + "\n")

        try:
            urllib.request.urlretrieve(url=url, filename=r"C:\Users\vinic\OneDrive\Imagens\prints_analises\50000_rotulacao_web" + "\\" +
            pasta + "\\" + str(n)+ ".jpg")
            n = n + 1
        except:
            print("Nao foi possivel baixar a imagem nesse url!\n")
            continue
    else:
        continue
print("Script Finalizado!\n")
