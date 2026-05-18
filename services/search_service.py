# services/search_service.py
"""
Motor de búsqueda predictivo basado en PageRank personalizado.
Utiliza el perfil del usuario para personalizar el ranking de productos.
"""
import networkx as nx
from core.pagerank import compute_pagerank
from database.data_store import productos


def build_product_graph(product_ids=None):
    """
    Construye un grafo dirigido donde:
    - Nodos = productos
    - Aristas = productos que comparten tags (peso proporcional a tags compartidos)
    """
    G = nx.DiGraph()

    if product_ids:
        items = {k: v for k, v in productos.items() if k in product_ids}
    else:
        items = productos

    for pid in items:
        G.add_node(pid)

    pids = list(items.keys())
    for i in range(len(pids)):
        for j in range(len(pids)):
            if i != j:
                tags_i = set(items[pids[i]]["tags"])
                tags_j = set(items[pids[j]]["tags"])
                shared = tags_i & tags_j
                if shared:
                    weight = len(shared) / max(len(tags_i), len(tags_j))
                    G.add_edge(pids[i], pids[j], weight=weight)

    return G


def get_personalization_vector(graph, user_profile):
    """
    Genera el vector de personalización para PageRank.
    Cada nodo recibe un peso según cuánto coinciden sus tags
    con los intereses del usuario.
    """
    personalization = {}
    for node in graph.nodes():
        product = productos[node]
        tags = product["tags"]
        score = sum(user_profile.get(tag, 0) for tag in tags) / max(len(tags), 1)
        personalization[node] = max(score, 0.01)
    return personalization


def search_products(query, user_profile):
    """
    Motor de búsqueda predictivo:
    1. Filtra productos que coincidan con la query
    2. Construye grafo de relaciones entre productos
    3. Ejecuta PageRank personalizado
    4. Retorna productos ordenados por relevancia

    Returns:
        tuple: (lista de productos rankeados, tags de búsqueda)
    """
    query = query.lower().strip()

    # Filtrar productos
    matching_ids = []
    for pid, product in productos.items():
        name_match = query in product["nombre"].lower()
        tag_match = any(query in tag for tag in product["tags"])
        if name_match or tag_match or query == "":
            matching_ids.append(pid)

    if not matching_ids:
        return [], []

    # Tags de los productos encontrados
    search_tags = set()
    for pid in matching_ids:
        search_tags.update(productos[pid]["tags"])

    # Construir grafo
    G = build_product_graph(matching_ids)

    # PageRank personalizado
    personalization = get_personalization_vector(G, user_profile)

    try:
        scores = compute_pagerank(G, alpha=0.85, personalization=personalization)
    except Exception:
        scores = {pid: 1.0 / len(matching_ids) for pid in matching_ids}

    # Construir resultados
    max_score = max(scores.values()) if scores else 1
    results = []
    for pid in matching_ids:
        product = productos[pid]
        raw_score = scores.get(pid, 0)
        results.append({
            "id": pid,
            "nombre": product["nombre"],
            "tags": product["tags"],
            "precio": product["precio"],
            "score": round(raw_score / max_score * 100, 1)
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results, list(search_tags)
