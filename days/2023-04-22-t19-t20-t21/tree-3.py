# dct = { 1: [4, 7] }
# тут узлы могут иметь совпадающие значения
tree = [ 1, 4, 3, 3, 7, 4, 7, 0, 0, 1, ]

def get_max_path(root):
    if root >= len(tree): return 0
    left_path_max = get_max_path(root*2+1)
    right_path_max = get_max_path(root*2+2)
    return tree[root] + max(left_path_max, right_path_max)


root = 0
print(get_max_path(root))

'''
          1
    4          3
 3     7    4     7 
N N   1 N  N N   N N

'''