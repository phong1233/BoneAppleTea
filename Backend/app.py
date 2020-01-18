from flask import Flask
from flask import request
from services import Services

app = Flask(__name__)
service = Services()

@app.route('/')
def hello_world():
    return 'The app is running properly'

@app.route('/recipes', methods=['GET'])
def get_recipes():
    return service.get_recipes()
# @app.route('/rejectRecipe', method=['POST'])
# def del_recipes():


if __name__ == '__main__':
    app.run()