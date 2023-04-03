from flask import Flask, render_template, redirect, request, json, flash
from flask_bootstrap import Bootstrap
import requests as r
from weather_app.forms import SearchForm

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'qfegy235q643ehsG'
Bootstrap(app)

API_KEY = '79d58935cdcd4342a5f141825230104'


@app.route('/', methods=['POST', 'GET'])
def main():
    form = SearchForm()
    return render_template('main/index.html', form=form)


@app.route('/search', methods=['POST', 'GET'])
def search():
    name = request.form['name']
    if name:
        BASE_URL = f'http://api.weatherapi.com/v1/current.json?key=79d58935cdcd4342a5f141825230104&q={name}&aqi=no'
        response = r.get(url=BASE_URL)
        data = json.loads(response.text)
        return render_template('main/weather_get.html', data=data)

    else:
        return render_template('main/index.html', error='badd')


if __name__ == '__main__':
    app.run(debug=True)
