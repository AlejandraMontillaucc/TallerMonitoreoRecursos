import psutil
import time

LIMITE = 500_000

memoria = []

print("===== ESTRÉS DE MEMORIA =====")

for i in range(LIMITE):
    memoria.append("X" * 1000)

    if i % 50_000 == 0:
        ram = psutil.virtual_memory().percent
        print(f"Objetos creados: {i:,} | RAM utilizada: {ram}%")
        time.sleep(0.5)

print("\nPrueba finalizada.")
print(f"Total de objetos creados: {len(memoria):,}")