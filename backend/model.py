from typing import Union
from pydantic import BaseModel
import random

class Categories(BaseModel): 
    name : str

class Words(BaseModel): 
    word : str
    translate : str
    example : str   

class Question(BaseModel): 
    word: str
    answer: Union[str, None]
    option1: str
    option2: str
    option3: str
    option4: str    

class Test(BaseModel):
    questions: list[Question]

def WordEntity(word) -> dict:
    return{
        "id" : str(word["_id"]),
        "word" : word["word"],
        "translate" : word["translate"],
        "example" : word["example"]
    }

def WordsEntity(entity) -> list:
    return[WordEntity(item) for item in entity]

def fourWordsEntity_Word_Translate(trueWord, words:list) ->dict:
    arr = random.sample(range(0, 4), 4)
    for i in range(4):
        if(arr[i]==0):
            arr[i]=trueWord["translate"]
        elif(arr[i]==1):
            arr[i]=words[0]["translate"]
        elif(arr[i]==2):
            arr[i]=words[1]["translate"]
        elif(arr[i]==3):
            arr[i]=words[2]["translate"]
        i+=1
    return{
        "word": trueWord["word"],
        "answer": None,
        "option1": arr[0],
        "option2": arr[1],
        "option3": arr[2],
        "option4": arr[3]
    }

def fourWordsEntity_Translate_Word(trueWord, words:list) ->dict:
    arr = random.sample(range(0, 4), 4)
    for i in range(4):
        if(arr[i]==0):
            arr[i]=trueWord["word"]
        elif(arr[i]==1):
            arr[i]=words[0]["word"]
        elif(arr[i]==2):
            arr[i]=words[1]["word"]
        elif(arr[i]==3):
            arr[i]=words[2]["word"]
        i+=1
    return{
        "word": trueWord["translate"],
        "answer": None,
        "option1": arr[0],
        "option2": arr[1],
        "option3": arr[2],
        "option4": arr[3]
    }


def getFourWordsForTest(value, collection):
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
    if(value=="Word_Translate"):
        return fourWordsEntity_Word_Translate(trueWord, arr)
    if(value=="Translate_Word"):
        return fourWordsEntity_Translate_Word(trueWord, arr)

def isRightTranslate(collection, word_value, translate_value):
    w=collection.find_one({"word": word_value})
    if(w is not None):
        if (translate_value==w.get("translate")):
            return True
        return False
    w=collection.find_one({"translate": word_value})
    if (translate_value==w.get("word")):
        return True
    return False
