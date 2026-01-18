import math

points = []

with open('input.txt', 'r') as f:
      for line in f:
              data = line.strip().split(",")
                  points.append(list(map(int, data)))

                  # compute distances

                  pairs = []
                  n=len(points)
                  for i in range(n):
                          for j in range(i+1,n):
                                      dist=math.dist(points[i],points[j])
                                              pairs.append((dist,i,j))

                                              pairs_sorted=sorted(pairs,key=lambda x:x[0])

                                              # Gráf szomszédsági listája
                                              from collections import defaultdict

                                              graph = defaultdict(list)

                                              for _, u, v in pairs_sorted[:1000]:
                                                      graph[u].append(v)
                                                          graph[v].append(u)

                                                          # Mélységi bejárással komponensek keresése
                                                          visited = set()
                                                          components = []

                                                          for node in graph:
                                                                  if node not in visited:
                                                                              stack = [node]
                                                                                      comp = []
                                                                                              while stack:
                                                                                                              n = stack.pop()
                                                                                                                          if n not in visited:
                                                                                                                                              visited.add(n)
                                                                                                                                                              comp.append(n)
                                                                                                                                                                              for neighbor in graph[n]:
                                                                                                                                                                                                      if neighbor not in visited:
                                                                                                                                                                                                                                  stack.append(neighbor)
                                                                                                                                                                                                                                          components.append(comp)


                                                                                                                                                                                                                                          ordered_data = sorted(components, key=len, reverse=True)
                                                                                                                                                                                                                                          answer = 1
                                                                                                                                                                                                                                          for i in ordered_data[:3]:
                                                                                                                                                                                                                                                print(i)
                                                                                                                                                                                                                                                  answer *=len(i)
                                                                                                                                                                                                                                                  print("Answer:", answer)
                                                                                                                                                                                                                    #iiii
