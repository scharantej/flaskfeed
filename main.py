 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    articles = [
        {'title': 'Article 1', 'content': 'This is the content of article 1.'},
        {'title': 'Article 2', 'content': 'This is the content of article 2.'},
        {'title': 'Article 3', 'content': 'This is the content of article 3.'}
    ]
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = {
        'title': 'Article 1',
        'content': 'This is the content of article 1.'
    }
    return render_template('article.html', article=article)

@app.route('/search')
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run()


html code for index.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Newsfeed</title>
</head>
<body>
    <h1>Newsfeed</h1>
    <ul>
        {% for article in articles %}
            <li><a href="/article/{{ article.id }}">{{ article.title }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>


html code for article.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Newsfeed</title>
</head>
<body>
    <h1>{{ article.title }}</h1>
    <p>{{ article.content }}</p>
</body>
</html>


html code for search.html

html
<!DOCTYPE html>
<html>
<head>
    <title>Newsfeed</title>
</head>
<body>
    <h1>Search</h1>
    <form action="/search" method="get">
        <input type="text" name="q">
        <input type="submit" value="Search">
    </form>
</body>
</html>
