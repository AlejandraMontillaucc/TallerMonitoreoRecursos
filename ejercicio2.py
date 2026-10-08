import time

archivo = "archivo_grande.txt"

# Nuestra caché en RAM
cache = {}


def leer_archivo():
    # Si el archivo ya está en caché
    if archivo in cache:
        print(" Leyendo desde la CACHÉ (RAM)...")

        inicio = time.time()

        contenido = cache[archivo]

        fin = time.time()

        print(f"Tiempo desde caché: {fin - inicio:.6f} segundos")

    else:
        print(" Leyendo desde el DISCO...")

        inicio = time.time()

        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()

        fin = time.time()

        # Guardamos el archivo en la caché
        cache[archivo] = contenido

        print(f"Tiempo desde disco: {fin - inicio:.6f} segundos")

    return contenido


print("========== SIMULADOR DE MEMORIA CACHÉ ==========\n")

# Primera lectura
print("PRIMERA LECTURA:")
leer_archivo()

print()

# Segunda lectura
print("SEGUNDA LECTURA:")
leer_archivo()