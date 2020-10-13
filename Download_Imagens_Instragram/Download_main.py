#código generalizado de download para o instagram
import argparse
import instaloader
import Download_filtros

#Função para baixar imagens de uma hashtag, seguindo um filtro e possivelmente um limite de paciencia
#As imagens são baixadas em "pasta"
def baixar(hashtag, filtro, usa_paciencia, pasta):
    paciencia = 0
    paciencia_total = 1000

    instaBot = instaloader.Instaloader(compress_json=False, download_comments=False, download_videos=False,
                                max_connection_attempts=8000,  dirname_pattern='{target}', filename_pattern='{date_local}_BRT')

    print("Requisitando posts...\n")

    lista_posts = instaBot.get_hashtag_posts(hashtag)

    print("Iniciando contagem...\n")

    for post in lista_posts:
        if(filtro(post)):
            paciencia = 0
            print("Post encontrado!\n")
            instaBot.download_post(post, pasta)
        else:
            paciencia = paciencia + 1
            if (paciencia == paciencia_total and usa_paciencia):
                print("Fim do processo\n")
                break


analisador = argparse.ArgumentParser(description="Código iniciado\n")

#argumentos sendo passados por linha de comando
analisador.add_argument("--hashtag", required = True, help = "Hashtag continda nos posts que se deseja baixar\n")
analisador.add_argument("--operacao", required = True, help = "Operação de download a ser realizada, detre as seguintes:\n")
analisador.add_argument("--pasta", help = "Pasta onde as imagens devem ser baixadas\n", default="mais_recente")

argumentos = vars(analisador.parse_args())

hashtag = argumentos['hashtag']
operacao = argumentos['operacao']
pasta = argumentos['pasta']

usa_paciencia = True

#definir operação a ser realizada
if (operacao == "todas"):
    usa_paciencia = False
    filtro = Download_filtros.todas
elif (operacao == "mais_curtidas"):
    filtro = Download_filtros.mais_curtidas
elif (operacao == "todas_mais_curtidas"):
    usa_paciencia = False
    filtro = Download_filtros.mais_curtidas
elif (operacao == "ultima_semana"):
    filtro = Download_filtros.ultima_semana
else:
    print("Operacao não identificada. Execução falhou\n")
    quit()

baixar(hashtag, filtro, usa_paciencia, pasta)
