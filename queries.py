from flask import Flask, jsonify

from actor import Actor
from base import Session
from contact_details import ContactDetails
from movie import Movie

try: 
    from PIL import Image
except ImportError:
    import Image

from aws_rekog import detect_text

session = Session()

movies = session.query(Movie).all()
actors = session.query(Actor).all()

app = Flask(__name__)

# assigns info from db to obj for serialization
food_items = {"result": detect_text('photo', 'bucket')}
actorObj = {"actors": []}

# checks if querying is working
# print('n### All movies:')
# for movie in movies:
#     movieObj["movies"].append({"name": movie.title, "release_date": movie.release_date})
    # print(f'{movie.title} was release on {movie.release_date}')

# for actor in actors:
#     actorObj["actors"].append({"id": actor.id, "name": actor.name, "birthday": actor.birthday})


@app.route('/')
def index():
    return "idx pg"

@app.route('/food', methods=['GET'])
def foods():
    return jsonify( food_items )


if __name__ == '__main__':
    app.run(debug=True)