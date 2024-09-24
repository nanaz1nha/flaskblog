from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def home():
    toPage = {
        'title': app.config['SITENAME']
    }
    return render_template('layout.html', page=toPage)


@app.route('/contacts')
def peteca():
    return "Diga o que você quer agora!"


if __name__ == '__main__':
    app.run(debug=True)
