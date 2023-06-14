from igraph import Graph, Edge, Vertex

def random_graph(n: int, p: float) -> Graph:
  return Graph.Erdos_Renyi(n=n, p=p)


