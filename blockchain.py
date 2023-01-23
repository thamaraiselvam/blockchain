from time import time
from uuid import uuid4
from flask import Flask, jsonify, request
import hashlib
import json
import os

class Blockchain(object):
    def __init__(self):
        # Maintain chain state
        self.chain = []
        # Holds transactions for each block
        self.current_transactions = []
        # Represents all connected nodes
        self.nodes = set()

    def new_block(self, proof, previous_hash=None):
        # Creates a new Block and adds it to the chain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        # Adds a new transaction to the list of transactions
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hashes a Block
        block_string = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

app = Flask(__name__)

# Generate a globally unique address for this node
node_identfier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

if __name__ == '__main__':
    port = os.environ.get('PORT')
    print(port)
    app.run(host='0.0.0.0', port=port)