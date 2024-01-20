from flask import Flask, jsonify
import redis
import socket

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def increment():
    count = redis_client.incr('counter')
    hostname = socket.gethostname()
    return f'Hostname: {hostname}, Count: {count}'

@app.route('/health')
def health_check():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7999)
