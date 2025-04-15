def resistencia_mult(df,m,b):
    rM = df['R multímetro']
    vF = df['V fuente']

    vM = m*vF + b

    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(10,6))
    plt.scatter(vM, rM, color='blue', alpha=0.6)
    plt.xlabel('Voltage Multimeter (V)')
    plt.ylabel('Resistance Multimeter (Ω)')
    plt.title('Resistance vs Voltage Measurements')
    plt.grid(True)
    plt.show()
    
    