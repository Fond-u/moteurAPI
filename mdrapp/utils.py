from mdrapp.models import SetOfFilm


def load_data_csv(data_file):
	sof = SetOfFilm("liste de film")
	sof.data_from_csv(data_file)
	return sof