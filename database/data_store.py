
# Usuarios del laboratorio

usuarios = {
    "navarro": {
        "nombre": "Navarro",
        "password": "nav2024",  
        "perfil": {             
            "electronica": 0.9,
            "juegos": 0.8,
            "musica": 0.3,
            "deportes": 0.2,
            "libros": 0.4,
            "hogar": 0.1,
            "cocina": 0.0,
            "jardin": 0.0,
            "arte": 0.0,
            "moda": 0.2
        }
    },
    "beltran": {
        "nombre": "Beltrán",
        "password": "belt2024",
        "perfil": {
            "deportes": 0.95,
            "moda": 0.7,
            "electronica": 0.3,
            "juegos": 0.6,
            "musica": 0.4,
            "libros": 0.1,
            "hogar": 0.2,
            "cocina": 0.0,
            "jardin": 0.0,
            "arte": 0.0
        }
    },
    "pineda": {
        "nombre": "Pineda",
        "password": "pine2024",
        "perfil": {
            "libros": 0.95,
            "musica": 0.9,
            "arte": 0.8,
            "electronica": 0.2,
            "juegos": 0.1,
            "deportes": 0.0,
            "moda": 0.3,
            "hogar": 0.2,
            "cocina": 0.1,
            "jardin": 0.0
        }
    },
    "panesso": {
        "nombre": "Panesso",
        "password": "pane2024",
        "perfil": {
            "hogar": 0.95,
            "jardin": 0.85,
            "cocina": 0.8,
            "electronica": 0.2,
            "libros": 0.1,
            "musica": 0.1,
            "deportes": 0.0,
            "juegos": 0.0,
            "arte": 0.2,
            "moda": 0.3
        }
    }
}


# Productos 

productos = {
    1: {"nombre": "Laptop Gamer", "tags": ["electronica", "juegos"], "precio": 1200},
    2: {"nombre": "Smartphone 5G", "tags": ["electronica"], "precio": 800},
    3: {"nombre": "Audífonos Bluetooth", "tags": ["electronica", "musica"], "precio": 150},
    4: {"nombre": "Teclado Mecánico RGB", "tags": ["electronica", "juegos"], "precio": 100},
    5: {"nombre": "Mouse Ergonómico", "tags": ["electronica"], "precio": 50},
    6: {"nombre": "Balón de Fútbol", "tags": ["deportes"], "precio": 30},
    7: {"nombre": "Raqueta de Tenis", "tags": ["deportes"], "precio": 70},
    8: {"nombre": "Zapatillas Running", "tags": ["deportes", "moda"], "precio": 90},
    9: {"nombre": "Novela Best Seller", "tags": ["libros"], "precio": 20},
    10: {"nombre": "Libro 'Python para todos'", "tags": ["libros", "electronica"], "precio": 45},
    11: {"nombre": "Set de Ollas Antiadherentes", "tags": ["hogar", "cocina"], "precio": 120},
    12: {"nombre": "Silla Ergonómica Oficina", "tags": ["hogar"], "precio": 250},
    13: {"nombre": "Planta Artificial Decorativa", "tags": ["hogar", "jardin"], "precio": 25},
    14: {"nombre": "Guitarra Acústica", "tags": ["musica"], "precio": 200},
    15: {"nombre": "Pintura al Óleo Lienzo", "tags": ["arte"], "precio": 60},
    16: {"nombre": "Consola de Videojuegos", "tags": ["juegos", "electronica"], "precio": 500},
    17: {"nombre": "Camiseta Deportiva", "tags": ["deportes", "moda"], "precio": 35},
    18: {"nombre": "Curso Online de Jardinería", "tags": ["jardin"], "precio": 40},
}


# Publicidad

publicidad = {
    1: {"imagen": "anuncio_electronica.jpg", "tags": ["electronica"], "prioridad_base": 0.5},
    2: {"imagen": "anuncio_deportes.jpg", "tags": ["deportes"], "prioridad_base": 0.5},
    3: {"imagen": "anuncio_libros.jpg", "tags": ["libros"], "prioridad_base": 0.5},
    4: {"imagen": "anuncio_hogar.jpg", "tags": ["hogar"], "prioridad_base": 0.5},
    5: {"imagen": "anuncio_musica.jpg", "tags": ["musica"], "prioridad_base": 0.5},
    6: {"imagen": "anuncio_juegos.jpg", "tags": ["juegos"], "prioridad_base": 0.5},
    7: {"imagen": "anuncio_moda.jpg", "tags": ["moda"], "prioridad_base": 0.5},
    8: {"imagen": "anuncio_cocina.jpg", "tags": ["cocina"], "prioridad_base": 0.5},
    9: {"imagen": "anuncio_arte.jpg", "tags": ["arte"], "prioridad_base": 0.5},
    10: {"imagen": "anuncio_jardin.jpg", "tags": ["jardin"], "prioridad_base": 0.5},
}


def update_user_profile(username, search_tags, boost=0.05):
    if username not in usuarios:
        return

    perfil = usuarios[username]["perfil"]

    for tag in perfil:
        if tag in search_tags:
            perfil[tag] = min(1.0, perfil[tag] + boost)
        else:
            perfil[tag] = max(0.0, perfil[tag] - boost * 0.1)