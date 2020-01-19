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
    dic["like"] = True
    recipe_operation.receive(dic)
    return "Good"

@app.route('/reject', methods=['POST'])
def reject():
    received = request.json
    dic = json.load(received)
    dic['like'] = False
    recipe_operation.receive(dic)
    return True

if __name__ == '__main__':
    app.run()