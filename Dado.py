print("Arrojador de Dados")
print ("*******************")

while(True):
    try:
        respuesta = int(input("¿Quiere lanzar los dados?\n1)SI\n2)NO\n"))


        if respuesta == 1:
            from random import randint

            def lanzar_dados():
                dado1 = randint(1,6)
                dado2 = randint(1,6)
                return dado1, dado2

            def evaluar_jugada(dado1, dado2):
                suma_dados = dado1 + dado2
                if  suma_dados <= 6:
                    return f'Lanzaste dos dados y su suma es {suma_dados}. '
                elif suma_dados>6 and suma_dados <10:
                    return f'Lanzaste dos dados y su suma es {suma_dados}. '
                elif suma_dados>=10:
                    return f'Lanzaste dos dados y su suma excelentemente es {suma_dados}. '

            dado1, dado2 = lanzar_dados()
            comprobar_intento = evaluar_jugada(dado1, dado2)
            print(comprobar_intento)
        else:
            print("Hasta luego vuelva prontos")
            break
    except ValueError:
        print("Por favor ingrese el numero (1) o el Nùmero (2)")
