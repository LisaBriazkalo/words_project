from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId
from model import *
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()
client = MongoClient("mongodb://localhost:27017/")
mydb=client.test

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Встановлюємо дозвіл на всі джерела запитів (змініть на список URL-адрес, якщо потрібно)
    allow_methods=["*"],  # Встановлюємо дозвіл на всі HTTP методи
    allow_headers=["*"],  # Встановлюємо дозвіл на всі заголовки
)

@app.get("/")
async def get():
    return mydb.list_collection_names()

@app.get("/{collection_name}")
async def getdata(collection_name):
    if(collection_name in mydb.list_collection_names()):
        print(f"Колекція '{collection_name}' існує")
        collection=mydb.get_collection(collection_name)
        return WordsEntity(collection.find())
    else:
        return {collection_name :"не існує"}
    
@app.get("/{collection_name}/{id}")
async def getone(collection_name, id):
    if(collection_name in mydb.list_collection_names()):
        collection=mydb.get_collection(collection_name)
        return WordEntity(collection.find_one({"_id":ObjectId(id)}))
    else:
        return {collection_name :"не існує"}

@app.post("/")
async def post(collection_name: Categories):
    mydb.create_collection(str(collection_name.name))
    return mydb.list_collection_names()

@app.post("/{collection_name}")
async def post(collection_name, item: Words):
    if(collection_name in mydb.list_collection_names()):
        collection=mydb.get_collection(collection_name)
        collection.insert_one(item.dict())
        return WordsEntity(collection.find())
    else:
        return {collection_name :"не існує"}

@app.put("/{collection_name}")
async def update(collection_name, new_collection_name : Categories):
    if(collection_name in mydb.list_collection_names()):
        collection=mydb.get_collection(collection_name)
        mydb[collection_name].rename(str(new_collection_name.name))
        return mydb.list_collection_names()
    else:
            return {collection_name :"не існує"}

@app.put("/{collection_name}/{id}")
async def update(collection_name, id, item: Words):
    if(collection_name in mydb.list_collection_names()):
        collection=mydb.get_collection(collection_name)
        collection.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(item)})
        return WordEntity(collection.find_one({"_id":ObjectId(id)}))
    else:
            return {collection_name :"не існує"}

@app.delete("/{collection_name}/{id}")
async def delete(collection_name, id):
    if(collection_name in mydb.list_collection_names()):
        collection=mydb.get_collection(collection_name)
        return WordEntity(collection.find_one_and_delete({"_id":ObjectId(id)}))
    else:
            return {collection_name :"не існує"}
    
@app.delete("/{collection_name}")
async def delete(collection_name):
    if(collection_name in mydb.list_collection_names()):
        collection=mydb.get_collection(collection_name)
        mydb[collection_name].drop()
        return mydb.list_collection_names()
    else:
            return {collection_name :"не існує"}

