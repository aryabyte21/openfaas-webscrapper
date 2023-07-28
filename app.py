from flask import Flask, render_template, request
import requests
from mongo_setup import create_mongo_client, create_database, create_collection

app = Flask(__name__)

# Setup MongoDB
client = create_mongo_client()
db = create_database(client, 'web_scraper_db')
collection = create_collection(db, 'scraped_pages')

@app.route('/', methods=['GET', 'POST'])
def home():
    title = ""
    if request.method == 'POST':
        url = request.form.get('url')
        openfaas_url = "http://localhost:8080/function/web-scraper"
        headers = {"Content-Type": "text/plain"}
        res = requests.post(openfaas_url, headers=headers, data=url)
        title = res.text

        data = {"url": url, "title": title}
        collection.insert_one(data)

    return render_template('index.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)
