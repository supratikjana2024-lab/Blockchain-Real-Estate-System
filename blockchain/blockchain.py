from .block import Block

class Blockchain:

    def __init__(self):

        self.chain=[]
        self.create_genesis()

    def create_genesis(self):

        genesis=Block(0,{"action":"genesis"},"0")
        self.chain.append(genesis)

    def latest_block(self):

        return self.chain[-1]

    def add_block(self,transaction):

        prev=self.latest_block()

        block=Block(

        len(self.chain),
        transaction,
        prev.hash

        )

        self.chain.append(block)

        return block