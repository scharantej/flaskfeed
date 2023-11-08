 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    articles = [
        {
            'title': 'Article 1',
            'content': 'This is the content of article 1.'
        },
        {
            'title': 'Article 2',
            'content': 'This is the content of article 2.'
        },
        {
            'title': 'Article 3',
            'content': 'This is the content of article 3.'
        }
    ]
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    articles = [
        {
            'title': 'Article 1',
            'content': 'This is the content of article 1.'
        },
        {
            'title': 'Article 2',
            'content': 'This is the content of article 2.'
        },
        {
            'title': 'Article 3',
            'content': 'This is the content of article 3.'
        }
    ]
    article = articles[article_id]
    return render_template('article.html', article=article)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        keyword = request.form['keyword']
        articles = [
            {
                'title': 'Article 1',
                'content': 'This is the content of article 1.'
            },
            {
                'title': 'Article 2',
                'content': 'This is the content of article 2.'
            },
            {
                'title': 'Article 3',
                'content': 'This is the content of article 3.'
            }
        ]
        articles = [article for article in articles if keyword in article['title']]
        return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
