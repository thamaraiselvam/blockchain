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
        pass

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
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]
