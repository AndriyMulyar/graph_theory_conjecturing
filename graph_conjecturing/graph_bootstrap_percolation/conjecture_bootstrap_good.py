from sage.all import *
from bootstrap_percolation import is_2_bootstrap_good
from graph_conjecturing.graph_theory.conjecturing import propertyBasedConjecture
from graph_conjecturing.graph_theory.graph_theory import efficiently_computable_properties, sage_graphs


#counter_examples, problem_graphs, sage_graphs, all_graphs,
def generate_non_isomorphic_graphs(n):
    """
    A generater yeilding all non-isomorphic graphs of increasing order up to order n.
    http://doc.sagemath.org/html/en/reference/graphs/sage/graphs/graph_generators.html?highlight=graph_gen#module-sage.graphs.graph_generators
    :param n:
    :return: a yielding generator
    """

    for i in range(2,n+1):
        for graph in graphs(i, implementation='c_graph'): #utilize implementation from nauty
            yield graph


custom_properties = [is_2_bootstrap_good]







properties = custom_properties + efficiently_computable_properties




# print(len(problem_graphs))
# print(len(sage_graphs))
# print(len(all_graphs))
# exit()
# graph_property_cache = {}
# all_non_isomorphic_graphs_below_order= []
# for graph in generate_non_isomorphic_graphs(7):
#     all_non_isomorphic_graphs_below_order.append(graph)
    #graph_property_cache[graph.graph6_string()] = {property.__name__ : property(graph) for property in properties}


# class0small + counter_examples + problem_graphs + sage_graphs

propertyBasedConjecture(objects= sage_graphs ,
                        properties=properties,
                        mainProperty=0,
                        verbose=True,
                        sufficient=True,
                        time=5,
                        debug=True)






