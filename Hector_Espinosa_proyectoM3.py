import random
import matplotlib.pyplot as plt

# Función para calular el comportamiento de las canicas
def calcular_canicas(num_canicas, num_niveles):
    """
    Calular el comportamiento de las canicas
    Recibe como parámetros el número de las canicas y el numero de niveles por las que van a caer
    
    """
    # Declarar la lista en la que se van a guardar los resultados con las posiciones en las que caen las canicas
    resultados = [0] * num_niveles
    # Ciclo for por cada canica
    for canica in range(num_canicas):
        # Definir posición inicial de las canicas que se encuentra en el punto medio de 12
        posicion = random.randint(6,7)
        #Ciclo for para simular la caída de las canicas por cada nivel
        for nivel in range(num_niveles):
            # Si la posición llega al límite izquierdo(menos de 0) y que la siguiente posición generada no se salga del límite 
            if posicion == 0:
                posicion = random.randint(0,posicion+1)
            # Si la posición llega al límite derecho(más de 12) y que la siguiente posición generada no se salga del límite 
            elif posicion == num_niveles:
                posicion = random.randint(posicion-1,posicion)
            #Se genera la siguiente posición de la canica
            else:
                posicion = random.randint(posicion-1, posicion+1)
        # Se aumenta el contador de la posición en la que cayó la canica
        resultados[posicion-1] += 1
    return resultados

# Función para generar e imprimir la gráfica con los resultados
def generar_grafica(resultados):
    """
    Se genera una gráfica de barras y se configura el título y las etiquetas de los ejes
    Recibe como parámetros un arreglo con los resultados de las posiciones en las que cayeron las canicas
    """
    num_resultados = len(resultados)
    plt.bar(range(num_resultados), resultados)
    plt.xlabel("Contenedor")
    plt.ylabel("Número de canicas")
    plt.title("Máquina de Galton")
    plt.show()

# Llamar función que calcula la caída de las canicas
resultados = calcular_canicas(3000, 12)
# Llamar función que genera la gráfica y la muestra en pantalla
generar_grafica(resultados)