#imports the Block class from block.py
from block import Block

class Blockchain:
    def __init__(self, chain=[], all_transactions = []):
      self.chain = chain
      self.all_transactions = all_transactions
      self.genesis_block()
    
    def genesis_block(self):
      newBlock = Block(self.all_transactions, 0)
      self.chain.append(newBlock)
      pass