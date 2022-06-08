from itertools import cycle
import networkx as nx
import matplotlib as plt
from networkx import minimum_cycle_basis

G = nx.Graph()
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'E', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('C', 'E', weight=3)
G.add_edge('D', 'C', weight=4)
G.add_edge('A', 'C', weight=5)

# print(find_cycle(G))
# print(minimum_cycle_basis(G))
print([sorted(c) for c in nx.minimum_cycle_basis(G)])

"""
Возвращает базовый цикл минимального веса для G
Минимальный вес означает базис цикла, 
для которого суммарный вес 
(длина невзвешенных графов) всех циклов минимален.
"""

