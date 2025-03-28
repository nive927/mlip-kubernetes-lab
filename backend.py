# backend.py
from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def hello_user():
    user_id = request.args.get("user_id", "Guest")
    instance = socket.gethostname()
    
    # TODO: Add a unique message or identifier to distinguish responses from different backend instances.
    # For example, you can include the instance name in the response.   
    
    return f"Hello, {user_id}! This response is from instance: {instance}" #Use the above defined instance here 

if __name__ == '__main__':
    # TODO: Change the port if needed (default is 5001)
    app.run(host='0.0.0.0', port=5001)
