# services/ad_service.py
"""
Servicio de publicidad personalizada usando Colas de Prioridad (heapq).
Ordena los anuncios según el perfil del usuario.
"""
import heapq
from database.data_store import publicidad

# Mapeo de categorías a emojis y colores para placeholder visual
AD_THEMES = {
    "electronica": {"emoji": "💻", "color": "#3b82f6"},
    "deportes": {"emoji": "⚽", "color": "#10b981"},
    "libros": {"emoji": "📚", "color": "#8b5cf6"},
    "hogar": {"emoji": "🏠", "color": "#f59e0b"},
    "musica": {"emoji": "🎵", "color": "#ec4899"},
    "juegos": {"emoji": "🎮", "color": "#ef4444"},
    "moda": {"emoji": "👗", "color": "#d97706"},
    "cocina": {"emoji": "🍳", "color": "#f97316"},
    "arte": {"emoji": "🎨", "color": "#14b8a6"},
    "jardin": {"emoji": "🌱", "color": "#22c55e"},
}


def get_prioritized_ads(user_profile, top_n=5):
    """
    Ordena los anuncios usando una Cola de Prioridad (heap)
    según el perfil del usuario.

    Implementación con heapq:
    - Prioridad = Σ (perfil_usuario[tag] × prioridad_base) para cada tag
    - heapq es min-heap → se niegan prioridades para obtener max-first

    Args:
        user_profile (dict): Perfil de intereses del usuario
        top_n (int): Número máximo de anuncios a retornar

    Returns:
        list: Anuncios ordenados por prioridad descendente
    """
    # Construir cola de prioridad
    priority_queue = []

    for ad_id, ad in publicidad.items():
        priority = 0.0
        for tag in ad["tags"]:
            user_interest = user_profile.get(tag, 0.0)
            priority += user_interest * ad["prioridad_base"]

        # heapq es min-heap, negamos para max-heap
        heapq.heappush(priority_queue, (-priority, ad_id))

    # Extraer anuncios en orden de prioridad
    result = []
    while priority_queue and len(result) < top_n:
        neg_priority, ad_id = heapq.heappop(priority_queue)
        ad = publicidad[ad_id]
        categoria = ad["tags"][0]
        theme = AD_THEMES.get(categoria, {"emoji": "📢", "color": "#6b7280"})

        result.append({
            "id": ad_id,
            "imagen": ad["imagen"],
            "tags": ad["tags"],
            "prioridad": round(-neg_priority, 3),
            "categoria": categoria.capitalize(),
            "emoji": theme["emoji"],
            "color": theme["color"],
        })

    return result
