from hashlib import sha256
from block import Block
import json
import time

class Blockchain:
	difficulty = 4 

	def __init__(self):
		self.unconfirmed_transactions = []
		self.chain = []
		self.len = 1
		self.create_genesis_block()
	
	#create a genesis block and push it onto the chain
	def create_genesis_block(self):
		assert(self.len == 1), "Can only create a genesis block there are no blocks"
		genesis_block = Block(0, 0, 10, 0)
		genesis_block.hash = genesis_block.compute_hash()
		self.chain.append(genesis_block)

	@property
	def last_block(self):
		return self.chain[self.len - 1]



	def add_tx(self, data):
		self.unconfirmed_transactions.append(data)

	#add a block to the chain
	def add_block(self, block, proof):
		#print("appending block with hash: ", block.compute_hash())
		previous_hash = self.last_block.hash

		if previous_hash != block.previous_hash:
			print("add block returned false, previous hash issue")
			return False

		block.hash = proof
		self.len += 1
		self.chain.append(block)
		self.chain[self.len - 1].set_index(self.len - 1)
		self.chain[self.len - 1].hash = block.compute_hash()
		print("block successfully added")

	def is_valid_proof(self, block, block_hash):
		return (block_hash.startswith('0' * Blockchain.difficulty) and block_hash == block.compute_hash())

	def print_block(self, index):
		if index < len(self.chain) and index >= 0:
			print("Block at index", index, "has a hash of: ", self.chain[index])
		else:
			print("There are currently", len(self.chain), "blocks. Index ", index, "is out of bounds")

	def print_chain(self):
		if self.len > 0:
			print("\nChain Length:", self.len, "\n")
			i = 0
			while i < self.len:
				print("Block: ", self.chain[i].get_index(), "has hash:", self.chain[i].hash)
				i += 1
	
		else:
			print("There are currently no blocks in the blockchain, add the genesis block", end="")
			print("then try printing again")

	def proof_of_work(self, block):
		block.nonce = 0
		computed_hash = block.compute_hash()
		while not computed_hash.startswith('0' * Blockchain.difficulty):
			block.nonce += 1
			computed_hash = block.compute_hash()
		return computed_hash

	def mine(self):
		
		if not self.unconfirmed_transactions:
			return False

		last_block = self.last_block
		new_block = Block(index=last_block.index + 1, transactions=self.unconfirmed_transactions,
				timestamp = time.time(), previous_hash=last_block.hash)

		proof = self.proof_of_work(new_block)
		self.add_block(new_block, proof)
		self.unconfirmed_transactions = []
		return new_block.index


