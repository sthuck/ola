from igraph import Graph

def create_grid_graph(rows, cols):
    g = Graph(directed=False)

    # Add vertices
    for i in range(rows):
        for j in range(cols):
            g.add_vertex(name=(i, j))

    # Add edges
    for i in range(rows):
        for j in range(cols):
            if i < rows - 1:
                g.add_edge((i, j), (i + 1, j))
            if j < cols - 1:
                g.add_edge((i, j), (i, j + 1))

    return g

# Specify the number of rows and columns for the grid graph
num_rows = 2
num_cols = 2

# Create the grid graph
grid_graph = create_grid_graph(num_rows, num_cols)

# Print the graph summary
print(grid_graph.summary())

# Plot the graph (optional)
#layout = grid_graph.layout("grid")
#plot = grid_graph.plot(layout=layout, bbox=(300, 300), margin=20)
#plot.show()



