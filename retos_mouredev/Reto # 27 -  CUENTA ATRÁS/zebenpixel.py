import time
import threading

def countdown(start: int, seconds: int):
   
    # isinstance() maneja de manera más flexible las subclases y herencia
    if isinstance(start, int) and isinstance(seconds, int) and start > 0 and seconds > 0:
        original_string = "X-X-X-X-X-X-X-X-X-X-"
        modified_string = original_string

        for number in range(start, -1, -1):
            modified_string = modified_string[2:]  # Elimina dos caracteres en cada iteración
            print(f"Tiempo restante: {number} segundos - Contador: {modified_string}")
            if number > 0:
                time.sleep(seconds)
        
        print("X- ¡Conteo finalizado! -X")
    else:
        print("Los parámetros deben ser enteros positivos")

if __name__ == "__main__":
    # Conteo Asíncrono
    threading.Thread(target=countdown, args=(9, 1)).start()
