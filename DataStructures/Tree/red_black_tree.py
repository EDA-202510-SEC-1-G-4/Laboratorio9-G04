from DataStructures.Tree import rbt_node as rbn
from DataStructures.List import array_list as al

def new_map():
    rbt = {'root':None,
           'type':'RBT'}
    return rbt


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

def balance(root):
    if root['color'] == 0 and root['left']['color'] == 0:
        root = rotate_left(root)
    elif root['right']['color'] == 0:
        root = rotate_right(root)
    return root
        

def put(rbt,key,value):
    rbt['root'] = insert_node(rbt['root'],key,value)
    return rbt

#Falta el recorrido de verificación para balanceo
