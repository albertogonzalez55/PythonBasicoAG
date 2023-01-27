sampleDict = {
       "class": {
           "student": {
               "name": "Mike",
               "marks": {
                   "physics": 70,
                   "history": 80,
                   "math": 90
}, }
} }

# Extraer nombre del estudiante en el diccionario y definirla como una variable
studentname=sampleDict["class"]["student"]["name"]

#Extraer la nota de cada asignatura del dicho estudiante en el diccionario y definirla como una variable
physicsgrade= sampleDict["class"]["student"]["marks"]["physics"]
historygrade=sampleDict["class"]["student"]["marks"]["history"]
mathgrade=sampleDict["class"]["student"]["marks"]["math"]

#Definir como variables la operaciones para poder llegar al resultado del promedio
total= physicsgrade+historygrade+mathgrade 
promedio= total/3 

#Imprimir nombre y promedio
print("{"+studentname + ": " + str(promedio)+"}") 