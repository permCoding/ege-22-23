# dct = { 1: [4, 7] }
# тут все узлы разные
tree = {
    1: [4, 3],
    4: [9, 7],
    9: [None, None],
    7: [2, None],
    2: [None, None],
    3: [6, 8],
    6: [None, None],
    8: [None, None]
}

def get_max_path(root):
    if root == None: return 0
    left_path_max = get_max_path(tree[root][0])
    right_path_max = get_max_path(tree[root][1])
    return root + max(left_path_max, right_path_max)


root = 1
print(get_max_path(root))

'''
          1
    4          3
 9     7    6     8 
N N   2 N  N N   N N

'''