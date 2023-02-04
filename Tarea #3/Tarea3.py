# Restas:
def subtract(x, y):
    return x - y

# División
def divide(x, y):
    return x / y

# Factorial
def factorial (n):
    if (n == 0):
        return 1
    else:
        return n * factorial (n-1)

#Suma
def suma(lista):
    resultado= 0
    for i in lista:
        resultado = resultado + i
    return resultado

#Multiplicación
def multi(lista):
    res = 1
    for i in lista:
        res *= i
    return res

# Potencia
def poten(x,y):
    return pow (x,y)

while True:
    print("Elija un tipo de operación.")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.División")
    print("5.Factorial")
    print("6.Potencia")
    print ("7.Salir")
    opera = input("Ingrese el tipo de operación que desee solucionar: ")

# Resta
    if opera in ('2'):
        try:
            num1 = float(input("Numero 1: "))
            num2 = float(input("Numero 2: "))
        except ValueError:
            print("Invalido")
            continue
        if opera == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            #Crear y escribir archivos de texto
            f = open("operacionresta.txt", "a")
            f.write(str (num1)+ "-" + str (num2) +  "=" + str (subtract(num1, num2)))
            f.close()
            f = open("operacionresta.txt", "r")

# Division        
    elif opera in ('4'):
        # Pedirle al usuario los numeros
        try:
            num6 = float(input("Numero 1: "))
            num9 = float(input("Numero 2: "))
        #Verificar
        except ValueError:
            print("Invalido")
            continue
        #Ejecutar la funcion
        if opera == '4':
            #Imprimir resultados
            print(num6, "/", num9, "=", divide(num6, num9))
            #Crear archivo de texto
            f = open("operaciondivision.txt", "a")
            f.write(str (num6) + "/" + str (num9) + "=" + str (divide(num6, num9)))
            f.close()
            f = open("operaciondivision.txt", "r")

# Factorial
    elif opera in ('5'):
        #Pedirle usuario el numero
        try:
            num3 = float(input("Numero: "))
        #Verificarlo
        except ValueError:
            print("Invalido")
            continue
        # Ejecutar funcion
        if opera == '5':
            print ("El factorial de " + str (num3)+ " es "+ str (factorial (num3)))
            #Crear y escribir archivos de textos
            f = open("operacionfactorial.txt", "a")
            f.write("El factorial de " + str (num3)+ " es "+ str (factorial (num3)))
            f.close()
            f = open("operacionfactorial.txt", "r")

#Salir
    elif opera in ('7'):
        if opera == '7':
            break
    
# Suma
    elif opera in ('1'):
        lista = []
        # Pedirle al usuario los numeros que desea sumar
        valor = float(input ("Ingrese Número (ingrese 0 si quiere dejar de agregar): "))
        while valor!= 0:
            lista.append(valor)
            valor=float(input("Ingrese Número (Ingresa valor 0 para finalizar): "))
        print ("El resultado de la suma de " + str (lista) + "= "+ str(suma(lista)))
        #Crear y escribir archivos de texto
        f = open("operacionsuma.txt", "a")
        f.write("El resultado de la suma de " + str (lista) + "= "+ str(suma(lista)))
        f.close()
        f = open("operacionsuma.txt", "r")

#Multiplicacion
    elif opera in ('3'):
        lista = []
        # Pedirle al usuario los numeros que desea sumar
        valor = float(input ("Ingrese Número: (ingrese 0 si quiere dejar de agregar)"))
        while valor!= 0:
            lista.append(valor)
            valor=float(input("Ingresa valor 0 para finalizar:"))
        print ("El resultado al multiplicar" + str (lista) + "= "+ str(multi(lista)))
        #Crear y escribir archivos de texto
        f = open("operacionmultiplicacion.txt", "a")
        f.write("El resultado al multiplicar" + str (lista) + "= "+ str(multi(lista)))
        f.close()
        f = open("operacionmultiplicacion.txt", "r")

#Potencias
    elif opera in ('6'):
        num = 1
        for i in range (0,num):
            base = int (input("Por favor ingrese la base: "))
            exponente = int (input("Por favor ingrese el exponente: "))
            print (str(base) + " elevado a " +" "+ str(exponente) + " es = " + str(poten (base, exponente)))
            #Crear y escribir archivos de texto
            f = open("operacionpotencia.txt", "a")
            f.write(str(base) + " elevado a " +" "+ str(exponente) + " es = " + str(poten (base, exponente)))
            f.close()
            f = open("operacionpotencia.txt", "r")


    else:
        print("Digite un numero que se encuentre entre las opciones (1/2/3/4/5/6/7)")


