from flask import Flask, request
from Backend.recipe_operation import send_next_10
app = Flask(__name__)


@app.route('/')
def base_index():
    return 'THE WEBSITE IS WORKING!!!'

# Returns 10 recipes
@app.route('/send_next_recipes', methods=['GET'])
def send_next_recipes():
    return send_next_10()

# receive, put in databases
@app.route('/receive_recipes', methods=['POST'])
def receive_recipes():
    received = request.json


if __name__ == '__main__':
    app.run()