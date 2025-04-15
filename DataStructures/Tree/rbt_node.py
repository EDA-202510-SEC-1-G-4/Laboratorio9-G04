RED = 0
BLACK = 1

def new_node(key, value, color=RED):
    node = {
        "key": key,
        "value": value,
        "size": 1,
        "left": None,
        "right": None,
        "color": color,
        "type": "RBT",
    }

    return node

def is_red(my_node):
    return my_node["color"] == RED

def get_value(my_node):
    value = None
    if my_node is not None:
        value = my_node["value"]
    return value

def get_key(my_node):
    key = None
    if my_node is not None:
        key = my_node["key"]
    return key

def change_color(my_node, color):
    my_node["color"] = color

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
        change_color(node,1)
    elif node['color'] == 1:
        change_color(node,0)
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
    return

def put(rbt,key,value):
    return
