from flask import Flask, render_template
from flask_mysqldb import MySQL, MySQLdb


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskblogdb'

mysql = MySQL(app)


SITE = {
    'name': 'FlaskBlog',
    'logo': '<img src="/static/img/logo01.png" alt="">',
    'favicon': '/static/img/favicon.png',
    'slogan': 'Cabe tudo dentro!',
    'license': '<i class="fa-regular fa-copyright fa-fw fa-flip-horizontal"></i> Copyleft 2024 Joca da Silva'
}


@app.route('/')
def home():

    sql = '''
        SELECT art_id, art_title, art_resume, art_thumbnail
        FROM article 
        WHERE art_status = 'on' 
        ORDER BY art_date DESC;
    '''
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    articles = cur.fetchall()
    cur.close()

    # print(articles)

    toPage = {
        'title': '',
        'site': SITE,
        'css': 'home.css',
        'js': 'home.js',
        'articles': articles
    }
    return render_template('home.html', page=toPage)


@app.route('/view/<artid>')
def view(artid):

    if not artid.isdigit():
        return page_not_found(404)

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = '''
        SELECT *, 
            DATE_FORMAT(art_date, '%%d/%%m/%%Y às %%H:%%i') AS art_datebr,
            TIMESTAMPDIFF(
                YEAR, 
                sta_birth, 
                CURDATE()) - (DATE_FORMAT(CURDATE(), '00-%%m-%%d') < DATE_FORMAT(sta_birth, '00-%%m-%%d')
            ) AS sta_age
        FROM article 
        INNER JOIN staff ON art_author = sta_id
        WHERE art_id = %s 
	        AND art_status = 'on';
    '''
    cur.execute(sql, (artid,))
    article = cur.fetchone()
    
    print(article)

    if article is None:
        return page_not_found(404)
    
    update_sql = "UPDATE article SET art_views = art_views + 1 WHERE art_id = %s"
    cur.execute(update_sql, (artid,))
    mysql.connection.commit()
    cur.close()

    toPage = {
        'title': article['art_title'],
        'site': SITE,
        'css': 'view.css',
        'article': article
    }
    return render_template('view.html', page=toPage)


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
