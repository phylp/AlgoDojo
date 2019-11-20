from consolemenu import *
from utils import *

graphMenu = ConsoleMenu("Graph Menu")

#BST Search
bstSearchProblem = ConsoleMenu("Problem: BST Search", prologue_text="Find closest node within a binary search tree (test text...)", formatter=formatter)
bstSearchProblem.append_item(getOptionOne("graphs", "bst_search"))
bstSearchProblem.append_item(getOptionTwo("graphs", "bst_search"))
bstSearchProblem.append_item(getOptionThree("graphs", "bst_search"))
bstOptionsMenu = SubmenuItem("BST Search", bstSearchProblem, graphMenu)
graphMenu.append_item(bstOptionsMenu)


