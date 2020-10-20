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

# Find the *first* record in collection
result = mycol.find_one()
print(result)

# Find *ALL* results in collection
for result in mycol.find():
	print(result)

# Suppress display of the "_id" field
for result in mycol.find({}, { "_id": 0, "name": 1, "address": 1 }):
	print(result)

# Suppress display of the "address" field
for result in mycol.find({}, { "address": 0 }):
	print(result)

# Filter results using regex
myquery = { "address": { "$regex": "^8" } }
for result in mycol.find(myquery):
	print(result)

# Sort by name in *descending* order (all results)
mydoc = mycol.find().sort("name", -1)
for result in mydoc:
	print(result)

