from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *
import datetime

formatter = MenuFormatBuilder().set_title_align('center').set_subtitle_align('center').set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_BORDER).show_prologue_top_border(True)

#open vim
def getOptionOne(dir, name):
    command = f'vim ./problems/{dir}/{name}/solution.py'
    return CommandItem("Create/Edit Solution",command)

#test solution
def getOptionTwo(dir, name):
    directory = f'./problems/{dir}/{name}'
    command = f'rm -rf {directory}/__pycache__ && python {directory}/{name}_tests.py && sleep 5'
    return CommandItem("Test Solution",command)

#rename file and move it to archive
def getOptionThree(dir, name):
    currentDate = datetime.datetime.now()
    dateString = currentDate.strftime("%Y-%m-%d_%H%M")
    newFileName = f'{name}_{dateString}'
    newPath = f'./archive/{newFileName}.py'
    command = f'mv ./problems/{dir}/{name}/solution.py {newPath} && echo "Moved file to {newPath}" && sleep 3'
    return CommandItem("Archive Solution", command)