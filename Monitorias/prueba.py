cedula = int(input("Ingrese su cedula: "))
salario_b = int(input("Ingrese su salario: "))
año_vinculacion = int(input("Ingrese su año vinculacion: "))


if (salario_b > 1200000 and año_vinculacion > 1995):
    aumento = salario_b * 0.06
elif (salario_b <550000 or año_vinculacion == 1995):
    aumento = salario_b * 0.03
else:
    aumento = salario_b * 0.04

salario_neto = (salario_b + aumento)-(salario_b * 0.04)

print("Cedula: ",cedula, "\n Salario neto: ",salario_neto)


