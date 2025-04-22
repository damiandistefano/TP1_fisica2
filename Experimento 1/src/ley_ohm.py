import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def graficar_ley_ohm(df1, df2, v_col, i_col):
    
    V1 = df1[v_col]
    I1 = df1[i_col]

    V2 = df2[v_col]
    I2 = df2[i_col]

    # Ajuste lineal
    pendiente1, intercepto1, r_value1, p_value1, std_err1 = linregress(I1, V1)
    pendiente2, intercepto2, r_value2, p_value2, std_err2 = linregress(I2, V2)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.scatter(I1, V1, color='black')
    plt.plot(I1, pendiente1 * I1 + intercepto1, label='R = 9600 $\omega$', color='red', linestyle='--')
    plt.scatter(I2, V2, color='black')
    plt.plot(I2, pendiente2 * I2 + intercepto2, label='R = 98000 $\omega$', color='blue', linestyle='--')
    plt.xlabel("Corriente [A]")
    plt.ylabel("Voltaje [V]")
    plt.grid(True)
    plt.legend()
    plt.ylim(0, 5)

    plt.tight_layout()
    plt.show()

    # print(f"Pendiente (resistencia estimada): {pendiente:.2f} ohm")
    # print(f"R² del ajuste: {r_value**2:.4f}")
