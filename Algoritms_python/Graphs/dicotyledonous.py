"""
Проверка графа на двудольность
При прохождении по каждому ребру красим следующую вершину в противоположный цвет.
Если при переборе соседних вершин мы нашли вершину, уже покрашенную в тот же цвет,
что и текущая, то в графе существует нечётный цикл, а значит, 
он не является двудольным.
"""


import networkx as nx 
from networkx.algorithms import bipartite


B = nx.Graph()
# Добавьте узлы с атрибутом узла "bipartite"
B.add_nodes_from([1, 2, 3, 4], bipartite=0)
B.add_nodes_from(["a", "b", "c"], bipartite=1)
# Добавляйте ребра только между узлами противоположных наборов узлов
B.add_edges_from([(1, "a"), (1, "b"), 
                  (2, "b"), (2, "c"), 
                  (3, "c"), (4, "a")])


nx.draw_circular(B,
         node_size=1000,
         with_labels=True)


if bipartite.is_bipartite(B) is True: print('Двудольный граф') 
else:
    print('Не двудольный граф')


bipartite.is_bipartite(B)

""" Если True - значит граф двудольный 
    Ecли False - не двудольный 
"""

"""     
bipartite.is_bipartite(Граф неорентированный)
Этот метод проверяет, является ли граф двудольным
"""










