def sum(a,b):
    resultado = a+b

    return resultado

def res(a,b):
    resultado =a-b
    return resultado 

def mul(a,b):
    resultado =a*b
    return resultado
    
def div(a,b):
    if b == 0:
        print("Error no es posible divir en 0")
        return 
    resultado= a/b
    #### revisar que b  sea diferente de 0
    return resultado 

print("Marque el numero correspondiente a la operacion.")
print("1.sum")
print("2.res")
print("3.mul")
print("4.div")

while True:
    choice = input("Numero seleccionado: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Introdusca el primer valor : "))
        num2 = float(input("Introdusca el segundo valor: "))

        if choice == '1':
            print(num1, "+", num2, "=", sum(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", res(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", mul(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))
        break
    else:
        print("Error")