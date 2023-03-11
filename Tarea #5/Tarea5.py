#Lista al cubo en Programación normal:
from random import randint
nums_random=[randint(1,10)for _ in range(10)]

print ("Programación Normal: ")
print (nums_random)

nums_alcubo = [n**3 for n in nums_random]

print (nums_alcubo)

#Lista al cubo en programacion funcional:
lista=[randint(1,10)for _ in range(10)]
lista2=list(map(lambda n: n**3, lista))
print ("Programación funcional: ")
print (lista)
print (lista2)



# Factorial en Programación normal:

# Recivir numero de un usuario a traves de la interfaz
n=int(input("Ingrese un numero entero:"))

# Definir una funcion, en este caso factorial
def factorial (n):

    # Si el numero ingresado es igual a 0 devolver 1
    if (n == 0):
        return 1
        # Lo demas es devolver el numero ingresado multiplicado por la funcion definida menos 1
    else:
        return n * factorial (n-1)

# Imprimir resultado
print ("Programación Normal:")
print ("El factorial de: "+ str (n)+": es: " + str (factorial (n)))

# Factroial en programación funcional
from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1))
print ("Programación funcional: ")
print(factorial(3)) 





##Eliminar repetidos normal

#Generar listas
Lista = [1, 2, 2, 3, 3, 4, 4, 5, 6, 8, 8]
resultantList = []
 
 # Elementos en la lista
for element in Lista:
    #Si no esta en ponerlo en la lista nueva
    if element not in resultantList:
        resultantList.append(element)

#Imprimir lista nueva donde no hay repetidos
print ("Programación Normal: ")
print(resultantList)


#Eliminar repetidos en programación funcional
lista = [1, 2, 2, 3, 4, 4, 5, 5]

nueva_lista = list(set(lista))

print ("Programación funcional: ")
print(nueva_lista) # Imprime [1, 2, 3, 4, 5



# Contar caracteres de un string en programacion normal: 
def contarocur (frase):
    from collections import Counter, defaultdict
    resultado={}
    for c in frase:
        resultado[c]=resultado.get(c, 0) + 1
    print (resultado)

 
 
#Contar caracteres de un string en programación funcional:
from collections import Counter

cadena = input("Ingrese una frase: ")

contador = dict(Counter(filter(lambda x: x.isalpha(), cadena.lower())))

print ("Programación funcional: ")
print(contador) 