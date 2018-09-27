'''
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
 which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    rtrn = root.val + " "
    if root.left is not None:
        rtrn += serialize(root.left)
    else:
        rtrn += "-1 "
    if root.right is not None:
        rtrn += serialize(root.right)
    else:
        rtrn += "-1 "
    return rtrn


def deserialize(s):
    conv_list = str(s).split()
    if len(conv_list) is 0 or conv_list[0] is "-1":
        return None
    root = Node(conv_list.pop(0))
    root.left = deserialize(' '.join(conv_list))
    currNode = root.left
    while currNode is not None:
        conv_list.pop(0)
        currNode = currNode.left
    root.right = deserialize(' '.join(conv_list))
    currNode = root.right
    while currNode is not None:
        conv_list.pop(0)
        currNode = currNode.right
    return root


node = Node('root', Node('left', Node('left.left')), Node('right'))
deserialize(serialize(node))
print(deserialize(serialize(node)).left.left.val)
assert deserialize(serialize(node)).left.left.val == 'left.left'
print(serialize(node))
print(serialize(deserialize(serialize(node))))
#assert deserialize(serialize(node)).right.val == 'right'