import psutil
import time
from datetime import datetime

UMBRAL_RAM = 80

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    print("=" * 40)
    print("     VIGILANTE DE RECURSOS")
    print("=" * 40)
    print(f"CPU: {cpu}%")
    print(f"RAM: {ram}%")

    if ram > UMBRAL_RAM:
        mensaje = (
            f"[{datetime.now()}] ALERTA: "
            f"RAM supera el 80% - Uso actual: {ram}%\n"
        )

        print("⚠️ ALERTA: RAM SUPERÓ EL 80%")

        with open("alertas_ram.txt", "a", encoding="utf-8") as archivo:
            archivo.write(mensaje)

    time.sleep(2)