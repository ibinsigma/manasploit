from flask import Flask, request, jsonify
from flask_cors import CORS
from serve import get_model_api

app = Flask(__name__)
CORS(app)
model_api = get_model_api()

@app.route('/')
def index():
	return "Index API"

@app.errorhandler(404)
def url_error(e):
	return """
	Wrong URL!
	<pre>{}</pre>""".format(e), 404

@app.errorhandler(500)
def server_error(e):
	return """
	An internal error occured: <pre>{}</pre>
	See logs for full stacktrace.
	""".format(e), 500

@app.route('/api', methods=['POST'])
def api():
	input_data = request.json
	prediction = model_api(input_data)
	response = jsonify(prediction)
	return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)