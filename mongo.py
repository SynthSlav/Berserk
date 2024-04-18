import os
import pymongo
if os.path.exists("env.py"):
    import env 
app = pymongo(__name__)


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "berserkroot"
COLLECTION = "test.characters"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

documents = coll.find()

for doc in documents:
    print(doc)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=os.environ.get("PORT", "3000"),
        debug=True)
