from flask import Flask,jsonify,request
from storage import all_movies,liked_movies,not_liked_movies,did_not_watch_movies
from contentfiltering import get_recommendation
from demographicfiltering import output

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success!"
    })

@app.route("/liked-movie",methods = ["POST"])
def liked_movie():
    movie = all_movies[0]
    liked_movies.append(movie)
    all_movies = all_movies[1:]
    return jsonify({
        "status": "success!"
    })

@app.route("/unliked-movie",methods = ["POST"])
def not_liked_movie():
    movie = all_movies[0]
    not_liked_movies.append(movie)
    all_movies = all_movies[1:]
    return jsonify({
        "status": "success!"
    })

@app.route("/did-not-watch-movie",methods = ["POST"])
def did_not_liked_movie():
    movie = all_movies[0]
    did_not_watch_movies.append(movie)
    all_movies = all_movies[1:]
    return jsonify({
        "status": "success!"
    })

@app.route("/popular-movies")
def popular_movies():
    movie_data = []
    for i in output:
        data = {
            'title': i[0],
            'poster_link': i[1],
            'release_date': i[2] or "N/A",
            'duration': i[3],
            'rating': i[4],
            'overview': i[5]
        }
        movie_data.append(data)
    return jsonify({
        "data": movie_data,
        "status": "success!"
    })

@app.route("/recommended-movies")
def recommended_movies():
    all_recommended = []
    for movie in liked_movies:
        output = get_recommendation(movie[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    movie_data = []
    for i in all_recommended:
        data = {
            'title': i[0],
            'poster_link': i[1],
            'release_date': i[2] or "N/A",
            'duration': i[3],
            'rating': i[4],
            'overview': i[5]
        }
        movie_data.append(data)
        return jsonify({
            'data': movie_data,
            'status': "success!"
        })

if __name__ == "__main__":
    app.run()
