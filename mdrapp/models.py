# coding: utf-8
import pandas as pd

class SetOfFilm:
    def __init__(self, name):
    	self.name = name

    def data_from_csv(self, csv_file):
    	self.dataframe = pd.read_csv(csv_file, low_memory=False)

    def data_from_dataframe(self, dataframe):
    	self.dataframe = dataframe

    def get_title_from_id(self, idf):
    	return self.dataframe.movie_title[idf]