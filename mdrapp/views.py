import numpy as np
import random
from flask import Flask, render_template, jsonify, request

from .utils import *

app = Flask(__name__)

app.config.from_object('config')

sof = load_data_init(app.config['METADATA'])
rf = load_data_recom(app.config['RECOMMANDATA'])

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html' , imin = sof.get_index_min(), imax = sof.get_index_max())


@app.route('/film/<id_film>')
def film(id_film):
	if controle_num(id_film):
		return bad_num()
	if int(id_film) not in rf.list_index():
		return remove_num()
	return render_template('film.html', id_film = id_film, title_film = sof.get_title_from_id(int(id_film)), lien_film = sof.get_link_from_id(int(id_film)))

@app.route('/film/')
def film2():
	id_film = request.args.get('id_film')
	if controle_num(id_film):
		return bad_num()
	if int(id_film) not in rf.list_index():
		return remove_num()
	return render_template('film.html', id_film = id_film, title_film = sof.get_title_from_id(int(id_film)), lien_film = sof.get_link_from_id(int(id_film)))

@app.route('/recommand/<id_film>')
def recommend(id_film):
	if controle_num(id_film):
		return bad_num()
	if int(id_film) not in rf.list_index():
		return remove_num()
	return jsonify(_request={'id':id_film, 'name':sof.get_title_from_id(int(id_film))},_result=formatresult(rf.get_5_from_10first(id_film), sof))

@app.route('/bad_num/')
def bad_num():
	return 'Votre saisie est incorrect :  <a href= "/"> retour index </a>'

@app.route('/remove_num/')
def remove_num():
	return 'Cet indice a été retiré de la liste de film pour cause de doublon : <a href= "/"> retour index </a>'