from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap

from weather_app.forms import SearchForm

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'qfegy235q643ehsG'
Bootstrap(app)


@app.route('/')
def main():
    form = SearchForm()
    return render_template('main/index.html', **{'form': form})


@app.route('/search')
def search():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
