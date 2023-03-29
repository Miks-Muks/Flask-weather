from weather_app import app


@app.route('/name')
def index():
    return 'Hello world'
