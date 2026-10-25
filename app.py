
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    
    <p>This application is deployed using a Platform as a Service.</p>
    """
