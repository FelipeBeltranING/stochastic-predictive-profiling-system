

def compute_pagerank(G, alpha=0.85, max_iter=100, tol=1e-06):
    nodes = list(G.nodes())
    N = len(nodes)
    dangling = [n for n in G.nodes() if G.out_degree(n) == 0]
    print(f"Nodos dangling: {len(dangling)}")

    pr = {n: 1.0 / N for n in nodes}

    for _ in range(max_iter):
        pr_prev = dict(pr)

        for n in nodes:
            # Suma de aportes de nodos que apuntan a n
            incoming = sum(
                pr_prev[v] / G.out_degree(v)
                for v in G.predecessors(n)
                if G.out_degree(v) > 0
            )
            pr[n] = alpha * incoming + (1 - alpha) / N

        if sum(abs(pr[n] - pr_prev[n]) for n in nodes) < tol:
            return pr

    return pr