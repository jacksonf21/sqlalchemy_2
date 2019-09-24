from flask import Flask, jsonify, render_template, redirect, request
from aws_rekog import detect_text
import json
import base64
# from boost import boost
from upload import upload


app = Flask(__name__)

@app.route('/')
def index():
    return "idx pg"

@app.route('/food', methods=['GET'])
def foods():
    food_items = {"result": detect_text('photo', 'bucket')}
    return jsonify( food_items )

@app.route('/image', methods=['GET'])
def prompt():
    return render_template('list.html')

@app.route('/image', methods=['POST'])
def image():
    x = request.form['image_data'] 
    
    with open("imageToSave.jpg", "wb") as fh:
        fh.write(base64.b64decode(x))

    upload("imagessplitus", 'imageToSave.jpg', 'test1.jpg')

    food_items = {"result": detect_text('test1.jpg', 'imagessplitus')}
    print (food_items)
    
    return jsonify( food_items )

    # return redirect("http://127.0.0.1:5000/image", code=302)


if __name__ == '__main__':
    app.run(debug=True)