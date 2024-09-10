def complex_function(x, y, z):
    if x > 10:
        if y < 5:
            if z == 0:
                print("Caso 1: x > 10, y < 5, z == 0")
            else:
                if z > 5:
                    print("Caso 2: x > 10, y < 5, z > 5")
                else:
                    print("Caso 3: x > 10, y < 5, z no cumple condiciones anteriores")
        else:
            if y == 10:
                print("Caso 4: x > 10, y == 10")
            else:
                if z != 0:
                    print("Caso 5: x > 10, y >= 5, z != 0")
                else:
                    print("Caso 6: x > 10, y >= 5, z == 0")
    else:
        if x == 10:
            if y == z:
                print("Caso 7: x == 10, y == z")
            else:
                if z > 10:
                    print("Caso 8: x == 10, z > 10")
                else:
                    print("Caso 9: x == 10, y != z, z <= 10")
        else:
            if x < 0:
                print("Caso 10: x < 0")
            else:
                if z < 0:
                    print("Caso 11: x <= 10, z < 0")
                elif z == 0:
                    print("Caso 12: x <= 10, z == 0")
                else:
                    print("Caso 13: x <= 10, z > 0")
                    
# Llamada de prueba a la función
complex_function(15, 3, 0)
complex_function(8, 12, 5)
complex_function(10, 10, 15)
