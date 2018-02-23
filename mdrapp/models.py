# coding: utf-8
import pandas as pd
from random import *

class SetOfFilm:
    def __init__(self, name):
    	self.name = name

    def data_from_csv(self, csv_file):
    	self.dataframe = pd.read_csv(csv_file, low_memory=False)

    def data_from_dataframe(self, dataframe):
    	self.dataframe = dataframe

    def get_title_from_id(self, idf):
    	return self.dataframe.movie_title[idf]

    def get_link_from_id(self,idf):
    	return self.dataframe.movie_imdb_link[idf]

    def get_index_min(self):
    	return self.dataframe.index.min()

    def get_index_max(self):
    	return self.dataframe.index.max()


class filmRecommand():
	def data_from_csv(self, csv_file):
		self.dataframe = pd.read_csv(csv_file, low_memory=False)
		self.dataframe = self.dataframe.set_index(self.dataframe['id_init'])

	def get_5_first(self,idf):
		tabl = []
		for x in range(5):
		    tabl.append(int(self.dataframe.loc[int(idf), 'film_{}'.format(x+1)]))
		return tabl

	def get_5_from_10first(self,idf):
		tab2 = []
		tabran = []
		while len(tab2) < 5 :
		    rn = randint(1, 10)
		    if rn not in tabran:
		        tab2.append(int(self.dataframe.loc[int(idf), 'film_{}'.format(rn)]))
		    tabran.append(rn)
		return tab2

	def list_index(self):
		return self.dataframe.index.tolist()