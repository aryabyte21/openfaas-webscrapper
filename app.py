from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        schedule = request.form.get('schedule')
        # Here you should call your OpenFaaS function with the URL and the schedule.
        # We'll add this later.
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
