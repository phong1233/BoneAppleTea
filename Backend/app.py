from flask import Flask

app = Flask(__name__)

@app.route('/')
def base_index():
    return 'THE WEBSITE IS WORKING!!!'


if __name__ == '__main__':
    app.run()