from consolemenu import *
from utils import *

arrayMenu = ConsoleMenu("Array Menu")


#Three Number Sum
threeNumberSum = ConsoleMenu("Problem: Three Number Sum", prologue_text="Given an array of integers and a target sum, find all combinations of three number combinations which add up to the target value.", formatter=formatter)
threeNumberSum.append_item(getOptionOne("arrays", "three_number_sum"))
threeNumberSum.append_item(getOptionTwo("arrays", "three_number_sum"))
threeNumberSum.append_item(getOptionThree("arrays", "three_number_sum"))
threeNumberSumOptionsMenu = SubmenuItem("Three Number Sum", threeNumberSum, arrayMenu)
arrayMenu.append_item(threeNumberSumOptionsMenu)
