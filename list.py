from random import randint
from bintree.bin_trees import binary_search_tree
from tkinter import *
import math

class Main:
    def __init__(self):

        window = Tk() # Create a window
        window.title("Recursive Tree") # Set a title

        self.width = 800
        self.height = 600
        # self.canvas = Canvas(window,
        # width = self.width, height = self.height,bg="white")
        # self.canvas.pack()

        # Add a label, an entry, and a button to frame1
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()

        self.maintext = Text(window, width = 600, height = 400)
        self.maintext.pack()

        Label(frame1,
            text = "Nodes: ").pack(side = LEFT)
        self.depth = StringVar()
        self.bst = binary_search_tree()

        Entry(frame1, textvariable = self.depth,
            justify = RIGHT).pack(side = LEFT)
        Button(frame1, text = "Insert Node",
            command = self.insertNodes).pack(side = LEFT)
        Button(frame1, text="Preorder",
               command=self.printPreorder).pack(side=LEFT)
        Button(frame1, text="Inorder",
               command=self.printInorder).pack(side=LEFT)
        Button(frame1, text="Postorder",
               command=self.printPostorder).pack(side=LEFT)
        Button(frame1, text="Search Node",
               command=self.isNode).pack(side=LEFT)
        Button(frame1, text="Delete Node",
               command=self.deleteNode).pack(side=LEFT)
        Button(frame1, text="Print Tree",
               command=self.printBST).pack(side=LEFT)
        Button(frame1, text="Level Traversal",
               command=self.printByLevel).pack(side=LEFT)
        Button(frame1, text="Reset Tree",
               command=self.resetBST).pack(side=LEFT)
        sys.stdout = TextRedirector(self.maintext, "stdout")

        window.mainloop() # Create an event loop

    def insertNodes(self):
        nodes = self.depth.get()
        nodes = nodes.split(" ")
        nodes = [int(x) for x in nodes]
        for i in nodes:
            self.bst.insert(i)

    def deleteNode(self):
        self.bst.remove(int(self.depth.get()))

    def printBST(self):
        print(self.bst.prettyPrint())
        print("\n" * 3)


    def printInorder(self):
        print(self.bst.print_tree("inorder"))
        print("\n" * 3)
        self.maintext.delete("1.0", END)

    def printPostorder(self):
        print(self.bst.print_tree("postorder"))
        print("\n" * 3)
        self.maintext.delete("1.0", END)


    def printPreorder(self):
        print(self.bst.print_tree("preorder"))
        print("\n" * 3)
        self.maintext.delete("1.0", END)

    def printByLevel(self):
        print(self.bst.printLevelOrder())
        print("\n" * 3)
        self.maintext.delete("1.0", END)

    def resetBST(self):
        self.maintext.delete("1.0", END)
        self.bst = binary_search_tree()

    def isNode(self):
        node = self.depth.get()
        node = int(node)
        print(self.bst.search(node))

class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")


Main()