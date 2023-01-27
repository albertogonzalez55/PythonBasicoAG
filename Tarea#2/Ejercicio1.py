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
print ("El factorial de: "+ str (n)+": es: " + str (factorial (n)))



