
def contar (frse):
    cantidad_letras=0
    cantidad_digitos=0
    for c in frse:
        if c.isnumeric():
                        cantidad_digitos +=1
        elif c.isalpha():
                        cantidad_letras +=1     
        else:
            pass


        pretoral= cantidad_digitos + cantidad_letras
        total=len(frse)
        result=total-pretoral
                    
    print ('Letras = ', cantidad_letras)
    print ('Números = ', cantidad_digitos)
    print ('Caracteres Especiales = ' , str (result))

# n=input('Ingrese una frase: ')
# print (contar(n))

def contarocur (frase):
    from collections import Counter, defaultdict
    resultado={}
    for c in frase:
        resultado[c]=resultado.get(c, 0) + 1
    print (resultado)

# f=input('Ingrese una frase: ')
# print (contarocur(f))

def eliminar3 (lista, eli):
    for x in lista:
        if eli in lista:
            lista.remove(eli)
    print(lista)
        
# print(eliminar3([20, 30, 40, 20, 5, 100, 5, 20], 20))

def lstaytuple4 ():
    i=input("Ingrese una secuencia de números: ")

    a=[i]
    b=(i)
    print ("Lista: "+ str(a))
    print ("Tupla: " + str (b))

# lstaytuple4 ()

def lytpla4():
    #Pedir al usuario:
    usu = input("Introduce una muestra de números separados por comas: ")
    #Tupla
    usu = usu.split(',')
    n = len(usu)
    for i in range(n):
        usu[i] = int(usu[i])
    usu = tuple(usu)
    print ("Tupla: "+ str (usu))
    #Lista
    lista=[]
    for x in usu:
        lista.append (x)
    print ("Lista: "+ str (lista))


# lytpla4 ()











