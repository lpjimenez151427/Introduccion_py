Ndeserie  = int(input("numero de terminos? "))

n1, n2 = 0, 1
count = 0

if Ndeserie <= 0:
   print("Por favor ingrese el valor positivo")
elif Ndeserie == 1:
   print("El resultado es ",Ndeserie,":")
   print(n1)
else:
   print("La sucecion es:")
   while count < Ndeserie:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1