from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def vmult_vs_vfuente(df):
    voltaje_mult = df['V multimetro']
    voltaje_fuente = df['V fuente']

    # Ajuste lineal: y = m*x + b
    m, b = np.polyfit(voltaje_mult, voltaje_fuente, 1)

    # Mostrar pendiente por consola
    print(f"Pendiente (ajuste lineal): {m:.3f}")
    print(f"Ordenada al origen: {b:.3f}")

    # Graficar datos experimentales
    plt.plot(voltaje_mult, voltaje_fuente, 'o', label='Datos')

    # Graficar recta ajustada
    x = np.linspace(min(voltaje_mult), max(voltaje_mult), 100)
    y = m * x + b
    plt.plot(x, y, 'r--', label=f'Ajuste: y = {m:.2f}x + {b:.2f}')

    plt.xlabel('Voltaje multímetro (V)')
    plt.ylabel('Voltaje fuente (V)')
    plt.title('Voltaje multímetro vs Voltaje fuente')
    plt.grid(True)
    plt.legend()
    plt.axis('equal')  # opcional, para mantener escala 1:1
    plt.show()