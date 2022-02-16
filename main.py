from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='index')


@app.route('/result')
def result():
    return render_template('result.html', name='result')


if __name__ == '__main__':
    app.run(debug=True)
