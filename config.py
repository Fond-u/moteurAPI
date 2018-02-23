import os

# Database initialization
basedir = os.path.abspath(os.path.dirname(__file__))
datadir = os.path.join(basedir,"mdrapp", "data")
METADATA = os.path.join(datadir, 'movie_metadata.csv')
RECOMMANDATA = os.path.join(datadir, 'recommand.csv')