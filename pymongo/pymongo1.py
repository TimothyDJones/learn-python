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

mydict = { "name": "John", "address": "123 My Street" }
result = mycol.insert_one(mydict)
print(result)
print(result.inserted_id)

mydict = { "name": "Peter", "address": "456 Another Road" }
result = mycol.insert_one(mydict)
print(result)
print(result.inserted_id)
