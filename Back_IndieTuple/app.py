from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello')
def hello():
  return jsonify({'message': 'Hello, Indie Tuple!'})

if __name__ == '__main__':
  app.run(debug=True)