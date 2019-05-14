from sage.all import *
from bootstrap_percolation import is_2_bootstrap_good

def generate_non_isomorphic_graphs(n):
    """
    A generater yeilding all non-isomorphic graphs of increasing order up to order n.
    http://doc.sagemath.org/html/en/reference/graphs/sage/graphs/graph_generators.html?highlight=graph_gen#module-sage.graphs.graph_generators
    :param n:
    :return: a yielding generator
    """

    for i in range(2,n+1):
        for graph in graphs(i, implementation='c_graph'):
            yield graph


for graph in generate_non_isomorphic_graphs(10):
    print(graph.order())
    print(graph.graph6_string())

