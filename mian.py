from flask import Flask, request, render_template
import requests as r
from bs4 import BeautifulSoup as bf

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/sub', methods=['POST'])
def sub():
    try:
        if request.method == 'POST':
            url = request.form['link']
            links = find_url(url)
            return render_template('show.html', links=links)
    except Exception as e:
        return f'Eroor: {e}'

def find_url(url):
    response = r.get(url)

    soup = bf(response.text, 'html.parser')

    a_tags = soup.find_all('a')

    links = []

    for a_tag in a_tags:
        href = a_tag.get('href')
        if not url == href:
            links.append(href)

    return links

if __name__ == '__main__':
    app.run(debug=True)
