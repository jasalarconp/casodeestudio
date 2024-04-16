# ejercicio 1: Desarrollar un programa que permita solicitar 15 valores al usuario mostrar el resultado de la suma de los mismos y su promedio.
print("hola, ingresa 15 valores")

numeros = []
for i in range(15):
    valor = float(input("ingresa el valor {}: ".format(i+1)))
    numeros.append(valor)

#calcular la suma de los valores
suma_total = sum(numeros)

#calcular el promedio de los valores 
promedio = suma_total / len(numeros)

#mostrar resultado
print("La suma de los valores es:", suma_total)
print("El promedio de los valores es:", promedio)

#ejercicio 2: La alcaldía de Fusagasugá tiene puntos de reparto de vacunas contra el covid-19, se pretende que funcionen de la siguiente manera. Cada día, empezar con 1000 vacunas disponibles y a través de un programa que controla las entregas avisar si el inventario baja de 200 unidades. Desarrollar un programa que muestre los resultados.

def reparto_vacunas():
    inventario = 1000

    while inventario > 0:
        print("Inventario actual de vacunas:", inventario)

        if inventario < 200:
            print("El inventario es menor a 200 unidades.")
        
        entregas = int(input("ingrese la cantidad de vacunas entregadas hoy (o 0 para salir): "))

        if entregas == 0:
            print("saliendo del programa")
            break
        inventario -= entregas

    print("el inventario de vacunas ha llegado a cero. Fin del programa")

if __name__ == "__main__":
    reparto_vacunas()
