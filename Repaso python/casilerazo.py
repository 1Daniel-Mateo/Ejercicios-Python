#Este es el juego del casillerazo
import random

nombre = input("Bienvenido de la ruleta, ingresa tu nombre: ")
print("Puedes jugar siempre y cuando tu monto sea mayor a 3000")
aleatorio = random.randrange(1, 36)

while True:
    print("Bienvenido", nombre)
    monto = int(input("ingresa tu monto para empezar a jugar: "))

    while monto >= 3000:     
            numero = int(input("ingresa un numero entre 1 y 36 para iniciar: "))
            
            if 1 <= numero <= 36:
                if numero == aleatorio:
                    print("Felicidades haz ganado 1000 dolares")
                    monto+=1000
                    print("Tu monto es de ", monto)
                else:
                    print("Lo siento no has ganado nada")
                    monto-=200
                    print("Tu monto es de ", monto)
            else:
                print("Numero incorrecto vuelve a intentarlo")
    else:
        print("Tu monto es inferior a 3000")
        

    resp = input("¿Quieres seguir jugando?(s/n): ")

    if resp != "s":
        print("Hasta luego", nombre)
        break
 




