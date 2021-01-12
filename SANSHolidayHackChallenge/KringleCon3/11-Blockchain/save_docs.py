#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from naughty_nice import *

# Stolen from Block() object's MD5 version of full_hash() method
def compute_sha256_hash(signed_block):
    obj = SHA256.new()
    obj.update(signed_block)
    return obj.hexdigest()


if __name__ == '__main__':
    # Read in the blockchain
    with open('official_public.pem', 'rb') as fh:
        official_public_key = RSA.importKey(fh.read())
    chain = Chain(load=True, filename='blockchain.dat')

    # SHA256 hash of altered block
    target_block_hash = '58a3b9335a6ceb0234c12d35a0564c4ef0e90152d0eb2ce2082383b38028a90f'

    # Fetch the altered block in the chain
    for block in chain.blocks:
        this_hash = compute_sha256_hash(block.block_data_signed())
        if this_hash == target_block_hash:
            block.dump_doc(1)
            block.dump_doc(2)
            break
