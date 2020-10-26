import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
	print("'mydatabase' found in MongoDB!")

# Create a collection ("table")
mycol = mydb["customer"]

collist = mydb.list_collection_names()
print(collist)
if "customer" in collist:
	print("'customer' collection found in 'mydatabase'!")

mylist = [
	{ "_id": 1, "name": "Amy", "address": "873 Oak Street" },
	{ "_id": 2, "name": "Brad", "address": "321 Ivy Road" },
	{ "_id": 3, "name": "Colleen", "address": "473 Valley Blvd" },
	{ "_id": 4, "name": "Dave", "address": "229 East 23rd Ave" }
]
result = mycol.insert_many(mylist)
print(result)
print(result.inserted_ids)

