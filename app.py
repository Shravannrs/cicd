from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__name__':
    app.run()

app.run(port=5000)