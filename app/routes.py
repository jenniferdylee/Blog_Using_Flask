from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author' : {'username' : 'Jennifer'},
            'body' : 'Beautiful day in Seoul!'
        },
        {
            'author' : {'username' : 'Jiyun'},
            'body' : 'The Hoppers movie was so good'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
