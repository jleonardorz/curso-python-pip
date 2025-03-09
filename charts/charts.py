# Ejecutar desde terminal para que cree la imagen

import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    # Generar grafica
    # obtener figura y coordenadas
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)

    # Guardar grafica
    plt.savefig('pie.png')
    plt.close()

