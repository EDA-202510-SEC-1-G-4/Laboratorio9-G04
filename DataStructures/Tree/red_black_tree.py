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
    if rbn.is_red(node):
        rbn.change_color(node,1)
    else:
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
    if root != None and root['left'] != None:
        if rbn.is_red(root) and rbn.is_red(root['left']):
            root = rotate_left(root)

    if root != None and root['right'] != None:    
        if rbn.is_red(root['right']):
            root = rotate_right(root)
    
    if root != None and root['right'] != None and root['left'] != None:
        if rbn.is_red(root['right']) and rbn.is_red(root['left']):
            root = flip_colors(root)
    return root
        

def put(rbt,key,value):
    rbt['root'] = insert_node(rbt['root'],key,value)
    rbt['root'] = balance(rbt['root'])
    if rbn.is_red(rbt['root']):
        rbn.change_color(rbt['root'],1)
    return rbt

#Falta el recorrido de verificación para balanceo
