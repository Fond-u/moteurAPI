import os

# Database initialization
basedir = os.path.abspath(os.path.dirname(__file__))
ENGINE_DATABASE = os.path.join(basedir,"mdrapp", "data", 'movie_metadata.csv')