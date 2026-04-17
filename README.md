# Laboratorio 2: Ataques de Fuerza Bruta en DVWA

Este repositorio contiene el script de Python, diccionarios e imágenes de la experiencia práctica del segundo laboratorio de criptografía.

El objetivo principal de este proyecto es desplegar un entorno aislado utilizando la aplicación web **DVWA (Damn Vulnerable Web App)** mediante contenedores Docker, y auditar su formulario de inicio de sesión utilizando cuatro enfoques y herramientas distintas, comparando su rendimiento, huella de red y proponiendo métodos de mitigación.

## Reproducción del Ataque (Python)

Para ejecutar el script de automatización desarrollado en este repositorio, sigue estos pasos:

### 1. Despliegue del entorno

Levanta el contenedor local de DVWA mapeando el puerto 8000:

```
docker run -d --name lab_dvwa -p 8000:80 vulnerables/web-dvwa
```

### 2. Configuración de credenciales

Ingresa a `http://127.0.0.1:8000/` en tu navegador, inicia sesión (`admin` / `password`), configura el nivel de seguridad en **Low**, y extrae tu token de sesión (`PHPSESSID`). Edita el archivo `brute_force_dvwa.py` y reemplaza el valor:

```
HEADERS = {
    "Cookie": "PHPSESSID=token_de_prueba; security=low"
}
```

### 3. Ejecución del script

Se debe tener instalada la librería `requests` y ejecutar el script junto a los diccionarios locales:

```
pip install requests
python brute_force_dvwa.py
```
