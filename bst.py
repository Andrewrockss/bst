'''Contains an implementation of a binary search tree (BST).'''


class BST:
    '''A data structure similar to Python's built-in set, but implemented
    using a binary search tree (BST) instead of a hash table.
    '''

    def __init__ (self, iterable=None):
        '''Creates a binary search tree containing the keys in iterable, if
        specified.
        '''
        self.root = None
        if iterable is not None:
            for key in iterable:
                self.add(key)

    def add (self, key):
        '''Adds key to the BST, replacing any equivalent keys that are already
        present.'''
        if self.root is None:
            self.root = BSTNode(key, parent=None)
        else:
            ins = self.root.insertion_point(key)
            if key < ins.key:
                ins.left = BSTNode(key, parent=ins)
            elif ins.key < key:
                ins.right = BSTNode(key, parent=ins)
            else:
                ins.key = key

    def __contains__ (self, key):
        '''Implementation of Python expression 'key in bst'. Returns whether
        key is in the binary search tree.
        '''
        if self.root is None:
            return False
        else:
            ins = self.root.insertion_point(key)
            return not (key < ins.key or ins.key < key)

    def remove (self, key):
        '''Removes key from self if it exists. Otherwise raises KeyError(key).
        Returns: None
        '''
        raise NotImplementedError('deleting BST keys is not yet implemented')

    def __repr__ (self):
        '''Called whenever Python needs a string representation of BST, for
        example with repr(bst), str(bst), or when you type 'bst' at
        the Python interpreter.
        '''
        return repr(self.root) if self.root else '<empty tree>'

    def __nonzero__ (self):
        '''Called when self is used in a boolean context, e.g. as the
        condition in an if statement: "if bst: ...". Returns whether
        tree is empty
        '''
        return self.root is not None


class BSTNode:

    def __init__ (self, key, parent):
        '''Creates a BSTNode with given key and parent, and empty left and
        right subtrees.
        '''
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

    def insertion_point (self, key):
        '''Returns: The last valid BSTNode on the path from the root of this
        subtree to the location where key should be inserted.
        Post-conditions: The return value 'ins' satisfies exactly one of:
          * key < ins.key and ins.left is None
          * ins.key < key and ins.right is None
          * key == ins.key; more precisely, not(key < ins.key or ins.key < key)
        '''
        node = self
        while True:
            if key < node.key:
                next_node = node.left
            elif node.key < key:
                next_node = node.right
            else:
                next_node = None
            if next_node is None:
                return node
            else:
                node = next_node

    def max_depth (self):
        '''Returns: The maximum depth of this subtree, i.e. the length of the
        longest path from the root to a leaf.  This is the worst-case
        running time of self.insertion_point().
        '''
        left_depth = self.left.max_depth() if self.left else 0
        right_depth = self.right.max_depth() if self.right else 0
        return 1 + max(left_depth, right_depth)

    def __repr__ (self):
        '''Returns: a string representation of this subtree with the format
        <left key right>, where 'left' and 'right' are
        representations of the subtrees and 'key' is the key at the
        current node (empty subtrees are represented by a '.').
        Examples:
          * A leaf with key 5 is '<. 5 .>'
          * After adding keys 2, 7 and 6: '<<. 2 .> 5 <<. 6 .> '7' .>>'
        '''
        left_str = str(self.left) if self.left else '.'
        right_str = str(self.right) if self.right else '.'
        return '<{} {} {}>'.format(left_str, repr(self.key), right_str)
