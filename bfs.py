def BFS(tree,level=["A"]):
  bfs_list = []
  if len(level) > 0:
    bfs_list += level
    sub_level = []
    for vertex in level:
      if vertex not in tree:
        continue
      sub_level += tree[vertex]
    bfs_list += BFS(tree,sub_level)
  return bfs_list

tree = {"A" : ["C", "D"],
        "C" : ["P","R","L"],
        "R" : ["O","E"],
        "G" : ["N", "M"],
        "Q" : ["G", "H"],
        "D" : ["F", "Q", "S"],
        "P" : [],
        "L" : [],
        "N" : [],
        "M" : [],
        "H" : [],
        "S" : [],
        "F" : [],
        "O" : [],
        "E" : []}

print(BFS(tree))