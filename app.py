from flask import Flask
import redis
import socket

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def increment():
    count = redis_client.incr('counter')
    hostname = socket.gethostname()
    return f'Hostname: {hostname}, Count: {count}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7999)
