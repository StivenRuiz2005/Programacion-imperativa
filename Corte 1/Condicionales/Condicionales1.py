
# inicio variables

cedula = int(input('Ingrese su cedula: '))
salario = int(input('ingrese su salario basico: '))
age_vinculation = int(input('Ingrese su año de vinculacion: '))

# Condicionales

if salario >= 1200000 and age_vinculation >= 1990:
    salario_neto = salario  * 0.08
    total= salario - salario_neto
    print('su cedula es: ', cedula)
    print('Su salario es de: ',total)

elif salario <=55000 or age_vinculation == 1990:
    salario_neto = salario * 0.02
    total= salario - salario_neto
    print('su cedula es: ', cedula)
    print('Su salario es de: ',total)


else:
    salario_neto= salario * 0.05
    total= salario - salario_neto
    print('su cedula es: ', cedula)
    print('Su salario es de: ',total)
