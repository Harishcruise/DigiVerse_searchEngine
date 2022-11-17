from flask import jsonify, request, Blueprint
from MongoConfig.config import client, db , user_collection
from gridfs import GridFS


testRoutes1 = Blueprint('TestRoute1', __name__)
fs = GridFS(db)


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

file_location = "routes\dummy.txt"
@testRoutes1.route('/postFile', methods=['GET'])
def postFile():
    with open(file_location, 'rb') as f:
        contents = f.read()
    fs.put(contents,filename="app")
    return contents 





