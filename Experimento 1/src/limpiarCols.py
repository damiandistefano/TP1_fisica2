import pandas as pd
cols = ["V multimetro","I teo mult","V fuente","I teo fuente","I real"]
def limpiar_columnas(df, columnas=cols):
    for col in columnas:
        df[col] = df[col].str.replace(',', '.', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df