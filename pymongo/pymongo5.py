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

# Filter results using regex
myquery = { "address": { "$regex": "^8" } }
newvalues = { "$set": { "name": "Minnie Mouse" } }
result = mycol.update_many(myquery, newvalues)
print(result.modified_count, " documents updated.")

# Display records *after* update
mydoc = mycol.find(myquery)
for result in mydoc:
	print(result)

