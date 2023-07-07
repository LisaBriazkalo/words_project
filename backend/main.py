from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId
from model import *
from fastapi.middleware.cors import CORSMiddleware
import random


app=FastAPI()
client = MongoClient("mongodb://localhost:27017/")
mydb=client.test

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_collections_names")
async def get():
    return mydb.list_collection_names()

@app.get("/get_words_from_collection/{collection_name}")
async def getdata(collection_name):
    if not (collection_name in mydb.list_collection_names()):
        return {collection_name :"не існує"}
    collection=mydb.get_collection(collection_name)
    return WordsEntity(collection.find())
        
    
@app.get("/get_word_details/{collection_name}/{id}")
async def getone(collection_name, id):
    if not (collection_name in mydb.list_collection_names()):
        return {collection_name :"не існує"}
    collection=mydb.get_collection(collection_name)
    return WordEntity(collection.find_one({"_id":ObjectId(id)}))
        
    
@app.get("/fourWords/{collection_name}")
async def getone(collection_name):
    if not (collection_name in mydb.list_collection_names()):
        return {collection_name :"не існує"}

    collection=mydb.get_collection(collection_name)

    size=collection.estimated_document_count()
    trueWord=random.randint(0, size-1)
    i=0
    for document in collection.find():
        if(i==trueWord):
            trueWord=document
            break
        i+=1
    
    arr = random.sample([x for x in range(0, size) if x != i], 3)
    arr.sort()
    i=0
    j=0
    for document in collection.find():
        if(j!=3 and i==arr[j]):
            arr[j]=document
            j+=1
        i+=1
    return fourWordsEntity(trueWord, arr)
        

@app.post("/post_new_category")
async def post(collection_name: Categories):
    mydb.create_collection(str(collection_name.name))
    return mydb.list_collection_names()


@app.post("/post_new_word/{collection_name}")
async def post(collection_name, item: Words):
    if not (collection_name in mydb.list_collection_names()):
        return {collection_name :"не існує"}

    collection=mydb.get_collection(collection_name)
    collection.insert_one(item.dict())
    return WordsEntity(collection.find())
        

@app.put("/update_collection_name/{collection_name}")
async def update(collection_name, new_collection_name : Categories):
    if not (collection_name in mydb.list_collection_names()):
        return {collection_name :"не існує"}

    mydb[collection_name].rename(str(new_collection_name.name))
    return mydb.list_collection_names()
            

@app.put("/update_word/{collection_name}/{id}")
async def update(collection_name, id, item: Words):
    if not (collection_name in mydb.list_collection_names()):
        return {collection_name :"не існує"}

    collection=mydb.get_collection(collection_name)
    collection.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(item)})
    return WordEntity(collection.find_one({"_id":ObjectId(id)}))
            

@app.delete("/delete_word/{collection_name}/{id}")
async def delete(collection_name, id):
    if not (collection_name in mydb.list_collection_names()):
        return {collection_name :"не існує"}
    
    collection=mydb.get_collection(collection_name)
    return WordEntity(collection.find_one_and_delete({"_id":ObjectId(id)}))
            
    
@app.delete("/delete_collection/{collection_name}")
async def delete(collection_name):
    if not (collection_name in mydb.list_collection_names()):
        return {collection_name :"не існує"}
    collection=mydb.get_collection(collection_name)
    mydb[collection_name].drop()
    return mydb.list_collection_names()            

