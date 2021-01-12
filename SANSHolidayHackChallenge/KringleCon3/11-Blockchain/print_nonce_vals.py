#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from naughty_nice import *

if __name__ == '__main__':
    with open('official_public.pem', 'rb') as fh:
        official_public_key = RSA.importKey(fh.read())
    chain = Chain(load=True, filename='blockchain.dat')

    for b in chain.blocks:
        print(b.nonce)
