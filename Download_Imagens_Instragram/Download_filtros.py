#filtros para o download de imagens
import datetime
from instaloader import Post

def todas(Post):
    return True

def mais_curtidas(Post):
    if(Post.likes >= 50000):
        return True
    else:
        return False

def ultima_semana(Post):
    if(Post.date_local >= datetime.datetime.now() - datetime.timedelta(days=7)):
        return True
    else:
        return False
