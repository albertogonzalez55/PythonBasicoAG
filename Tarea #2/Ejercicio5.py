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


studentname=sampleDict["class"]["student"]["name"]

physicsgrade= sampleDict["class"]["student"]["marks"]["physics"]
historygrade=sampleDict["class"]["student"]["marks"]["history"]
mathgrade=sampleDict["class"]["student"]["marks"]["math"]

total= physicsgrade+historygrade+mathgrade 
promedio= total/3 

print("{"+studentname + ": " + str(promedio)+"}") 