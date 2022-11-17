from flask_pymongo import pymongo



connection_str = "mongodb://HarishCruise:Jamestay007@ac-dpeivug-shard-00-00.ynv4qtm.mongodb.net:27017,ac-dpeivug-shard-00-01.ynv4qtm.mongodb.net:27017,ac-dpeivug-shard-00-02.ynv4qtm.mongodb.net:27017/?ssl=true&replicaSet=atlas-ec6i31-shard-0&authSource=admin&retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_str)
db = client.get_database('DigiVerse_DB')
user_collection = pymongo.collection.Collection(db, 'TestingInstance')

