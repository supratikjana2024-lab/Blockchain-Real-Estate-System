import hashlib
import json
import time

class Block:

    def __init__(self,index,transaction,previous_hash):

        self.index=index
        self.timestamp=time.time()
        self.transaction=transaction
        self.previous_hash=previous_hash
        self.hash=self.calculate_hash()

    def calculate_hash(self):

        data=json.dumps({

        "index":self.index,
        "timestamp":self.timestamp,
        "transaction":self.transaction,
        "previous_hash":self.previous_hash

        },sort_keys=True)

        return hashlib.sha256(data.encode()).hexdigest()