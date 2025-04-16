import datetime
import hashlib

def create_block(data, blockNo=0, previousHash=0x0, nonce=0, next_block=None):
    return {
        'blockNo': blockNo,
        'data': data,
        'next': next_block,
        'hash': None,
        'nonce': nonce,
        'previousHash': previousHash,
        'timestamp': datetime.datetime.now()
    }

def compute_hash(block):
    h = hashlib.sha256()
    h.update(
        str(block['blockNo']).encode("utf-8")
        + str(block['data']).encode("utf-8")
        + str(block['next']).encode("utf-8")
        + str(block['hash']).encode("utf-8")
        + str(block['nonce']).encode("utf-8")
        + str(block['previousHash']).encode("utf-8")
        + str(block['timestamp']).encode("utf-8")
    )
    return h.hexdigest()

def block_to_string(block):
    return f"Block hash {str(compute_hash(block))} \nBlockNo {str(block['blockNo'])} \nBlock data {str(block['data'])} \nNonce {str(block['nonce'])} \n ----------------"

def create_blockchain():
    diff = 20
    maxNonce = 2**32
    target = 2 ** (256 - diff)
    genesis_block = create_block("genesis")
    return {
        'diff': diff,
        'maxNonce': maxNonce,
        'target': target,
        'block': genesis_block,
        'head': genesis_block
    }

def add_block(blockchain, block):
    block['previousHash'] = compute_hash(blockchain['block'])
    block['blockNo'] = blockchain['block']['blockNo'] + 1
    blockchain['block']['next'] = block
    blockchain['block'] = block

def mine_block(blockchain, block):
    for n in range(blockchain['maxNonce']):
        if int(compute_hash(block), 16) <= blockchain['target']:
            add_block(blockchain, block)
            print(block_to_string(block))
            break
        else:
            block['nonce'] += 1

def validate_transaction(transaction):
    # Example validation logic for a transaction
    if 'sender' not in transaction or 'receiver' not in transaction or 'amount' not in transaction:
        return False
    if transaction['amount'] <= 0:
        return False
    return True

def create_block_with_transaction(transaction, blockNo=0, previousHash=0x0, nonce=0, next_block=None):
    if not validate_transaction(transaction):
        raise ValueError("Invalid transaction")
    return create_block(transaction, blockNo, previousHash, nonce, next_block)

blockchain = create_blockchain()
for n in range(5):
    mine_block(blockchain, create_block("Block " + str(n + 1)))
    print(blockchain)

# Example usage of the smart contract
transaction = {'sender': 'Alice', 'receiver': 'Bob', 'amount': 50}
try:
    new_block = create_block_with_transaction(transaction)
    mine_block(blockchain, new_block)
except ValueError as e:
    print(f"Transaction failed: {e}")

current_block = blockchain['head']
while current_block is not None:
    print(block_to_string(current_block))
    current_block = current_block['next']
