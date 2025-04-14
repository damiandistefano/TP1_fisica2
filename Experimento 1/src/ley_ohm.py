import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def graficar_ley_ohm(df, v_col, i_col):
    
    V = df[v_col]
    I = df[i_col]

    # Ajuste lineal
    pendiente, intercepto, r_value, p_value, std_err = linregress(I, V)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.scatter(I, V, label='Datos experimentales', color='blue')
    plt.plot(I, pendiente * I + intercepto, label=f'Ajuste lineal: V = {pendiente:.2f} I + {intercepto:.2f}', color='red', linestyle='--')
    plt.xlabel("Corriente [A]")
    plt.ylabel("Voltaje [V]")
    plt.title(f"Ley de Ohm: {v_col} vs {i_col}")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    print(f"Pendiente (resistencia estimada): {pendiente:.2f} ohm")
    print(f"R² del ajuste: {r_value**2:.4f}")
