import networkx as nx

def compute_pagerank(G, alpha=0.85, personalization=None, max_iter=100, tol=1e-06,
                     nstart=None, weight='weight', dangling=None):
    """
    Envoltorio para networkx.pagerank que recibe los mismos parámetros y
    devuelve el diccionario de puntuaciones PageRank.

    Parámetros:
    -----------
    G : NetworkX graph
        Grafo dirigido o no dirigido.
    alpha : float, optional (default=0.85)
        Factor de amortiguación (probabilidad de seguir enlaces).
    personalization : dict, optional
        Diccionario con pesos personalizados para cada nodo.
    max_iter : int, optional (default=100)
        Número máximo de iteraciones.
    tol : float, optional (default=1e-06)
        Tolerancia de convergencia.
    nstart : dict, optional
        Diccionario con valores iniciales de PageRank.
    weight : string, optional (default='weight')
        Nombre del atributo de arista que se usa como peso.
    dangling : dict, optional
        Diccionario para asignar PageRank a nodos sin enlaces salientes.

    Retorna:
    --------
    pagerank : dict
        Diccionario con nodos como claves y sus puntuaciones PageRank.
    """
    return nx.pagerank(
        G=G,
        alpha=alpha,
        personalization=personalization,
        max_iter=max_iter,
        tol=tol,
        nstart=nstart,
        weight=weight,
        dangling=dangling
    )