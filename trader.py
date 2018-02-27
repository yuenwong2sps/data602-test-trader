import time
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    localtime = time.asctime( time.localtime(time.time()) )
    return "My local time:" + localtime

if __name__ == "__main__":
    app.run(host='0.0.0.0') # host='0.0.0.0' needed for docker
	

