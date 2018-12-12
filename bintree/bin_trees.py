from modules.queue import Queue
from copy import deepcopy as deepcopy

class Node:
    def __init__(self, dataValue):
        self.dataValue = dataValue
        self.leftChild = None
        self.rightChild = None
        self.size = 1

    def compute_size(self):
        """ Computes the `self` size according to its children sizes. """
        self.size = 1
        if self.leftChild:
            self.size = self.size + self.leftChild.size
        if self.rightChild:
            self.size = self.size + self.rightChild.size

class binary_search_tree():

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.dataValue:
            if cur_node.leftChild is None:
                cur_node.leftChild = Node(value)
            else:
                self._insert(value, cur_node.leftChild)
        if value > cur_node.dataValue:
            if cur_node.rightChild is None:
                cur_node.rightChild = Node(value)
            else:
                self._insert(value, cur_node.rightChild)

    def print_tree(self, transversal_type):
        if transversal_type == "preorder":
            return self._print_preorder(self.root, "")
        elif transversal_type == "inorder":
            return self._print_inorder(self.root, "")
        elif transversal_type == "postorder":
            return self._print_postorder(self.root, "")
        else:
            print("{} does not exist".format(transversal_type))
            return False

    def _print_tree(self, root, indent, transversal = ""):

        if root is not None:
            self._print_tree(root.rightChild, indent + "   ")
            transversal += indent + str(root.dataValue)
            self._print_tree(root.leftChild, indent + "   ")
        return transversal


    def _print_preorder(self, start, transversal):
        # Root -> Left -> Right
        if start:
            transversal += (str(start.dataValue) + " - ")
            transversal = self._print_preorder(start.leftChild, transversal)
            transversal = self._print_preorder(start.rightChild, transversal)
        return transversal

    def _print_inorder(self, start, transversal):
        #Left -> Root -> Right
        if start:
            transversal = self._print_inorder(start.leftChild, transversal)
            transversal += (str(start.dataValue) + " - ")
            transversal = self._print_inorder(start.rightChild, transversal)
        return transversal

    def _print_postorder(self, start, transversal):
        #Left -> Right -> Root
        if start:
            transversal = self._print_postorder(start.leftChild, transversal)
            transversal = self._print_postorder(start.rightChild, transversal)
            transversal += (str(start.dataValue) + " - ")
        return transversal

    def search(self, value):
        if self.root!=None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value==cur_node.dataValue:
            return True
        elif value < cur_node.dataValue and cur_node.leftChild!=None:
            return self._search(value, cur_node.leftChild)
        elif value > cur_node.dataValue and cur_node.rightChild!=None:
            return self._search(value, cur_node.rightChild)
        return False

    def min_value(self, node):
        current = node
        while(current.leftChild is not None):
            current = current.leftChild
        return current

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.dataValue:
            return cur_node
        elif value < cur_node.dataValue and cur_node.leftChild != None:
            return self._find(value, cur_node.leftChild)
        elif value > cur_node.dataValue and cur_node.rightChild != None:
            return self._find(value, cur_node.rightChild)

    def getNumNodes(self):
        if self.root:
            return self._getNumNodes(self.root)
        else:
            return 0

    def _getNumNodes(self, node):
        total = 1
        if node.leftChild:
            total += self._getNumNodes(node.leftChild)
        if node.rightChild:
            total += self._getNumNodes(node.rightChild)
        return total

    def getHeight(self):
        return self._getHeight(self.root)

    def _getHeight(self, node):
        if not node:
            return 0
        else:
            return max(self._getHeight(node.leftChild), self._getHeight(node.rightChild)) + 1

    def printLevelOrder(self):
        h = self.getHeight()
        for i in range(1, h + 1):
            self._printGivenLevel(self.root, i)
            # Print nodes at a given level

    def _printGivenLevel(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.dataValue)
        elif level > 1:
            self._printGivenLevel(node.leftChild, level - 1)
            self._printGivenLevel(node.rightChild, level - 1)

    def fillTree(self, height):
        self._fillTree(self.root, height)

    def _fillTree(self, node, height):
        if height <= 1:
            return
        if node:
            if not node.leftChild: node.leftChild = Node(' ')
            if not node.rightChild: node.rightChild = Node(' ')
            self._fillTree(node.leftChild, height - 1)
            self._fillTree(node.rightChild, height - 1)

    def prettyPrint(self):
        """
        """
        # get height of tree
        total_layers = self.getHeight()

        tree = deepcopy(self)

        tree.fillTree(total_layers)
        # start a queue for BFS
        queue = Queue()
        # add root to queue
        queue.enqueue(tree.root)  # self = root
        # index for 'generation' or 'layer' of tree
        gen = 1
        # BFS main
        while not queue.isEmpty():
            # copy queue
            #
            copy = Queue()
            while not queue.isEmpty():
                copy.enqueue(queue.dequeue())
            #
            # end copy queue

            first_item_in_layer = True
            edges_string = ""
            extra_spaces_next_node = False

            # modified BFS, layer by layer (gen by gen)
            while not copy.isEmpty():

                node = copy.dequeue()

                # -----------------------------
                # init spacing
                spaces_front = pow(2, total_layers - gen + 1) - 2
                spaces_mid = pow(2, total_layers - gen + 2) - 2
                dash_count = pow(2, total_layers - gen) - 2
                if dash_count < 0:
                    dash_count = 0
                spaces_mid = spaces_mid - (dash_count * 2)
                spaces_front = spaces_front - dash_count
                init_padding = 2
                spaces_front += init_padding
                if first_item_in_layer:
                    edges_string += " " * init_padding
                # ----------------------------->

                # -----------------------------
                # construct edges layer
                edge_sym = "/" if node.leftChild and node.leftChild.dataValue is not " " else " "
                if first_item_in_layer:
                    edges_string += " " * (pow(2, total_layers - gen) - 1) + edge_sym
                else:
                    edges_string += " " * (pow(2, total_layers - gen + 1) + 1) + edge_sym
                edge_sym = "\\" if node.rightChild and node.rightChild.dataValue is not " " else " "
                edges_string += " " * (pow(2, total_layers - gen + 1) - 3) + edge_sym
                # ----------------------------->

                # -----------------------------
                # conditions for dashes
                if node.leftChild and node.leftChild.dataValue == " ":
                    dash_left = " "
                else:
                    dash_left = "_"

                if node.rightChild and node.rightChild.dataValue == " ":
                    dash_right = " "
                else:
                    dash_right = "_"
                # ----------------------------->

                # -----------------------------
                # handle condition for extra spaces when node lengths don't match or are even:
                if extra_spaces_next_node:
                    extra_spaces = 1
                    extra_spaces_next_node = False
                else:
                    extra_spaces = 0
                # ----------------------------->

                # -----------------------------
                # account for longer data
                data_length = len(str(node.dataValue))
                if data_length > 1:
                    if data_length % 2 == 1:  # odd
                        if dash_count > 0:
                            dash_count -= ((data_length - 1) / 2)
                        else:
                            spaces_mid -= (data_length - 1) / 2
                            spaces_front -= (data_length - 1) / 2
                            if data_length is not 1:
                                extra_spaces_next_node = True
                    else:  # even
                        if dash_count > 0:
                            dash_count -= ((data_length) / 2) - 1
                            extra_spaces_next_node = True
                            # dash_count += 1
                        else:
                            spaces_mid -= (data_length - 1)
                            spaces_front -= (data_length - 1)
                # ----------------------------->

                # -----------------------------
                # print node with/without dashes
                if first_item_in_layer:
                    print((" " * spaces_front) + (dash_left * int(dash_count)) + str(node.dataValue) + (dash_right * int(dash_count)),end="")
                    first_item_in_layer = False
                else:
                    print((" " * (int(spaces_mid)+1 - int(extra_spaces))) + (dash_left * int(dash_count)) + str(node.dataValue) + (dash_right * int(dash_count)), end="")
                # ----------------------------->

                if node.leftChild: queue.enqueue(node.leftChild)
                if node.rightChild: queue.enqueue(node.rightChild)

            # print the fun squiggly lines
            if not queue.isEmpty():
                print("\n" + edges_string)

            # increase layer index
            gen += 1

    def remove(self, value):
        """
        Removes a Node which contains the value `value`.
        To remove a Node, three cases must be handled.
        Case 1: leaf node
                    -> delete it
        Case 2: node has one child
                    -> delete node and put its child in its place
        Case 3: node has two children
                    -> delete node and put its smallest child from its right branch in its place
        """
        if self.root:
            self.root = self.__remove(self.root, value)

    def __remove(self, node, value):
        if node.dataValue == value:

            # Case 1
            if node.leftChild is None and node.rightChild is None:
                return None

            # Case 2
            elif node.leftChild and node.rightChild is None:
                return node.leftChild

            # Case 2
            elif node.leftChild is None and node.rightChild:
                return node.rightChild

            # Case 3
            else:
                parent_node = node
                smallest_node = node.rightChild
                while smallest_node.leftChild:
                    parent_node = smallest_node
                    smallest_node = smallest_node.leftChild

                # The right Node is the smallest one
                if parent_node == node:
                    smallest_node.leftChild = node.leftChild

                # The smallest Node was found to the left of its right branch
                else:
                    parent_node.leftChild = smallest_node.rightChild
                    smallest_node.leftChild = node.leftChild
                    smallest_node.rightChild = node.rightChild
                return smallest_node

        elif node.dataValue > value and node.leftChild:
            node.leftChild = self.__remove(node.leftChild, value)

        elif node.dataValue < value and node.rightChild:
            node.rightChild = self.__remove(node.rightChild, value)

        node.compute_size()
        return node

nodes = "11 200 173 196 52 143 165 37 7 36"
nodes = nodes.split(" ")
nodes = [int(x) for x in nodes]
bst = binary_search_tree()
for i in nodes:
    bst.insert(i)
bst.prettyPrint()
bst.printLevelOrder()