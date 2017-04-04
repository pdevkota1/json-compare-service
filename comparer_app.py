from flask import Flask, request, jsonify, make_response, render_template
from json_comparer.dict_comparer import comparer
import json
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('json_comparer.html')


@app.route('/api/v1.0/compare_json', methods=['POST'])
def compare_json():
	print("data is %s" % request.json)
	data = request.json
	try:
		dict1 = json.loads(data["first_json"])
	except Exception as e: 
		return jsonify(error=403, text="First JSON Invalid!!"), 403
	try:
		dict2 = json.loads(data["second_json"])
	except Exception as e:
		return jsonify(error=403, text="Second json Invalid!!"), 403
	res = comparer(dict1, dict2, dict1_name="first_json", dict2_name="second_json")
	return jsonify({"diff": res})


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
