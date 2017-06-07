from flask import Flask, request
from flask.json import jsonify


app = Flask(__name__)



@app.route('/mathop')
def api_command():
	print "inside api command function"
	#request_json = request.json
	a = request.args.get('a', 0, type=int)
	b = request.args.get('b', 0, type=int)
	ans = a + b
	return jsonify({'result':ans})

@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
