from pymongo import MongoClient
import datetime

client = MongoClient()
db = client.test_database
collection = db.test_collection



# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()}

# print(post)


# collection_posts = db.posts
# post_id = collection_posts.insert_one(post).inserted_id
# print(post_id)

# print(db.list_collection_names())
# print(db.get_collection("collection2"))
# Ciao = db.collection2.find({})
# for i in Ciao:
#     print (i)


db.collection2.update({'Country': 'Switzerland'}, { '$set': {'A Corrado le piace questo paese': True}  })

Ciao = db.collection2.find({})
for i in Ciao:
    print (i)

client.close()