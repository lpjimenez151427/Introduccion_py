def serie_fibonacci(Ndeserie):
    n1, n2 = 0, 1
    count = 0

    if Ndeserie <= 0:
        print("Por favor ingrese el valor positivo")
    elif Ndeserie == 1:
        print("El resultado es ",Ndeserie,":")
        print(n1)
    else:

        print("El valor en la posicion {0} es: ".format(Ndeserie))
        lista_numeros =[n1,n2]
        while count < Ndeserie:
            #print(n1) 
            nth = n1 + n2
            lista_numeros.append(nth)
            n1 = n2
            n2 = nth
            count += 1
        return lista_numeros

Limite  = int(input("numero de terminos? "))
numeros =serie_fibonacci (Ndeserie=Limite)
print (numeros[len(numeros)-1])



