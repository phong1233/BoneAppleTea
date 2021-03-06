from flask import Flask, request
import json
#from recipe_operation import send_next_10
import recipe_operation
app = Flask(__name__)

@app.route('/')
def base_index():
    return 'THE WEBSITE IS WORKING!!!'

# Returns 10 recipes
@app.route('/send_next_recipes', methods=['GET'])
def send_next_recipes():
    return recipe_operation.send()

# receive, put in databases
@app.route('/receive_recipes', methods=['POST'])
def receive_recipes():
    received = request.json
    return True

@app.route('/accept', methods=['POST'])
def accept():
    dic = request.json

    recipe_operation.accept(dic)
    return "Good"

@app.route('/reject', methods=['POST'])
def reject():
    received = request.json
    dic = json.load(received)
    dic['like'] = False
    recipe_operation.receive(dic)
    return True

@app.route('/like', methods=['GET'])
def like():
    return recipe_operation.get_like()

if __name__ == '__main__':
    recipe_operation.start_database()

    app.run()