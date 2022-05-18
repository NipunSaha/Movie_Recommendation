import csv

all_movies = []
liked_movies = []
not_liked_movies = []
did_not_watch_movies = []

with open("final.csv") as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    all_movies = data[1:]