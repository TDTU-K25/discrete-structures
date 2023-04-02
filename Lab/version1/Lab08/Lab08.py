from matplotlib import pyplot as plt
import networkx as nx
import numpy as np


def draw_graph(A: list[list], vertices: str):
    G = nx.from_numpy_array(A)
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos=pos, with_labels=True, labels={a: b for
                                                           a, b in enumerate(vertices)})
    edge_labels = nx.draw_networkx_edge_labels(G, font_size=6,
                                               pos=pos, label_pos=0.5)
    plt.axis('equal')
    plt.show()


# Exercise 2
A1 = np.array([[0, 0, 3, 0, 1], [0, 0, 5, 3, 0], [
              3, 5, 0, 1, 0], [0, 3, 1, 0, 2], [1, 0, 0, 2, 0]])
# draw_graph(A1, 'abcde')

A2 = np.array([[0, 0, 0, 0, 1, 1], [0, 0, 5, 3, 0, 0], [0, 5, 0, 1, 5, 0], [
              0, 3, 1, 0, 2, 3], [1, 0, 5, 2, 0, 6], [1, 0, 0, 3, 6, 0]])
# draw_graph(A2, 'abcdef')


# Exercise 3
A = np.array([[0, 0, 5, 3, 0, 0], [0, 0, 3, 2, 0, 0], [5, 3, 0, 1, 3, 0], [
             3, 2, 1, 0, 1, 3], [0, 0, 3, 1, 0, 4], [0, 0, 0, 3, 4, 0]])
# draw_graph(A, 'abcdef')

B = np.array([[0, 0, 2, 3, 3, 0], [0, 0, 3, 2, 0, 0], [2, 3, 0, 2, 8, 6], [
             3, 2, 2, 0, 0, 5], [3, 0, 8, 0, 0, 3], [0, 0, 6, 5, 3, 0]])
# draw_graph(B, 'abcdef')


# Exercise 5

def ex5():
    G = nx.Graph()

    G.add_nodes_from(['Monkeys', 'Apes', 'Gorillas', 'Primates', 'Mice', 'Squirrels', 'Beavers', 'Rodents', 'Crocodiles', 'Komodo dragons', 'Lizards', 'Reptiles',
                     'Coconut trees', 'Grasses', 'Oaks', 'Plants', 'Mushrooms', 'Molds', 'Yeasts', 'Fungi', 'Mammals', 'Animals',  'Multicellular organisms', 'Unicellular organisms'])

    G.add_edges_from([('Monkeys', 'Primates'), 
                      ('Apes', 'Primates'), 
                      ('Gorillas', 'Primates'), 
                      ('Mice', 'Rodents'), 
                      ('Squirrels', 'Rodents'),
                      ('Beavers', 'Rodents'),  
                      ('Crocodiles', 'Reptiles'),
                      ('Komodo dragons', 'Reptiles'), 
                      ('Lizards', 'Reptiles'),
                      ('Coconut trees', 'Plants'), 
                      ('Grasses', 'Plants'), 
                      ('Oaks', 'Plants'), 
                      ('Mushrooms', 'Fungi'), 
                      ('Molds', 'Fungi'),
                      ('Yeasts', 'Fungi'),
                      ('Primates', 'Mammals'),
                      ('Rodents', 'Mammals'),
                      ('Mammals', 'Animals'),
                      ('Rodents', 'Animals'),
                      ('Reptiles', 'Animals'),
                      ('Animals', 'Multicellular organisms'),
                      ('Plants', 'Multicellular organisms'),
                      ('Mushrooms', 'Multicellular organisms'),
                      ('Molds', 'Multicellular organisms'),
                      ('Yeasts', 'Unicellular organisms')])

    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, font_size=10, node_size=800,
            node_color='lightblue', edge_color='gray')

    plt.show()

# ex5()