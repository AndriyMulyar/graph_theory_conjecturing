from sage.all import *

def is_2_bootstrap_good(G):
    return ktBootstrappable(G,2,2)

def ktBootstrappable(G, num_for_spread, num_initial_infected):
    """
    Checks if a graph is vertex bootstrap percolatable by considering every valid subset of num_for_spread starting
    vertices and percolating.

    :param G: a sage Graph object
    :param num_for_spread: the number of neighboring infected vertices required for spread
    :param num_initial_infected: the number of vertices initially infected
    :return: true is bootstrap percolatable, false otherwise
    """
    if G.order() <= num_initial_infected: # If all vertices can be infected initially...
        return True

    # grab initially isolated vertices
    isolated_vertices = isolatedVertices(G,num_for_spread,num_initial_infected)


    if len(isolated_vertices) >= num_initial_infected: # If there are more cells that need to be infected than there are initially infected cells...
        return False # ... no subset of vertices can infect every cell.

    S=Subsets(set(G.vertices()).difference(isolated_vertices), num_initial_infected - len(isolated_vertices)) # S is the set of subsets of G's vertices that we can infect initially, not including any isolated cells

    for s in S:
        s=set(s).union(isolated_vertices) # s includes all isolated cells, which we know must be included because they can't be reached otherwise (by definition)
        if percolate(num_for_spread,G,s):
            return True
    return False

def isolatedVertices(G,num_for_spread,num_initial_infected):
    """
    Computes a list of vertices that are not candidates seeds for successful percolation.
    :param G:
    :param num_for_spread:
    :param num_initial_infected:
    :return:
    """
    isolated_vertices = set() # we want to keep track of (and return) which vertices have few enough neighbors that they can't be infected by them
    count=0 # count of isolated vertices, which is what we might call them

    for v in G.vertices():
        if G.degree()[v] < num_for_spread: #if a vertex has a degree smaller than spread num then it cannot serve as part of an initial subset
            isolated_vertices.add(v);
            count += 1
        if count >= num_initial_infected: # If there are isolated vertices that aren't infected initially...
            break # ... it's impossible to bootstrap this graph, so give up.
    return isolated_vertices

def percolate(num_for_spread,G,initial):
    """
    Attempts to percolate G from the initial set of vertices by infecting adjacent vertices of already infected vertices
    if an un-infected vertex has num_for_spread infected neighbors
    :param num_for_spread:
    :param G:
    :param initial:
    :return: returns true if all vertices reached
    """
    G.relabel()
    neighbs=[0]*G.order()
    uninfected=[]
    for v in G.vertices():
        if v in initial:
            for s in G.neighbors(v):
                neighbs[s] += 1
        else:
            uninfected.append(v)

    # while we have vertices to infect
    while len(uninfected) > 0:
        new_vertex_infected = False

        #single infection timestep
        for v in uninfected:
            if neighbs[v] >= num_for_spread:
                new_vertex_infected = True
                uninfected.remove(v)
                for s in G.neighbors(v):
                    neighbs[s] += 1

        if not new_vertex_infected: #subsequent timesteps will not reduce the uninfected vertex set
            return False
    return True