from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

todos = [
    { "label": "Sample", "done": True }
]

some_data = { "name": "Bobby", "lastname": "Rixer" }


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    
    if "label" in request_body and "done" in request_body:
        todos.append(request_body)
    else:
        return jsonify({"error": "Missing 'label' or 'done' in request"}), 400

    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):

    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 400

    todos.pop(position)

    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)