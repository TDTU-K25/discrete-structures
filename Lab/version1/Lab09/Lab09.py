import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def draw_graph(G):
    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, font_size=10, node_size=800,
            node_color='lightblue', edge_color='gray')

    if (nx.is_weighted(G)):
        edge_labels = nx.draw_networkx_edge_labels(G, font_size=6,
                                                   pos=pos, label_pos=0.5)
    plt.show()

# Exercise 1


def ex1_a():
    G = nx.Graph()
    G.add_edge(1, 4)
    G.add_edge(2, 4)
    G.add_edge(3, 4)
    draw_graph(G)


# ex1_a()


def ex1_b():
    G = nx.Graph()
    G.add_edge(1, 2)
    G.add_edge(1, 4)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    draw_graph(G)

# ex1_b()


def ex1_c():
    G = nx.Graph()
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 4)
    draw_graph(G)

# ex1_c()

# Exercise 2


def graph_ex2():
    G = nx.Graph()
    G.add_edge('A', 'B', weight=1)
    G.add_edge('B', 'D', weight=2)
    G.add_edge('B', 'E', weight=3)
    G.add_edge('D', 'E', weight=5)
    G.add_edge('A', 'E', weight=2)
    G.add_edge('A', 'C', weight=4)
    G.add_edge('C', 'F', weight=6)
    G.add_edge('C', 'G', weight=7)
    return G

# draw_graph(graph_ex2())


def ex2_b(G):
    print("Shortest path from A to D:",
          nx.shortest_path(G, 'A', 'D', weight='weight'))
    print("Shortest path from G to D:",
          nx.shortest_path(G, 'G', 'D', weight='weight'))
    print("Shortest path from D to C:",
          nx.shortest_path(G, 'D', 'C', weight='weight'))


# ex2_b(graph_ex2())

# Exercise 3

def graph_ex3():
    G = nx.Graph()
    G.add_edge(0, 1, weight=3)
    G.add_edge(2, 3, weight=2)
    G.add_edge(0, 3, weight=7)
    G.add_edge(0, 4, weight=8)
    G.add_edge(1, 2, weight=1)
    G.add_edge(1, 3, weight=4)
    G.add_edge(3, 4, weight=3)
    return G

# draw_graph(graph_ex3())


def ex3_b(G):
    print(nx.convert_matrix.to_numpy_array(G))


# ex3_b(graph_ex3())


def ex3_c(G):
    print("Shortest path from 2 to 4:",
          nx.shortest_path(G, 2, 4, weight='weight'))

# ex3_c(graph_ex3())

# Exercise 4


def graph_ex4():
    G = nx.Graph()
    G.add_edge('v1', 'v2', weight=5)
    G.add_edge('v1', 'v3', weight=6)
    G.add_edge('v2', 'v3', weight=8)
    G.add_edge('v2', 'v4', weight=3)
    G.add_edge('v2', 'v5', weight=4)
    G.add_edge('v3', 'v5', weight=6)
    G.add_edge('v4', 'v5', weight=3)
    G.add_edge('v4', 'v6', weight=7)
    G.add_edge('v5', 'v6', weight=7)
    return G

# draw_graph(graph_ex4())


def ex4_b(G):
    print(nx.convert_matrix.to_numpy_array(G))


# ex4_b(graph_ex4())


def ex4_c(G):
    print("Shortest path from v1 to v6:",
          nx.shortest_path(G, 'v1', 'v6', weight='weight'))

# ex4_c(graph_ex4())


def ex4_d(G):
    weighted_matrix = nx.convert_matrix.to_numpy_array(G)
    adjacency_matrix = np.empty(
        (len(weighted_matrix), len(weighted_matrix[0])))
    for i in range(0, len(weighted_matrix)):
        for j in range(0, len(weighted_matrix[i])):
            if (weighted_matrix[i][j] != 0):
                adjacency_matrix[i][j] = 1
            else:
                adjacency_matrix[i][j] = 0
    print(adjacency_matrix)

# ex4_d(graph_ex4())


def ex4_e(G):
    all_paths = nx.all_simple_paths(G, 'v1', 'v6')
    list_path_length_3_from_v1_to_v6 = []
    for path in all_paths:
        if (len(path) == 3):
            list_path_length_3_from_v1_to_v6.append(path)
    print("Number of paths with length 3 from v1 to v6:",
          len(list_path_length_3_from_v1_to_v6))


# ex4_e(graph_ex4())
