from pydantic import BaseModel
import random

class Categories(BaseModel): 
    name : str

class Words(BaseModel): 
    word : str
    translate : str
    example : str      

def WordEntity(word) -> dict:
    return{
        "id" : str(word["_id"]),
        "word" : word["word"],
        "translate" : word["translate"],
        "example" : word["example"]
    }

def WordsEntity(entity) -> list:
    return[WordEntity(item) for item in entity]

def fourWordsEntity(trueWord, words:list) ->dict:
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
        "translate0": arr[0],
        "translate1": arr[1],
        "translate2": arr[2],
        "translate3": arr[3]
    }