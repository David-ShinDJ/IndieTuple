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
        nickname = data.get('nickname')
        
        if score >= 10:
            token = jwt.encode(
                {
                    'score': score,
                    'nickname': nickname,
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

@app.route('/api/verify-token', methods=['POST'])
def verify_token():
    try:
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "No token provided"}), 401
            
        # Bearer 토큰에서 실제 토큰 부분만 추출
        token = token.split(' ')[1]
        
        # 토큰 검증
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({
            "valid": True,
            "nickname": decoded['nickname'],
            "score": decoded['score']
        })
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

@app.route('/api/get-nickname', methods=['POST'])
def get_nickname():
    try:
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "No token provided"}), 401
            
        # Bearer 토큰에서 실제 토큰 부분만 추출
        token = token.split(' ')[1]
        
        # 토큰 검증 및 닉네임 추출
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({
            "nickname": decoded['nickname']
        })
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

if __name__ == '__main__':
    app.run(debug=True)


