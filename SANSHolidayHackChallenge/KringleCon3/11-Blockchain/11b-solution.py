#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Hash import MD5,SHA256
from naughty_nice import *

# Stolen from Block() object's MD5 version of full_hash() method
def compute_sha256_hash(signed_block):
    obj = SHA256.new()
    obj.update(signed_block)
    return obj.hexdigest()

# A copy of Block() object's full_hash() method
def compute_md5_hash(signed_block):
    hash_obj = MD5.new()
    hash_obj.update(signed_block)
    return hash_obj.hexdigest()

if __name__ == '__main__':
    # Read in the blockchain
    with open('official_public.pem', 'rb') as fh:
        official_public_key = RSA.importKey(fh.read())
    chain = Chain(load=True, filename='blockchain.dat')

    # SHA256 hash of altered block
    target_block_hash = '58a3b9335a6ceb0234c12d35a0564c4ef0e90152d0eb2ce2082383b38028a90f'
    altered_block = None

    # The starting position of the "subblocks" we want to change
    first_change = 64
    second_change = 256

    # Fetch the altered block in the chain
    for block in chain.blocks:
        this_hash = compute_sha256_hash(block.block_data_signed())
        if this_hash == target_block_hash:
            altered_block = block.block_data_signed()
            break

    hash1 = compute_md5_hash(altered_block)
    print(f"MD5 hash of block as we found it: {hash1}")

    # 'bytes' objects are immutable, so copy to a bytearray that we can modify
    new_block = bytearray(altered_block)
    hash2 = compute_md5_hash(new_block)
    print(f"MD5 hash of the copy we made, without changes: {hash2}")
    assert hash1 == hash2

    # Simple UniColl method
    # Make the changes to the 10th position of each subblock
    # and corresponding collision block then validate

    # First, Jack is supposed to get maximum penalty, so change the sign
    # from 1 to 0.
    new_block[first_change+9] -= 1
    new_block[first_change+64+9] += 1
    hash2 = compute_md5_hash(new_block)
    print(f"MD5 hash of block after first change: {hash2}")
    assert hash1 == hash2

    # Second, change the Catalog pointer in the PDF to the object containing
    # Shinny's true comments about Jack.
    new_block[second_change+9] += 1
    new_block[second_change+64+9] -= 1
    hash2 = compute_md5_hash(new_block)
    print(f"MD5 hash of block after second change: {hash2}")
    assert hash1 == hash2

    # Output what's being asked from question 11b)
    print(f"SHA256 of the block with 4 bytes changed: {compute_sha256_hash(new_block)}")
