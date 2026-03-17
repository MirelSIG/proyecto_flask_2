# Proyecto Flask 2: API Weather con SQLite

Este proyecto implementa una API REST sencilla para gestionar ciudades y su clima usando Flask + SQLite.

## Quickstart (60 segundos)

```bash
git clone https://github.com/MirelSIG/proyecto_flask_2.git
cd proyecto_flask_2
virtualenv -p python3 myEnv
source myEnv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Prueba rapida del backend:

- Abre `http://127.0.0.1:5001`
- Si quieres testear CRUD, importa en Postman el archivo `assets/pythonServer.postman_collection.json`

Incluye:

- Endpoints CRUD sobre `/cities`
- Persistencia en base de datos local `weather.db`
- Soporte CORS para consumir la API desde frontend o herramientas externas
- Coleccion de Postman para pruebas manuales

![Flask](./assets/imgReadme/python-flask-web-developer.jpg)

## 1. Arquitectura del proyecto

Flujo de capas:

1. `app.py`: punto de arranque del servidor
2. `src/webserver.py`: define las rutas HTTP
3. `src/weather.py`: capa de servicio
4. `src/weather_repository_sqlite.py`: acceso SQL a `weather.db`

Estructura principal:

```text
proyecto_flask_2/
├── app.py
├── requirements.txt
├── weather.db
├── assets/
│   └── pythonServer.postman_collection.json
└── src/
    ├── webserver.py
    ├── weather.py
    └── weather_repository_sqlite.py
```

## 2. Requisitos previos

- Python 3
- pip
- virtualenv (recomendado)
- Postman (opcional, para pruebas)

## 3. Instalacion paso a paso

### 3.1 Clonar y entrar en el proyecto

```bash
git clone https://github.com/MirelSIG/proyecto_flask_2.git
cd proyecto_flask_2
```

### 3.2 Crear y activar entorno virtual

```bash
virtualenv -p python3 myEnv
source myEnv/bin/activate
```

### 3.3 Instalar dependencias

Instalacion recomendada:

```bash
pip install -r requirements.txt
```

Si solo quieres resolver CORS rapido:

```bash
pip install flask-cors
```

## 4. Ejecutar el backend

Con el entorno virtual activo:

```bash
python3 app.py
```

El servidor arranca en:

- `http://127.0.0.1:5001`

Nota: en este proyecto el puerto configurado en `app.py` es `5001`.

## 5. Endpoints de la API

Base URL local:

- `http://127.0.0.1:5001`

Rutas disponibles:

1. `GET /` devuelve un mensaje HTML de prueba
2. `GET /cities` devuelve todas las ciudades
3. `GET /cities/<city_id>` devuelve una ciudad por id
4. `POST /cities` crea una ciudad
5. `PUT /cities/<city_id>` actualiza una ciudad
6. `DELETE /cities/<city_id>` elimina una ciudad

Ejemplo de body JSON para `POST` y `PUT`:

```json
{
  "id": "NAR",
  "name": "Narita",
  "temperature": 23,
  "rain_probability": 0.45
}
```

## 6. Probar con Postman

1. Abre Postman
2. Importa la coleccion: `assets/pythonServer.postman_collection.json`
3. Ejecuta en orden recomendado:

- `GET /`
- `GET /cities`
- `POST /cities`
- `GET /cities/NAR`
- `PUT /cities/NAR`
- `DELETE /cities/NAR`
- `GET /cities/NAR` (comprobar borrado)

Capturas de referencia:

![Ruta raiz](./assets/imgReadme/flask2_ruta_raiz.png)
![GET cities](./assets/imgReadme/flask2_get_cities.png)
![GET by id](./assets/imgReadme/flask2_cities_get_id.png)
![POST city](./assets/imgReadme/flask2_post_new.png)
![PUT city](./assets/imgReadme/flask2_update.png)
![DELETE city](./assets/imgReadme/flask2_delete_NRT.png)

## 7. Base de datos SQLite

La BD local se llama `weather.db` y contiene la tabla `cities`:

- `id`
- `name`
- `temperature`
- `rain_probability`

La tabla se crea automaticamente si no existe al iniciar el repositorio SQLite.

![DB Browser](./assets/imgReadme/wheatherDB.png)

## 8. Tests

Hay material de pruebas en `src/test_weather_repository_sqlite.py`.

Para ejecutar tests (si aplica en tu entorno):

```bash
python -m pytest -q
```

## 9. Solucion de problemas comunes

### Puerto ocupado

Si el puerto esta en uso, identifica y finaliza el proceso:

```bash
lsof -i :5001
kill <PID>
```

### Error de modulos no encontrados

Verifica que el entorno virtual este activo e instala dependencias:

```bash
source myEnv/bin/activate
pip install -r requirements.txt
```

## 10. CORS en Flask

Este proyecto ya habilita CORS en `src/webserver.py` con:

```python
from flask_cors import CORS
cors = CORS(app)
```

Con esto, clientes desde otros origenes (por ejemplo frontend en otro puerto) pueden consumir la API.
