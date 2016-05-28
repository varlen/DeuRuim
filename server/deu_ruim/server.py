#
# to do:
# get_denuncias_from_db(num_denuncias, id_denuncia_inicial)
# post_denuncia_to_db(denuncia)
# definir classe denuncia
#

from flask import Flask, request
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

server_url = '127.0.0.1'
server_port = '5000'


@app.route('/stories', methods=['POST'])
def create_story():
    '''Persiste uma nova denuncia dado informações sobre ela'''
    pass

@app.route('/stories/<story_id>/<amount>', methods=['GET','OPTIONS'])
def get_stories( story_id, amount):
    '''
        Lista as denuncias persistidas.
        Opcionalmente
    '''
    '''Funcao que recebe o request para mostrar as denuncias mais recentes'''
    #pegar numero_denuncias e denuncia inicial do request
    # denuncia_inicial == id da denuncia
    pass

@app.route('/stories/<story_id>/reports', methods=['POST'])
def rate( story_id ):
    '''Funcao que recebe um voto para uma denuncia especificada por id'''
    stories = get_stories_from_db(1,story_id)
    story = stories[0]

    if (rating == 'up'): story.rating += 1
    else: story.rating -= 1

    post_story_to_db(story)

if __name__ == "__main__":
    app.run(server_url)
