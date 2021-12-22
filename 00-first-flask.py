# first flask application


from flask import Flask, request
import socket
import flask
app = Flask(__name__)

app_host = '192.168.2.121'


@app.route('/')

def welcome():
    '''First web page!!!'''
    return '<html><body>First flask web framework ! Less go !!!!</body></html>'


@app.route('/gethostname')
def list_view():
    '''Get hostname'''
    return socket.gethostname()


@app.route('/version')
def viewFlaskVersion():
    '''Display flask version'''
    return 'Flask {version} run is {hostname}'.format(version=flask.__version__, hostname=list_view())


if __name__ == '__main__':
    app.run(debug=True, port=80, host=app_host)
