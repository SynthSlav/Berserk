import pymongo
import pprint
import json
import warnings
import Flask
import os
warnings.filterwarnings('ignore')
app = Flask(__name__)

client = pymongo.MongoClient('mongodb://localhost:27017')

db_objects = client['objects']

db_objects.create_collection('objects')

objects_collection = db_objects.get_collection('objects')

with open('obj.json') as f:
    obj_data = json.load(f)
objects_collection.insert_many(obj_data)





if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=os.environ.get("PORT", "3000"),
        debug=True)