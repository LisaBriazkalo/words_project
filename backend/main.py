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


@app.get("/get_next_word/{collection_name}/{id}")
async def getone(collection_name, id):
    if not (collection_name in mydb.list_collection_names()):
        return {collection_name :"не існує"}
    collection=mydb.get_collection(collection_name)

    if(collection.find_one({"_id":ObjectId(id)}) is None):
        return{"id error"}

    first_document = next(collection.find())
    cursor = collection.find()

    for document in cursor:
        if(document==collection.find_one({"_id":ObjectId(id)})):
            next_document=next(cursor, None)
            if(next_document is not None):
                return WordEntity(next_document)
            else: 
                return WordEntity(first_document)


@app.get("/get_previous_word/{collection_name}/{id}")
async def getone(collection_name, id):
    if not (collection_name in mydb.list_collection_names()):
        return {collection_name :"не існує"}
    collection=mydb.get_collection(collection_name)
    
    if(collection.find_one({"_id":ObjectId(id)}) is None):
        return{"id error"}

    first_document = next(collection.find())
    cursor = collection.find()
    cursor2 = collection.find()
    
    for i in cursor:
        for document in cursor2:
            next_document=next(cursor, None)
            if(next_document==collection.find_one({"_id":ObjectId(id)})):
                print(next_document)
                print()
                return WordEntity(document)
            if(next_document is None and first_document==collection.find_one({"_id":ObjectId(id)})):
                print(next_document)
                print(collection.find_one({"_id":ObjectId(id)}))
                return WordEntity(document)
      

@app.get("/getTest_word_translate/{collection_name}")
async def getone(collection_name):
    if not (collection_name in mydb.list_collection_names()):
        return {collection_name :"не існує"}

    collection=mydb.get_collection(collection_name)

    arr=[]
    for i in range(10):
        arr.append(getFourWordsForTest("Word_Translate", collection))
    return arr


@app.get("/getTest_translate_word/{collection_name}")
async def getone(collection_name):
    if not (collection_name in mydb.list_collection_names()):
        return {collection_name :"не існує"}

    collection=mydb.get_collection(collection_name)

    arr=[]
    for i in range(10):
        arr.append(getFourWordsForTest("Translate_Word", collection))
    return arr


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


@app.post("/check_result/{collection_name}")
async def post(collection_name, test: Test):
    if not (collection_name in mydb.list_collection_names()):
        return {collection_name :"не існує"}
    
    collection=mydb.get_collection(collection_name)
    score=0
    faile=0
    passed=0
    size=10

    for question in test.questions:
        if(question.answer==None):
            passed+=1
        elif(isRightTranslate(collection, question.word, question.answer)):
            score+=1
        elif(isRightTranslate(collection, question.word, question.answer)==False):
            faile+=1
    precision=score/size
    return {
        "size": size,
        "score": score,
        "faile": faile,
        "passed": passed,
        "precision": precision
    }   


@app.post("/check_word/{collection_name}")
async def post(collection_name, question: Question):
    if not (collection_name in mydb.list_collection_names()):
        return {collection_name :"не існує"}
    
    collection=mydb.get_collection(collection_name)
    return isRightTranslate(collection, question.word, question.answer)


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

