# Second flask application devlopment

from flask import Flask, render_template
app = Flask(__name__)
app_host = '192.168.2.121'


@app.route('/<username>')
def index(username):
    return render_template('index.html', name=username)


if __name__ == '__main__':
    app.run(debug=True, host=app_host, port=80)
