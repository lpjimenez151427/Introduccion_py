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

print("Seleccione una operacion")
operaciones_validas=('+', '-', '*', '/','-1')
print(operaciones_validas)

while True:
    choice = input("")
    if choice =='-1':
        break
    if choice in operaciones_validas:
        num1 = float(input("Introdusca el primer valor : "))
        num2 = float(input("Introdusca el segundo valor: "))
        if choice == '+':
            resultado =sum(a=num1, b=num2)
        elif choice == '-':
            resultado =res(num1, num2)
        elif choice == '*':
            resultado=mul(num1, num2) 
        elif choice == '/':
            resultado= div(num1, num2)
        print("{0} {1} {2} = {3} ".format(num1,choice,num2,resultado))          
    else:
        print("Error")