from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from blockchain.blockchain import Blockchain
from database.db import conn,cursor
from models.transaction import Transaction

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chain=Blockchain()


@app.get("/")
def home():
    return {"message":"Blockchain Real Estate API"}


@app.post("/register-property")
def register_property(property_id:str,owner:str,location:str):

    cursor.execute(
    "INSERT OR REPLACE INTO properties VALUES(?,?,?)",
    (property_id,owner,location)
    )

    conn.commit()

    block=chain.add_block({
    "action":"REGISTER",
    "property_id":property_id,
    "owner":owner,
    "location":location
    })

    return {"message":"Property Registered","block":block.index}


@app.get("/property/{pid}")
def get_property(pid:str):

    cursor.execute(
    "SELECT * FROM properties WHERE property_id=?",
    (pid,)
    )

    data=cursor.fetchone()

    if data is None:
        return {"error":"Property not found"}

    return {
        "property_id":data[0],
        "owner":data[1],
        "location":data[2]
    }


@app.post("/transfer-property")
def transfer(tx:Transaction):

    cursor.execute(
    "SELECT owner FROM properties WHERE property_id=?",
    (tx.property_id,)
    )

    result=cursor.fetchone()

    if result is None:
        return {"error":"Property not found"}

    if result[0]!=tx.seller:
        return {"error":"Seller not owner"}

    cursor.execute(
    "UPDATE properties SET owner=? WHERE property_id=?",
    (tx.buyer,tx.property_id)
    )

    conn.commit()

    block=chain.add_block({
    "action":"TRANSFER",
    "property_id":tx.property_id,
    "seller":tx.seller,
    "buyer":tx.buyer,
    "price":tx.price
    })

    return {"message":"Transfer successful","block":block.index}


@app.get("/chain")
def chain_view():

    blocks=[]

    for block in chain.chain:

        blocks.append(block.__dict__)

    return blocks