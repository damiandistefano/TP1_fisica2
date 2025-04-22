from matplotlib import pyplot as plt
import pandas as pd
import numpy as np



def vmult_vs_vfuente(df):
    err_v_mult = 0.01  # Error en voltaje multímetro
    err_v_fuente = 0.01  # Error en voltaje fuente

    voltaje_mult = df['Vmult']
    voltaje_fuente = df['Vfuente']

    # Ajuste lineal: y = m*x + b
    m, b = np.polyfit(voltaje_mult, voltaje_fuente, 1)

    # Mostrar pendiente por consola
    print(f"Pendiente (ajuste lineal): {m:.3f}")
    print(f"Ordenada al origen: {b:.3f}")

    # Graficar datos experimentales con barras de error en X e Y
    plt.errorbar(voltaje_mult, voltaje_fuente, 
                 xerr=err_v_mult, yerr=err_v_fuente, 
                 fmt='o', label='Datos', color='black')

    # Graficar recta ajustada
    x = np.linspace(min(voltaje_mult), max(voltaje_mult), 100)
    y = m * x + b
    plt.plot(x, y, 'r--', label=f'Ajuste: y = {m:.2f}x + {b:.2f}')

    plt.xlabel('Voltaje multímetro (V)')
    plt.ylabel('Voltaje fuente (V)')
    plt.grid(True)
    plt.legend()
    plt.axis('equal')  # Escala 1:1 para comparar visualmente

    plt.tight_layout()
    plt.show()

    return m, b
