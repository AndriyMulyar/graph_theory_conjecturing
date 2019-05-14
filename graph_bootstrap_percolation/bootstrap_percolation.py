from sage.all import *

def is_2_bootstrap_good(G):
    return ktBootstrappable(G,2,2)

# k is the number of adjacent infected cells it takes to become infected, t is the number of initially infected cells
def ktBootstrappable(G,k,t):
    n=G.order()
    V=G.vertices()
    if n <= t: # If all vertices can be infected initially...
        return true # ... the graph must be good.

    iVerts=isolatedVertices(G,k,t,V)
    if iVerts.cardinality >= t: # If there are more cells that must be initially infected than there are initially infected cells...
        return false # ... no subset of vertices can infect every cell.
    S=Subsets(G.vertices().difference(iVerts), t-iVerts.cardinality) # S is the set of subsets of G's vertices that we can infect initially, not including any isolated cells
    for s in S:
        s=s.union(iVerts) # s includes all isolated cells, which we know must be included because they can't be reached otherwise (by definition)
        if percolate(k,G,s,n,V):
            return true
    return false

def isolatedVertices(G,k,t,V):
    iVerts=graphs.EmptyGraph # we want to keep track of (and return) which vertices have few enough neighbors that they can't be infected by them
    count=0 # count of isolated vertices, which is what we might call them
    for v in V:
        if v.degree() < k:
            iVerts += v;
            count += 1
        if count >= t: # If there are isolated vertices that aren't infected initially...
            break # ... it's impossible to bootstrap this graph, so give up.
    return iVerts

def percolate(k,G,initial,n,V):
    G.relabel()
    neighbs=[0]*n
    uninfected=[]
    for v in V:
        if v in initial:
            for s in G.neighbors(v):
                neighbs[s]=neighbs[s]+1
        else:
            uninfected.append(v)
    while not len(uninfected)==0:
        flaggity=0
        for v in uninfected:
            if neighbs[v]>k-1:
                flaggity=1
                uninfected.remove(v)
                for s in G.neighbors(v):
                    neighbs[s]=neighbs[s]+1
        if len(uninfected)==0:
            return true
        if not flaggity:
            return false
    return true