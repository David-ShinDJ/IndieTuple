from flask import Flask, jsonify
from flask_socketio import SocketIO

# backend/app.py (Flask)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/todos', methods=['GET'])
def get_todos():
  todos = [
    {'id': 1, 'text': 'Reflex 배우기', 'completed': True},
    {'id': 2, 'text': 'IndieTuple 개발하기', 'completed': False}
  ]
  return jsonify(todos)

if __name__ == '__main__':
  app.run(debug=True)