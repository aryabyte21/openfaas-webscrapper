from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    title = ""
    if request.method == 'POST':
        url = request.form.get('url')
        # Here you should call your OpenFaaS function with the URL
        openfaas_url = "http://localhost:8080/function/web-scraper"
        headers = {"Content-Type": "text/plain"}
        res = requests.post(openfaas_url, headers=headers, data=url)
        title = res.text
    return render_template('index.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)
