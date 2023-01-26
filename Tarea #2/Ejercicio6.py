Lista = [1, 2, 2, 3, 3, 4, 4, 5, 6, 8, 8]

resultantList = []
 
for element in Lista:
    if element not in resultantList:
        resultantList.append(element)

print(resultantList)
