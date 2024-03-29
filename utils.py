from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *
import datetime
import os.path

formatter = MenuFormatBuilder().set_title_align('center').set_subtitle_align('center').set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_BORDER).show_prologue_top_border(True)

#copy template to solution file if template available, open vim
def getOptionOne(dir, name):
    command  = None
    basePath = f'./problems/{dir}/{name}'
    templatePath = f'{basePath}/template.py'
    solutionPath = f'{basePath}/solution.py'
    if os.path.exists(templatePath):
        command = f'cp {templatePath} {solutionPath} && vim {solutionPath}'
    else:
        command = f'vim {solutionPath}'
    return CommandItem("Create/Edit Solution",command)

#test solution
def getOptionTwo(dir, name):
    directory = f'./problems/{dir}/{name}'
    command = f'rm -rf {directory}/__pycache__ && python {directory}/{name}_tests.py 2> test.txt && cat test.txt && sleep 3'
    return CommandItem("Test Solution",command)

#rename file and move it to archive
def getOptionThree(dir, name):
    currentDate = datetime.datetime.now()
    dateString = currentDate.strftime("%Y-%m-%d_%H%M")
    newFileName = f'{name}_{dateString}'
    newPath = f'./archive/{newFileName}.py'
    command = f'mv ./problems/{dir}/{name}/solution.py {newPath} && echo "Moved file to {newPath}" && sleep 3'
    return CommandItem("Archive Solution", command)

