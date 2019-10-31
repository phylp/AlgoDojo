import sys
import os
import datetime
from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *

def main():
    #create file with vim
    def getOptionOne(dir, name):
        command = f'vim ./solutions/{dir}/{name}.py'
        return CommandItem("Create/Edit Solution",command)

    #test solution
    def getOptionTwo(dir, name):
        command = f'python ./tests/{dir}/{name}_tests.py'
        return CommandItem("Test Solution",command)
    
    #rename file and move it to archive
    def getOptionThree(dir, name):
        currentDate = datetime.datetime.now()
        dateString = currentDate.strftime("%Y-%m-%d_%H-%M-%S")
        newFileName = f'{name}_{dateString}'
        newPath = f'./archive/{newFileName}.py'
        command = f'mv ./solutions/{dir}/{name}.py {newPath}'
        return CommandItem("Archive Solution", command)

    formatter = MenuFormatBuilder().set_title_align('center').set_subtitle_align('center').set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_BORDER).show_prologue_top_border(True)

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
    bstSearchProblem = ConsoleMenu("BST search", prologue_text="Find closest node within a binary search tree (test text)", formatter=formatter)
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
