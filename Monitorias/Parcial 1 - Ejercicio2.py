"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 30/10/2023
Descricion: mago adivinador de numeros

"""

secret_number = 92

def mago(a): # Funcion para adivinar el numero secreto
    i= True
    print (" ----- Guess the secret number-----")
    while (i): #Bucle infinito para adivinar el numero secreto
        num = int(input("please enter an numer integer: "))
        if (num== a):
            print ("You're great!, You're free now")
            i= False 
        else:
            print("Halloween, Halloween! You're stuck in my cycle!")
            continue

if __name__ == '__main__':
    mago(secret_number)



 


        
    