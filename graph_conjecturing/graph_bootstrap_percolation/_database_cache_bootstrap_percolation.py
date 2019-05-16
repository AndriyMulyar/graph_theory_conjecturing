from graph_conjecturing.precomputed_cache.gt_precomputed_database import get_connection, update_property_database, verify_property_values
from sage.all import *
from sage.graphs.graph_input import from_graph6
from bootstrap_percolation import is_2_bootstrap_good
import sqlite3

conn = get_connection(database="/home/andriy/Documents/school/ML/projects/2019_Graph_Conjecturing/graph_theory_conjecturing/graph_conjecturing/precomputed_cache/gt_precomputed_database.db")
conn.text_factory = str


#result = conn.execute("select distinct graph from prop_values ORDER BY length(graph)")
result = conn.execute("select graph from main.prop_values where property like 'is_2_bootstrap_good' and value is 0")
#cursor.execute("SELECT name FROM main.prop_values WHE")

graphs_from_db = []

for graph in result.fetchall():
    g = Graph()
    from_graph6(g, graph[0])
    graphs_from_db.append(g)

# update_property_database([is_2_bootstrap_good],
#                          graphs_from_db,
#                          database="/home/andriy/Documents/school/ML/projects/2019_Graph_Conjecturing/graph_theory_conjecturing/graph_conjecturing/precomputed_cache/gt_precomputed_database.db",
#                          verbose=True
#                          )


verify_property_values([is_2_bootstrap_good],
                         graphs_from_db,
                         database="/home/andriy/Documents/school/ML/projects/2019_Graph_Conjecturing/graph_theory_conjecturing/graph_conjecturing/precomputed_cache/gt_precomputed_database.db"
                         )









