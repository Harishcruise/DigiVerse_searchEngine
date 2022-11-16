from flask import jsonify, request, Blueprint
from MongoConfig.config import user_collection

testRoutes1 = Blueprint('TestRoute1', __name__)

@testRoutes1.route('/test1', methods=['GET'])
def test1():
        print("hello1")
        return "hello1"


@testRoutes1.route('/postTest1', methods=['POST'])
def postTest1():
        resp = {}
        try:
            req_body = request.json
            user_collection.insert_one(req_body)            
            print("User Data Stored Successfully in the Database.")
            status = {
                "statusCode":"200",
                "statusMessage":"Successful."
            }
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)
            }
        resp["status"] =status
        return resp

