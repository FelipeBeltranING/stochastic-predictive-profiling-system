# Sistema de Perfilado

## Estructura de Directorios del Proyecto
sistema_perfilado/
│
├── core/ # El "Corazón" (Lógica matemática pura, independiente de la UI)
│ ├── init.py
│ ├── pagerank.py # Código del algoritmo PageRank
│ └── model_sor_jor.py # Código del modelo SOR-JOR (si deciden implementarlo)
│
├── database/ # Persistencia de Datos (Simulada o Real)
│ ├── init.py
│ └── data_store.py # Datos de usuarios de laboratorio, productos y publicidad
│
├── services/ # Capa de Aplicación (Une el Core con los datos)
│ ├── init.py
│ ├── auth_service.py # Control de acceso (Login)
│ ├── search_service.py # Motor de búsqueda predictivo
│ └── ad_service.py # Gestor de prioridad de publicidad por usuario
│
├── ui/ # Capa de Presentación (Interfaz de usuario)
│ ├── init.py
│ ├── web_app.py # Si eligen Web (Flask / FastAPI)
│ └── desktop_app.py # Si eligen Escritorio (Tkinter / PyQt)
│
└── main.py # Punto de entrada de la aplicación

text

## Explicación de cada Capa y su Responsabilidad

### A. Capa de Núcleo (`core/`)

Esta capa contiene **matemática pura**. No sabe qué es un botón, ni qué es una base de datos, ni qué es la web. Solo recibe matrices o listas de números y devuelve vectores calculados.

- **`pagerank.py`**: Una función que recibe una matriz de adyacencia (las conexiones de los productos del sistema) y devuelve el vector con los puntajes de importancia global.

### B. Capa de Datos (`database/`)

Para un proyecto de laboratorio, no es estrictamente obligatorio montar una base de datos compleja como PostgreSQL. Puedes usar archivos JSON, una base de datos ligera como SQLite, o simplemente diccionarios de Python en memoria dentro de `data_store.py`.

Aquí guardas los perfiles de tus compañeros de laboratorio:

```python
USUARIOS = {
    "juan_pablo": {"nombre": "Juan Pablo", "gustos": {"tecnologia": 0.9, "libros": 0.1}},
    "martin": {"nombre": "Martin", "gustos": {"tecnologia": 0.2, "libros": 0.8}}
}
C. Capa de Servicios (services/)
Es el intermediario (orquestador). Toma los datos crudos de la base de datos, los pasa por los algoritmos del core y genera el resultado final.

search_service.py: Cuando el usuario escribe "lap", este servicio busca qué productos coinciden con "lap" (ej: Laptop, Lápiz), le pide al core el PageRank de esos productos, consulta los gustos del usuario logueado para ajustar los pesos, y devuelve la lista ordenada predictiva.

ad_service.py: Toma los gustos del usuario activo y ordena la lista de imágenes de publicidad de mayor a menor afinidad.

D. Capa de Presentación (ui/)
Es la superficie visual que ve el usuario. Puede ser una aplicación web o de escritorio. Su única tarea es capturar los clicks o el texto que escribe el usuario, mandarlo a los servicios y pintar lo que estos le devuelvan.

Flujo de Trabajo en la Arquitectura (Ejemplo Práctico)
El Usuario escribe en la interfaz (ui/): Ingresa al sistema haciendo Login. El componente del buscador detecta que el usuario escribió la letra "M".

La UI llama al Servicio (services/): El backend recibe la letra "M" y el ID del usuario actual.

El Servicio procesa con el Algoritmo (core/): El servicio filtra los productos que empiezan con "M", extrae la matriz de relevancia calculada por el PageRank en el core, e inclina la balanza hacia los gustos del usuario logueado.

Respuesta Dinámica: El servicio devuelve el arreglo final. La interfaz gráfica se actualiza instantáneamente mostrando los resultados del autocompletado y reorganizando los banners de publicidad en la pantalla.
