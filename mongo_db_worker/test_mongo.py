from pymongo import MongoClient
import datetime
import pprint

client = MongoClient("mongodb://admin:VRuAd2Nvmp4ELHh5@localhost:27017/")
db = client["test-database"]
collection = db["test-collection"]

post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
pprint.pprint(posts.find_one())

