from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!"


@app.route('/contatos')
def peteca():
    return "Diga o que você quer agora!"


if __name__ == '__main__':
    app.run(debug=True)
