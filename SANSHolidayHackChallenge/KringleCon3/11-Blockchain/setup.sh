#!/usr/bin/bash -x
# You can download the two files below from Santa's Office
wget https://download.holidayhackchallenge.com/2020/blockchain.dat
wget https://download.holidayhackchallenge.com/2020/OfficialNaughtyNiceBlockchainEducationPack.zip
unzip OfficialNaughtyNiceBlockchainEducationPack.zip
cp OfficialNaughtyNiceBlockchainEducationPack/naughty_nice.py .
cp OfficialNaughtyNiceBlockchainEducationPack/official_public.pem .

# Needed to answer question 11a)
sudo apt install -y python3-pip python3-crypto
sudo pip3 install mersenne-twister-predictor
