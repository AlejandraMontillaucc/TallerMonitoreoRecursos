import os
import time
import psutil

proceso = psutil.Process(os.getpid())

print("===== PRIORIDAD DE PROCESO =====")
print(f"PID: {os.getpid()}")

prioridad = input("Escribe la prioridad (baja/normal/alta): ").lower()

if prioridad == "baja":
    proceso.nice = psutil.BELOW_NORMAL_PRIORITY_CLASS
elif prioridad == "alta":
    proceso.nice = psutil.HIGH_PRIORITY_CLASS
else:
    proceso.nice = psutil.NORMAL_PRIORITY_CLASS

print(f"Prioridad seleccionada: {prioridad}")
print("Realizando cálculo pesado...")

inicio = time.time()

resultado = 0

for i in range(50_000_000):
    resultado += i * i

fin = time.time()

print(f"Resultado: {resultado}")
print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")