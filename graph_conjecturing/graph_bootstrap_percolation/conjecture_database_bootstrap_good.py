from sage.all import *
from bootstrap_percolation import is_2_bootstrap_good
from graph_conjecturing.precomputed_cache.gt_precomputed_database import get_connection, precomputed_only_property_conjecture
from graph_conjecturing.graph_theory.graph_theory import properties
from sage.graphs.graph_input import from_graph6



custom_properties = [is_2_bootstrap_good]
target_properties = [] #holds properties to be used during conjecturing



database_file = "/home/andriy/Documents/school/ML/projects/2019_Graph_Conjecturing/graph_theory_conjecturing/graph_conjecturing/precomputed_cache/gt_precomputed_database.db"
conn = get_connection(database=database_file)
conn.text_factory = str
graphs_from_db = []

#Retrieves all properties with over a certain number of graphs, filters properties from gt.sage to this list and
#adds to the properties to use during conjecturing.
result = conn.execute('select property, count(graph) from main.prop_values GROUP BY property HAVING count(graph) > 7000;')
sufficient_props = [row[0] for row in result.fetchall()]
for property in properties:
    if property.__name__ in sufficient_props:
        target_properties.append(property)



#get our graphs
result = conn.execute("select distinct graph from main.prop_values where property like 'is_2_bootstrap_good' LIMIT 10000")

for graph in result.fetchall():
    g = Graph()
    from_graph6(g, graph[0])
    graphs_from_db.append(g) #turn the graph6 string into a sage graph object

conn.close()


properties = custom_properties + target_properties

#remove some properties from the final list
removed_properties = ['is_clique', 'is_dirac']
properties = [property for property in properties if property.__name__ not in removed_properties]

print([property.__name__ for property in properties])


#give this a list of objects we have compute 2BG for, it will filter out those that are missing values for any of our properties
precomputed_only_property_conjecture(graphs_from_db,
                                     properties,
                                     mainProperty=0,
                                     precomputed_db=database_file,
                                     debug=True,
                                     verbosity=2)