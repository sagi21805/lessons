def getEvenNumbers(limit: int):
    i = 0
    while i < limit:
        i += 2
        yield i
    
for val in getEvenNumbers(12):
    print(val)