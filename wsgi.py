from flask import Flask, render_template, redirect, request as req, json
from flask_bootstrap import Bootstrap
import requests as r
from weather_app.forms import SearchForm

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'qfegy235q643ehsG'
Bootstrap(app)

API_KEY = '79d58935cdcd4342a5f141825230104'


@app.route('/')
def main():
    form = SearchForm()
    return render_template('main/index.html', form=form)


@app.route('/search', methods=['POST'])
def search():
    BASE_URL = 'http://api.weatherapi.com/v1/current.json?key=79d58935cdcd4342a5f141825230104'
    if req.method == 'POST':
        name = req.form.get('name')
        BASE_URL = 'http://api.weatherapi.com/v1/current.json?key=79d58935cdcd4342a5f141825230104&q={name}'
        response = r.get(url=BASE_URL)
        return render_template('main/weather_get.html', data=response)


if __name__ == '__main__':
    app.run(debug=True)
