# dct = { 1: [4, 7] }
# тут узлы могут иметь совпадающие значения
tree = {
    0: [1, 1, 2],
    1: [4, 3, 4],
    2: [3, 5, 6],
    3: [3, None, None],
    4: [7, 9, None],
    5: [4, None, None],
    6: [7, None, None],
    9: [1, None, None]
}

# print(tree.keys())  # все узлы

def get_max_path(root):
    if root == None: return 0
    left_path_max = get_max_path(tree[root][1])
    right_path_max = get_max_path(tree[root][2])
    return tree[root][0] + max(left_path_max, right_path_max)


root = 0
print(get_max_path(root))

'''
          1
    4          3
 3     7    4     7 
N N   1 N  N N   N N

'''