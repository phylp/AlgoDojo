import sys
import os
import datetime
from consolemenu import *
from utils import *

def main():
    mainMenu = ConsoleMenu("Algo Dojo", "Train like a motha fuckin' ninja")

    #Problem Set Menus
    graphMenu = ConsoleMenu("Graph Menu")
    treeMenu = ConsoleMenu("Tree Menu")
    arrayMenu = ConsoleMenu("Array Menu")
    stringMenu = ConsoleMenu("String Menu")

    #Main Menu Items
    graphs = SubmenuItem("Graphs", graphMenu, mainMenu)
    trees = SubmenuItem("Trees", treeMenu, mainMenu)
    arrays = SubmenuItem("Arrays", arrayMenu, mainMenu)
    strings = SubmenuItem("Strings", stringMenu, mainMenu)

    #Graph Problems
    bstSearchProblem = ConsoleMenu("BST search", prologue_text="Find closest node within a binary search tree (test text...)", formatter=formatter)
    bstSearchProblem.append_item(getOptionOne("graphs", "bst_search"))
    bstSearchProblem.append_item(getOptionTwo("graphs", "bst_search"))
    bstSearchProblem.append_item(getOptionThree("graphs", "bst_search"))

    bfsOptionsMenu = SubmenuItem("BST Search", bstSearchProblem, graphMenu)
    graphMenu.append_item(bfsOptionsMenu)

    mainMenu.append_item(graphs)
    mainMenu.append_item(trees)
    mainMenu.append_item(arrays)
    mainMenu.append_item(strings)

    mainMenu.show()

if __name__ == "__main__":
    main()
