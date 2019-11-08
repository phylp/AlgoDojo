import sys
from consolemenu import *
from utils import *
from graphs import *
from arrays import *
from strings import * 

def main():
    mainMenu = ConsoleMenu("Algo Dojo", "Train like a motha fuckin' ninja")

    #Main Menu Items
    graphs = SubmenuItem("Graphs", graphMenu, mainMenu)
    arrays = SubmenuItem("Arrays", arrayMenu, mainMenu)
    strings = SubmenuItem("Strings", stringMenu, mainMenu)

    mainMenu.append_item(graphs)
    mainMenu.append_item(arrays)
    mainMenu.append_item(strings)

    mainMenu.show()

if __name__ == "__main__":
    main()
