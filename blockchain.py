class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()

    def new_block(self, proof, previous_hash=None):
        # Creates a new Block and adds it to the chain
        pass

    def new_transaction(self, sender, recipient, amount):
        # Adds a new transaction to the list of transactions
        pass

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass
