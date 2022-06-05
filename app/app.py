from flask import Flask,render_template
from dotenv import load_dotenv
import os
import socket

load_dotenv()
app = Flask(__name__)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html')
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
