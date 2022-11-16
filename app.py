from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
from routes.testRoute1 import testRoutes1
import sys
sys.path.append(".")

def app():
    web_app = Flask(__name__)
    CORS(web_app)
    
    web_app.register_blueprint(testRoutes1, url_prefix='/Testroute1')

    return web_app


app = app()

if __name__ == "__main__":
    app.run(host="localhost",debug=True)