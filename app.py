from flask import Flask, render_template


results = [
    {'name': 'John', 'age': '25'},
    {'name': 'Jane', 'age': '24'},
    {'name': 'Jack', 'age': '23'},
    {'name': 'Jill', 'age': '22'},
    {'name': 'Joe', 'age': '21'},
    {'name': 'Jenny', 'age': '20'}
]

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html', results=results)

    return app
