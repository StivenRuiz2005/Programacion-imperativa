"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 01 abril 2022
Descripcion: Nota Final
"""
def nota_final(talleres,parcial,opcional,proyecto,asistencia):
  
  if 0.0 <=(talleres and parcial and opcional and proyecto and asistencia) <= 5 :
    if opcional > parcial:
      return(talleres* 0.2)+(opcional* 0.2)+(proyecto*0.3)+(asistencia*0.3)
    else:
      return(talleres* 0.2)+(parcial* 0.2)+(proyecto*0.3)+(asistencia*0.3)
  else:
    return print('Nota no valida')

taller= float(input('Digite la nota del taller: '))
parcial= float(input('Digite la nota del parcial: '))
opcional= float(input('Digite la nota del opcional: '))
proyecto= float(input('Digite la nota del proyecto: '))
asistencia= float(input('Digite la nota de la asistencia: '))

print("Su nota final es",round(nota_final(taller,parcial,opcional,proyecto,asistencia),2))