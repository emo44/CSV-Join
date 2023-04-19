# pyinstaller videoenplay_une_csv.py --onefile --icon="C:\Users\emo\python\images\csv.ico"
import os
import csv
from datetime import datetime

def mostrar_instrucciones():
    print("Creado para Videoenplay por Emo")
    print("Para utilizar esta utilidad:")
    print("1. Ejecutalo en la misma carpeta donde hayas descomprimido todos los CSV.")
    print("2. El resultado es un nuevo fichero Todos.csv que contiene todos los csv y con una nueva columna fecha.")
    print("\nPresione cualquier tecla para continuar...")

# Mostrar instrucciones y esperar a que se presione una tecla
mostrar_instrucciones()
input()

# Obtener la lista de archivos en el directorio actual
archivos = os.listdir()

# Filtrar archivos CSV
archivos_csv = [archivo for archivo in archivos if archivo.endswith('.csv')]

if archivos_csv:
    # Preparar el archivo de salida
    with open("Todos.csv", "w", newline='') as archivo_salida:
        escritor_csv = csv.writer(archivo_salida)

        # Procesar cada archivo CSV
        for i, archivo_csv in enumerate(archivos_csv):
            # Extraer la fecha del nombre del archivo
            fecha_str = archivo_csv[-14:-4]  # Extraer los 10 últimos caracteres antes de la extensión
            fecha = datetime.strptime(fecha_str, "%d-%m-%Y").date()

            with open(archivo_csv, "r", newline='') as archivo_entrada:
                lector_csv = csv.reader(archivo_entrada)

                # Escribir encabezado si es el primer archivo
                if i == 0:
                    encabezado = next(lector_csv)
                    encabezado.insert(0, "Fecha")
                    escritor_csv.writerow(encabezado)
                else:
                    # Saltar el encabezado en los archivos siguientes
                    next(lector_csv)

                # Procesar cada fila y agregar la columna con la fecha
                for fila in lector_csv:
                    fila.insert(0, fecha)
                    escritor_csv.writerow(fila)

    print("Archivo 'Todos.csv' creado con éxito.")
else:
    print("No se encontraron archivos CSV en el directorio.")
