from chain import Blockchain
from block import Block



chain = Blockchain()
chain.create_genesis_block()
n = Block(1, 222, 3, 1)

chain.add_block(n)
chain.add_block(Block(2, 300, 1230, "na"))
chain.print_chain()


