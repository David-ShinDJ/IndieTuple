from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask import Flask, request, jsonify
app = Flask(__name__)

# Database

# 데이터 로드 
@app.route("/api/todos", methods=["GET"])
def get_todos():
    todos = read_todos()
    return jsonify(todos)


if __name__ == "__main__":
    app.run(debug=True)

# 데이터 로드
