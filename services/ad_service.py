import heapq
from database.data_store import publicidad

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
    priority_queue = []

    for ad_id, ad in publicidad.items():
        priority = 0.0
        for tag in ad["tags"]:
            user_interest = user_profile.get(tag, 0.0)
            priority += user_interest * ad["prioridad_base"]

        heapq.heappush(priority_queue, (-priority, ad_id))

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
