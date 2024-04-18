from pymongo.mongo_client import MongoClient
from flask import Flask, render_template, request, url_for, redirect

# Replace the placeholder with your Atlas connection string
uri = "mongodb+srv://BerserkBobi:basedgod001@berserkcluster.khnwedq.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

print(client.list_database_names())

db = client.test

print(db.list_collection_names)

areas1 =     {
        "name": "Abyss",
        "img_url": "https://berserk.fandom.com/wiki/Abyss?file=Abyss.jpg",
        "description": "The Abyss (深淵 Shin'en) is the deepest level of the Astral World. It is called 'Hell' by some.The Abyss is the home of the Idea of Evil. It has a vortex of souls, described by Puck as 'an endless swirl of consciousness' that feels 'as if all the evil in the world were gathered there'. "
    }

area = db.area

#result = area.insert_one(areas1)

areas2 =    {
    
        "name": "Kushan",
        "img_url": "https://berserk.fandom.com/wiki/Kushan_Empire?file=27-05-002.jpg",
        "description": "Kushan is a large empire ruled by Emperor Ganishka. The empire is located to the far east of the Holy See nations. It is not a monolithic empire - rather, it comprises a royal house over lesser ones. This led to grudges between them. "
    },  
{
        "name": "Abyss",
        "img_url": "https://berserk.fandom.com/wiki/Abyss?file=Abyss.jpg",
        "description": "The Abyss (深淵 Shin'en) is the deepest level of the Astral World. It is called 'Hell' by some.The Abyss is the home of the Idea of Evil. It has a vortex of souls, described by Puck as 'an endless swirl of consciousness' that feels 'as if all the evil in the world were gathered there'. "
    }

#result = area.insert_many(areas2)

print(area.count_documents({}))
