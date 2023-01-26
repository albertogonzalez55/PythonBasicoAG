a=input(print("Ingrese una palabra:"))
b=input(print("Ingrese otra palabra con la misma cantidad de caracteres que la primera:"))

if len (a) and len(b)==2:
    print (format (a[0]+ b [0]+a[1]+ b [1] ))
elif len (a) and len (b)== 3:
    print (format (a[0]+ b [0]+a[1]+ b [1]+a[2]+ b [2] ))
elif len (a) and len (b)== 4:
    print (format (a[0]+ b [0]+a[1]+ b [1]+a[2]+ b [2]+a[3]+ b [3] ))
elif len (a) and len (b)== 5:
    print (format (a[0]+ b [0]+a[1]+ b [1]+a[2]+ b [2]+a[3]+ b [3]+a[4]+ b [4] ))
elif len (a) and len (b)== 6:
    print (format (a[0]+ b [0]+a[1]+ b [1]+a[2]+ b [2]+a[3]+ b [3]+a[4]+ b [4]+a[5]+ b [5] ))
elif len (a) and len (b)== 7:
    print (format (a[0]+ b [0]+a[1]+ b [1]+a[2]+ b [2]+a[3]+ b [3]+a[4]+ b [4]+a[5]+ b [5] +a[6]+ b [6]))
else:
    print ("Error")

