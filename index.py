from flask import Flask, request, url_for, make_response, after_this_request, json

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return 'hello world, %s' % user_agent


@app.route("/static/<string:path>")
def get_request_path(path):
    return path


@app.route("/static/<path:b>.html")
def get_static_file(b):
    return b


@app.route('/aab')
def r():
    @after_this_request
    def add_header(res):
        res.headers['Content-Type'] = 'text/plain'
        return res

    return json.jsonify(status=0)


@app.errorhandler(404)
def errorhandler(error):
    return json.jsonify(code=40404)


if '__main__' == __name__:
    app.run(debug=True)
