def pegar_dados(nome_arq):
    arq = open(nome_arq, 'r')

    dados = arq.readlines()

    lista_analise = []

    conta_pulos = 0

    for linha in dados:
        if linha.startswith('Análise'):
            conta_pulos = 0
            linha = linha.replace('\n', '')
            novo_dic_imagem = {
                "Imagem" : linha[19:],
                "Rotulos" : []
            }

        elif linha.startswith('description'):
            conta_pulos = 0
            linha = linha.replace('"', '')
            linha = linha.replace('\n', '')
            tag = linha[13:]
        elif linha.startswith('score'):
            conta_pulos = 0
            linha = linha.replace('\n', '')
            pontuacao = linha[7:]
        elif linha.startswith('topicality'):
            conta_pulos = 0
            linha = linha.replace('\n', '')
            importancia = linha[12:]

            novo_dic_rotulo = {
                "Tag" : tag,
                "Pontuacao" : pontuacao,
                "Importancia" : importancia
            }

            novo_dic_imagem["Rotulos"].append(novo_dic_rotulo)
        elif linha == '\n':
            conta_pulos += 1

        if conta_pulos == 2:
            lista_analise.append(novo_dic_imagem)

    print(lista_analise)
    print('\n')
    return lista_analise

def pegar_rotulos(lista_analise):

    dic_rotulos = {}

    for analise in lista_analise:
        for rotulo in analise["Rotulos"]:
            if(rotulo["Tag"] in dic_rotulos):
                dic_rotulos[rotulo["Tag"]] += 1
            else:
                dic_rotulos.update({rotulo["Tag"] : 1})

    print(dic_rotulos)
    print('\n')
    print(sorted(dic_rotulos.values()))
    print('\n')
    return dic_rotulos

def rotulos_mais_usados(dic_rotulos):
    mais_usados = []
    valores_ordenados = sorted(dic_rotulos.values())
    todas_chaves = []

    while(len(mais_usados) < 6):
        for rotulo in dic_rotulos:
            if (dic_rotulos[rotulo] == valores_ordenados[-1]) and (rotulo not in todas_chaves):
                dic = {rotulo : dic_rotulos[rotulo]}
                del(valores_ordenados[-1])
                print(valores_ordenados)
                mais_usados.append(dic)

                todas_chaves = set().union(*(todos_dic.keys() for todos_dic in mais_usados))
                break

    print(mais_usados)
    print('\n')
    return mais_usados

def procurar_dois_rotulos(lista_analise, rotulo1, rotulo2):
    lista_rot1 = []
    lista_rot2 = []

    for analise in lista_analise:
        for rotulo in analise["Rotulos"]:
            if rotulo["Tag"] == rotulo1:
                lista_rot1.append(analise)

    #print(lista_rot1)

    for analise in lista_analise:
        for rotulo in analise["Rotulos"]:
            if rotulo["Tag"] == rotulo2:
                lista_rot2.append(analise)

    uniao = [analise for analise in lista_rot1 if analise in lista_rot2]
    print(uniao)
    print('\n')
    print(len(uniao))
    print('\n')
    return uniao

def main():
    lista_analise = pegar_dados('marielle_50000_rotulos.txt')
    dic_rotulos = pegar_rotulos(lista_analise)
    rotulos_mais_usados(dic_rotulos)
    procurar_dois_rotulos(lista_analise, 'Hair', 'Hairstyle')
    print(dic_rotulos["Product"])

main()
