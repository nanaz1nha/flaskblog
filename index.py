from flask import Flask, render_template

app = Flask(__name__)


SITE = {
    'name': 'FlaskBlog',
    'logo': '<img src="/static/img/logo01.png" alt="">',
    'favicon': '/static/img/favicon.png',
    'slogan': 'Cabe tudo dentro!',
    'license': '<i class="fa-regular fa-copyright fa-fw fa-flip-horizontal"></i> Copyleft 2024 Joca da Silva'
}


@app.route('/')
def home():
    toPage = {
        'title': '',
        'site': SITE,
        'css': 'home.css',
        'js': 'home.js'
    }
    return render_template('home.html', page=toPage)


@app.route('/contacts')
def contacts():
    toPage = {
        'title': 'Faça contato',
        'site': SITE,
        'css': 'contacts.css',
        'js': 'contacts.js'
    }
    return render_template('contacts.html', page=toPage)


@app.route('/about')
def about():
    toPage = {
        'title': 'Sobre...',
        'site': SITE,
        'css': 'about.css',
        'js': 'about.js'
    }
    return render_template('about.html', page=toPage)


@app.route('/policies')
def policies():
    toPage = {
        'title': 'Políticas de Privacidade',
        'site': SITE,
        'css': 'policies.css'
    }
    return render_template('policies.html', page=toPage)


@app.route('/search')
def search():
    toPage = {
        'title': 'Procurar',
        'site': SITE
    }
    return render_template('search.html', page=toPage)


@app.errorhandler(404)
def page_not_found(e):
    toPage = {
        'title': 'Erro 404',
        'site': SITE
    }
    return render_template('404.html', page=toPage), 404


if __name__ == '__main__':
    app.run(debug=True)
