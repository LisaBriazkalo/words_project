from pydantic import BaseModel


class Categories(BaseModel): 
    name : str

class Words(BaseModel): 
    word : str
    translate : str
    example : str

def CategoryEntity(category) -> dict:
    return {"name" : category["name"]}

def CategoriesEntity(entity) -> list:
    return[CategoryEntity(category) for category in entity]        

def WordEntity(word) -> dict:
    return{
        "id" : str(word["_id"]),
        "word" : word["word"],
        "translate" : word["translate"],
        "example" : word["example"]
    }

def WordsEntity(entity) -> list:
    return[WordEntity(item) for item in entity]