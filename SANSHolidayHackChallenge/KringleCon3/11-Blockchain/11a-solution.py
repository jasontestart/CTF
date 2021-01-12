#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from naughty_nice import *
from mt19937predictor import MT19937Predictor

if __name__ == '__main__':
    # Read in the blockchain
    with open('official_public.pem', 'rb') as fh:
        official_public_key = RSA.importKey(fh.read())
    chain = Chain(load=True, filename='blockchain.dat')

    # We are being asked to predict the nonce for a future block
    target_index = 130000

    # Set-up the predictor with all previous known
    # nonce values. We need 624 for 32-bit numbers. Do we
    # need at least 1248 for 64-bit numbers? 
    # Regardless: the more, the *merrier*!
    predictor = MT19937Predictor()
    for b in chain.blocks:
        predictor.setrandbits(b.nonce,64)

    # The first unknown index is the last known index, incremented by one
    first_unknown_index = chain.blocks[len(chain.blocks)-1].index + 1

    # Generate some predictions of nonce values for the indexes in-between
    i = first_unknown_index
    while i < target_index:
        predictor.getrandbits(64)
        i += 1

    # Output the HEX representation of what we want.
    print(hex(predictor.getrandbits(64)))
