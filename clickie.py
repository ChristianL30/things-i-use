from pynput.mouse import Button, Controller
import os
os.system('mode con: cols=65 lines=10')
os.system("cls")
mouse = Controller()
print("enter 'n' to close the program")
def position():
    mouse.position
    var = input("Type 'y' and press *Enter* to get the mouse position: ")
    if var == "y":
        print(".................................................")
        print("mouse position:", (mouse.position))
        position()
    else:
        exit()
position()