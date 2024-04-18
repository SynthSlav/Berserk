from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb+srv://berserkroot:<berserk001>@berserkcluster.khnwedq.mongodb.net/?retryWrites=true&w=majority&appName=BerserkCluster"
    character = MongoClient("CONNECTION_STRING")
    return character['character']

if __name__ == "__main__":
    characters = get_database()