import numpy as np
import random
from flask import Flask, render_template
from flask import jsonify, request

from .utils import load_data_csv

app = Flask(__name__)

app.config.from_object('config')

#sof = load_data_csv(app.config['ENGINE_DATABASE'])

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html' )


#@app.route('/film/<id_film>')
#def film(id_film):
#	title = sof.get_title_from_id(int(id_film))
#	return render_template('film.html', id_film = id_film, title_film = title)

#@app.route('/film/')
#def film2():
#	idf = request.args.get('id_film')
#	title = sof.get_title_from_id(int(idf))
#	return render_template('film.html', id_film = idf, title_film = title)