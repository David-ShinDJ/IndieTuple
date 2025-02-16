# Flask 서버
from flask import Flask, jsonify, request
from flask_cors import CORS
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'your-secret-key'  # 실제 운영시에는 환경변수로 관리

@app.route('/api/token', methods=['POST'])
def generate_token():
    try:
        data = request.get_json()
        score = data.get('score', 0)
        
        if score >= 10:
            token = jwt.encode(
                {
                    'score': score,
                    'timestamp': str(datetime.utcnow()),
                    'exp': datetime.utcnow() + timedelta(hours=1)
                },
                app.config['SECRET_KEY'],
                algorithm='HS256'
            )
            return jsonify({"token": token})
        else:
            return jsonify({"error": "Score not high enough"}), 400
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


