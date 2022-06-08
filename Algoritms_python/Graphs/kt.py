graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
 

def bfs(graph, start, end):
    stack = [(start, [start])]  
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == end:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
            path

l = list(bfs(graph, 'B', 'F'))
# print(l)
arr = []
for i in range(len(l)):
    a  = len(l[i])
    arr.append(a)
c = min(arr) -1
print(f'{c}$')
    


# set(graph[vertex]) - {'E', 'A', 'D'}
#                      {'E', 'A', 'D'}
#                      {'E', 'A', 'D'}
#                      {'C', 'B'}
#                      {'F', 'A'}
#                      {'F', 'B'}


# set(path) - {'B'}
#             {'B'}
#             {'B'}
#             {'A', 'B'}
#             {'C', 'A', 'B'}
#             {'E', 'B'}


# stack - [('B', ['B'])]


# vertex - B
        #  D
        #  A
        #  C
        #  E


# path - ['B']
        #['B', 'D']
        #['B', 'A']
        #['B', 'A', 'C']
        #['B', 'E']


# next - E
        # A
        # D
        # C
        # F
        # F


# path + [next] - ['B', 'A', 'C', 'F']
#                 ['B', 'E', 'F']


# next, path + [next] - 
                    # F ['B', 'A', 'C', 'F']
                    # F ['B', 'E', 'F']






