#Generar lista aleatroia
from random import randint
nums_random=[randint(1,10)for _ in range(10)]

#Imprimir la lista aleatoria
print (nums_random)

#Definir la función de los numeros al cubo
nums_alcubo = [n**3 for n in nums_random]

#Imprimir la lista con los resultados
print (nums_alcubo)
