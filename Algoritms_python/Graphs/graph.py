import networkx as nx
import matplotlib as plt


G = nx.Graph()
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'E', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('C', 'E', weight=3)
G.add_edge('D', 'C', weight=4)
G.add_edge('A', 'C', weight=5)


def graf(first: str, second: str):
    # расчет кратчайших путей для ВСЕХ пар вершин
    predecessors, _ = nx.floyd_warshall_predecessor_and_distance(G)
    # кратчайший путь от вершины [A] к вершине [B]
    shortest_path_s_v = nx.reconstruct_path(first, second, predecessors)
    ccc = shortest_path_s_v
    # список ребер кратчайшего пути
    edges = [(a,b) for a,b in zip(shortest_path_s_v, shortest_path_s_v[1:])]
    # список всех весов ребер
    weights = nx.get_edge_attributes(G, 'weight')
    # позиции вершин для визуализации графа
    #pos = nx.spring_layout(G)
    pos = nx.circular_layout(G)
    # рисуем граф
    nx.draw_networkx(G, pos=pos)
    # рисуем веса ребер
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    # рисуем кратчайший путь: [A] -> [B]
    nx.draw_networkx_edges(G, pos=pos, edgelist=edges, edge_color="r", width=3)
    # заголовок графика
    title = "Shortest path between [{}] and [{}]: {}"\
            .format("A", "D", " -> ".join(shortest_path_s_v))
    # plt.title(title)
    a = []
    b = []
    c = [] 
    for p in nx.all_simple_paths(G,first, second):
        print(p)  
        if len(p) == 2:
            a.append("yes")
        else:
            a.append("no")   
        if len(p) == 3:
            b.append("yes")
        else:
            b.append("no")  
        if len(p) == 4:
            c.append("yes")
        else:
            c.append("no")  
    if "yes" in a:
        print("a) yes")
    else:
        print("a) no")
    if "yes" in b:
        print("b) yes")
    else:
        print("b) no")
    if "yes" in c:
        print("c) yes")
    else:
        print("c) no")



graf('D', 'C')
