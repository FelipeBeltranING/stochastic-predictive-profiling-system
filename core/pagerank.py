def compute_pagerank(G, alpha=0.85, personalization=None, max_iter=100, tol=1e-06):
    
    nodos = list(G.nodes())
    N = len(nodos)
    if N == 0:
        return {}

    if personalization is None:
        p = {nodo: 1.0 / N for nodo in nodos}
    else:
        suma_p = sum(personalization.values())
        p = {nodo: personalization.get(nodo, 0.0) / suma_p for nodo in nodos}

    pagerank = {nodo: 1.0 / N for nodo in nodos}

    for _ in range(max_iter):
        nuevo_pagerank = {nodo: 0.0 for nodo in nodos}
        suma_dangling = 0.0 

        for nodo in nodos:
            out_edges = G.out_edges(nodo, data=True)
            
            if len(out_edges) == 0:
                suma_dangling += pagerank[nodo]
            else:
                total_weight = sum(data.get('weight', 1.0) for _, _, data in out_edges)
                
                for _, vecino, data in out_edges:
                    peso_arista = data.get('weight', 1.0)
                    participacion = pagerank[nodo] * (peso_arista / total_weight)
                    nuevo_pagerank[vecino] += participacion

        error = 0.0
        for nodo in nodos:
            enlaces_directos = alpha * nuevo_pagerank[nodo]
            nodos_fantasma = alpha * suma_dangling * p[nodo]
            teletransportacion = (1.0 - alpha) * p[nodo]
            
            valor_final = enlaces_directos + nodos_fantasma + teletransportacion
            
            error += abs(valor_final - pagerank[nodo])
            nuevo_pagerank[nodo] = valor_final

        pagerank = nuevo_pagerank

        if error < tol:
            break

    return pagerank