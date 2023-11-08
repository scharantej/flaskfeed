 
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/news', methods=['POST'])
def news():
  # Get the search query from the user.
  query = request.form.get('query')

  # Make a request to the news API.
  response = requests.get('https://newsapi.org/v2/top-headlines?q={}&apiKey=YOUR_API_KEY'.format(query))

  # Parse the JSON response.
  data = response.json()

  # Extract the articles from the JSON response.
  articles = data['articles']

  # Render the news template with the articles.
  return render_template('news.html', articles=articles)

if __name__ == '__main__':
  app.run()
