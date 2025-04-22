def resistencia_mult(df,m,b):
    rM = df['R multímetro']/ 1e6  # Convertir a megaohms
    vF = df['V fuente']

    vM = m*vF + b

    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(10,6))
    plt.scatter(vM, rM, color='blue', alpha=0.6)
    plt.xlabel('Voltaje Multímetro (V)')
    plt.ylabel('Resistencia Multímetro (MΩ)')
    plt.grid(True)
    plt.show()
    
    