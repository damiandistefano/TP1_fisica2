def resistencia_mult(df,m,b):
    rM = df['R multímetro']
    vF = df['V fuente']

    vM = m*vF + b

    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(10,6))
    plt.scatter(vM, rM, color='blue', alpha=0.6)
    plt.xlabel('Voltaje Multímetro (V)')
    plt.ylabel('Resistencia Multímetro (Ω)')
    plt.title('Mediciones de Resistencia vs Voltaje')
    plt.grid(True)
    plt.show()
    
    