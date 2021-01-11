#!/usr/bin/python3
# Initialize a list
digits = ['1', '3', '7']
for possiblePrime in range(1111, 7777):
    
    # Assume number is prime until shown it is not. 
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False

    digit_count = {}
    for i in digits:
        digit_count[i] = 0

    if isPrime:
        keepgoing = False
        for i in str(possiblePrime):
            if i in digits:
                keepgoing = True
                digit_count[i] += 1
            else:
                keepgoing = False
                break
        if keepgoing:
            candidate = True
            for i in digits:
                if digit_count[i] == 0 or digit_count[i] > 2:
                    candidate = False
            if candidate:
                print(possiblePrime)
