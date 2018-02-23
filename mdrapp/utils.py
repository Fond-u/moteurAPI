from mdrapp.models import SetOfFilm, filmRecommand
from flask import jsonify


def load_data_init(data_file):
	sof = SetOfFilm("liste de film")
	sof.data_from_csv(data_file)
	return sof

def load_data_recom(data_file):
	rf = filmRecommand()
	rf.data_from_csv(data_file)
	return rf

def formatresult(tbl_id, cl_name):
    t = []
    for idx in tbl_id:
    	name = cl_name.get_title_from_id(int(idx))
    	dic = {'id':idx, 'name':name}
    	t.append(dic)

    return t


def controle_num(val):
	try:
		num = int(val)
		if num >= 0 and num < 5043:
			return False
		else:
			return True
	except:
		return True