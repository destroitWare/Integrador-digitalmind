print ("*******************")
print ("Adivina Adivinador")
print ("*******************")
import random

numero = random.randint(1,10)

intentos = 0

play = True

while play:
    intentos += 1
    if intentos <= 3:
        print("Adivina el nùmero del 1 al 10. tenès 3 intentos")
        tiraDado = int(input("Elige un número del 1 al 10?: "))
        if tiraDado == numero:
            print("Has Acertado!!!!")
        else:
            print("Tienes otra oportunidad... te quedan ",3-intentos, "intentos")
    else:      
        print("El número del GANADOR era ", numero)
        play = False
