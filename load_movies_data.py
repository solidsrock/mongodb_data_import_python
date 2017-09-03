# the above just indicates to use python to intepret this file


import sys  # a python module with system functions for this OS
import pymongo  # python MongoDB module

# connect with mongo DB here
from pymongo import MongoClient

client = MongoClient()

# set the database
db = client['moviesdb']

# drop and recreate the collection
#db.drop_collection('ratings')
db.create_collection('movies')

# specify the collection to use
ratingsCollection = db.movies

# ------------------------------------------------------------
#  this 'for loop' will set 'line' to an input line from system
#    standard input file
# ------------------------------------------------------------
file2 = open('movies.dat')

for line in file2:
    word = line.split('::')
    movieid = word[0]
    Title = word[1]
    line2 = word[2]
    genre = line2.strip('\n')
    genres =genre.split("|")


    ratingsCollection.insert_one(
        {
            #"MovieID": userid,
            "MovieID": movieid,
            "Title": Title,
            "Genres": genres,
        }
    )
print("process finished")
# -----------------------------------
# sys.stdin call 'sys' to read a line from standard input,
# note that 'line' is a string object, ie variable, and it has methods that you can apply to it,
# as in the next line
# ---------------------------------
# movie file format -->MovieID::Title::Genres
# 1::Toy Story (1995)::Adventure|Animation|Children|Comedy|Fantasy
# process incoming lines of file

# insert data into mongo
