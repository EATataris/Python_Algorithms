class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.root >= new_node:
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        else:
            raise Exception('Неверное значение')

    def insert_right(self, new_node):
        if self.root <= new_node:
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        else:
            raise Exception('Неверное значение')

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
# r.insert_left(25)
r.insert_left(7)
print(r.get_left_child())
r.insert_left(6)
print(r.get_left_child().get_root_val())
# r.insert_right(7)
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
