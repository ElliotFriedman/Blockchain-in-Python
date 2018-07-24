from chain import Blockchain
from block import Block



chain = Blockchain()
chain.create_genesis_block()

#chain.add_block(Block(2, 300, 1230, "na"))
chain.print_chain()

chain.add_tx("Hi")
print("mine returned", chain.mine())
chain.print_chain()
