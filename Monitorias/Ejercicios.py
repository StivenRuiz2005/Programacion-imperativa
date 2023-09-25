cedula = int(input("Digite la cedula: "))
salario_b = float(input("Ingrese su salario: "))
age = int(input("Ingrese su año de vinculacion: "))

def Salario(Cedula,Salario_b,Age):
    if (Salario_b > 1200000 and Age > 1995):
        neto = Salario_b * 0.06
    elif (Salario_b < 550000 or Age == 1995):
        neto = Salario_b * 0.03
    else:
        neto = Salario_b * 0.04

    salario_final = (Salario_b + neto) - (Salario_b * 0.04)

    return print(f"Cedula: {Cedula} \nSu salario neto es: {salario_final}")

Salario(cedula,salario_b,age)
Salario(123456,1200001,1994)




