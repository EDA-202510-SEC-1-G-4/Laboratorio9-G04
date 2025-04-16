from DataStructures.Tree import rbt_node as rbn
from DataStructures.List import array_list as al

def rotate_left(node):
    if node != None and node['right'] == None:
        prin = node['left']
        left = node['left']['left']
        right = node
        node = prin
        node['left'] = left
        node['right'] = right
    elif node != None and node['right'] != None:
        prin = node['left']
        left = node['left']['left']
        right = node
        right2 = node['right']['right']
        node = prin
        node['left'] = left
        node['right'] = right
        node['right']['right'] = right2
    return node

def rotate_right(node):
    if node != None and node['right'] != None:
        prin = node['right']
        left = node
        node = prin
        node['left'] = left
    return

def flip_node_color(node):
    if node['color'] == 0:
        rbn.change_color(node,1)
    elif node['color'] == 1:
        rbn.change_color(node,0)
    return node

def flip_colors(node):
    if node != None:
        flip_node_color(node)
        if node['right'] != None:
            flip_node_color(node['right'])
        if node['left'] != None:
            flip_node_color(node['left'])
    return node

def insert_node(root,key,value):
    if root == None:
        root = rbn.new_node(key,value)
    elif root['key'] == key:
        root['value'] = value
    elif root['key'] > key:
        root = insert_node(root['left'],key,value)
    elif root['key'] < key:
        root = insert_node(root['right'],key,value)
    return root

def balanced(root,father=None):
    if father == None and root['right'] != None and root['left'] != None:
        balanced(root['left'],root)
        balanced(root['right'],root)
    elif father['color'] == 0 and root['color'] == 0 and father['left'] == root:
        father = rotate_left(father)
    elif father['right'] == root and root['color'] == 0:
        father = rotate_right(father)

    return

def put(rbt,key,value):
    if rbt != None:
        rbt['root'] = insert_node(rbt['root'],key,value)

    return
