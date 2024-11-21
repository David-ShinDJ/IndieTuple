from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask import Flask, request, jsonify
app = Flask(__name__)

# Database
todos : list[dict[str, any]] = [
      {'id': 1, 'text': 'Reflex 배우기', 'completed': False},
    {'id': 2, 'text': 'IndieTuple 개발하기', 'completed': False},
    {'id': 3, 'text': "데이터 베이스 공부하기", 'completed': False}
]


def db_add_todo(text: str):
    new_todo = {'id': len(todos) + 1, 'text': text, 'completed': False}
    todos.append(new_todo)
    return True

def read_todos():
    return todos

def find_todo(text: str):
    for todo in todos:
        if todo['text'] == text:
            return todo
    return None

def db_update_todo(text: str):
    for todo in todos:
        if todo['text'] == text:
            todo['completed'] = not todo['completed']
            return True
    return False

def db_delete_todo(text: str):
    index = next((index for index, todo in enumerate(todos) if todo['text'] == text), None)
    if index is not None:
        todos.pop(index)
        return True
    return False

# 데이터 로드 
@app.route("/api/todos", methods=["GET"])
def get_todos():
    todos = read_todos()
    return jsonify(todos)

## text 조회
# @app.route("api/todos/get/<str:text>", methods=["GET"])
# def get_todo(text):
#     return jsonify()

@app.route("/api/todos/add", methods=["POST"])
def add_todo():
    data = request.get_json()
    db_add_todo(data['text'])
    return jsonify({'message': 'Todo added!'}), 201

@app.route("/api/todos/update", methods=["PUT"])
def update_todo():
    data = request.get_json()
    text = data["text"]
    print(text)
    db_update_todo(text)
    return jsonify({"message": "Todo updated!"}), 200

@app.route('/api/todos/delete/<string:text>', methods=["DELETE"])
def delete_todo(text):
    db_delete_todo(text)
    return jsonify({'message': 'Todo deleted!'})

if __name__ == "__main__":
    app.run(debug=True)


# 데이터 로드
