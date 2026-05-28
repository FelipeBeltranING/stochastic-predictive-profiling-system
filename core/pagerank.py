import networkx as nx

def compute_pagerank(G, alpha=0.85, personalization=None, max_iter=100, tol=1e-06,
                     nstart=None, weight='weight', dangling=None):

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