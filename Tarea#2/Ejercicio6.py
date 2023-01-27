#Generar listas
Lista = [1, 2, 2, 3, 3, 4, 4, 5, 6, 8, 8]
resultantList = []
 
 # Elementos en la lista
for element in Lista:
    #Si no esta en ponerlo en la lista nueva
    if element not in resultantList:
        resultantList.append(element)

#Imprimir lista nueva donde no hay repetidos
print(resultantList)
