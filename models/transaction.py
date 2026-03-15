from pydantic import BaseModel

class Transaction(BaseModel):

    property_id:str
    seller:str
    buyer:str
    price:float