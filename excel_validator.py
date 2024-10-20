import pandas as pd

# Leer el archivo Excel
try:
    data = pd.read_excel("datos.xlsx")
except FileNotFoundError:
    print("El archivo 'datos.xlsx' no se encontró.")
    exit()
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")
    exit()

# Imprimir los nombres de las columnas para depuración
print("Nombres de columnas:", data.columns.tolist())

# Limpiar los nombres de las columnas eliminando espacios
data.columns = data.columns.str.strip()

# Validaciones básicas
def validar_filas(data):
    errores = []
    required_columns = ['NOMBRE', 'MONTO']  # Columnas requeridas
    for col in required_columns:
        if col not in data.columns:
            errores.append(f"Columna faltante: '{col}'")

    if not errores:  # Validar filas solo si las columnas existen
        for index, row in data.iterrows():
            if pd.isnull(row['NOMBRE']) or pd.isnull(row['MONTO']):
                errores.append(f"Fila {index + 1}: Datos incompletos")

    return errores

# Verificar errores
errores = validar_filas(data)
if errores:
    print("Errores encontrados:")
    for error in errores:
        print(error)
else:
    print("Datos validados")

    # Crear nueva columna con el aumento del 10%
    data['MONTO AUMENTADO'] = data['MONTO'] * 1.10
    # Guardar el nuevo archivo Excel
    try:
        data.to_excel("datos_resultantes.xlsx", index=False)
        print("Archivo 'datos_resultantes.xlsx' generado con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")