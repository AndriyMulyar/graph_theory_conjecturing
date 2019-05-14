from sage.all import *
from bootstrap_percolation import is_2_bootstrap_good
from conjecturing import propertyBasedConjecture
from pprint import pprint

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

not_applicable_to_all = ['is_cartesian_product', 'is_circumscribable', 'is_inscribable']

sage_all_computable_properties = ['is_apex', 'is_arc_transitive', 'is_asteroidal_triple_free', 'is_biconnected', 'is_bipartite', 'is_block_graph',
                                  'is_cactus', 'is_cayley', 'is_chordal', 'is_circulant', 'is_circular_planar',
                                  'is_clique', 'is_cograph', 'is_connected',
                                  'is_cycle', 'is_directed', 'is_distance_regular', 'is_drawn_free_of_edge_crossings',
                                  'is_edge_transitive', 'is_eulerian', 'is_even_hole_free', 'is_forest',
                                  'is_gallai_tree', 'is_half_transitive', 'is_hamiltonian', 'is_immutable', 'is_independent_set',
                                   'is_interval', 'is_long_antihole_free',
                                  'is_long_hole_free', 'is_odd_hole_free', 'is_overfull', 'is_partial_cube', 'is_perfect',
                                  'is_planar', 'is_polyhedral', 'is_prime', 'is_regular', 'is_self_complementary',
                                  'is_semi_symmetric', 'is_split', 'is_strongly_regular', 'is_transitively_reduced',
                                  'is_tree', 'is_triangle_free', 'is_vertex_transitive', 'is_weakly_chordal']

only_connected_graphs = ['szeged_index']
sage_efficient_invariants = ['number_of_loops', 'density', 'order', 'size', 'average_degree',
                             'triangles_count', 'radius', 'diameter', 'girth', 'wiener_index',
                             'average_distance', 'connected_components_number',
                             'spanning_trees_count', 'odd_girth', 'clustering_average', 'cluster_transitivity']

sage_intractable_invariants = ['chromatic_number', 'chromatic_index', 'treewidth',
                               'clique_number', 'pathwidth', 'fractional_chromatic_index', 'edge_connectivity',
                               'vertex_connectivity', 'genus', 'crossing_number']


properties = custom_properties + list(set([getattr(Graph, property) for property in sage_all_computable_properties]))



graph_property_cache = {}
all_non_isomorphic_graphs_below_order= []
for graph in generate_non_isomorphic_graphs(7):
    all_non_isomorphic_graphs_below_order.append(graph)
    #graph_property_cache[graph.graph6_string()] = {property.__name__ : property(graph) for property in properties}




propertyBasedConjecture(objects=all_non_isomorphic_graphs_below_order,
                        properties=properties,
                        mainProperty=0,
                        verbose=True,
                        debug=True)






