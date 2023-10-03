"""
Script to run through arknights daily using ocr
https://pypi.org/project/PyAutoGUI/
https://github.com/drov0/python-imagesearch 
"""

import tkinter as tk
import pyautogui
import pydirectinput
import time
from os.path import exists
from python_imagesearch.imagesearch import *

pyautogui.PAUSE = 0
pydirectinput.PAUSE = 0
pyautogui.FAILSAFE = False


def pyautoguitest():
    pyautogui.moveTo(1200, 400)
    pyautogui.mouseDown(button="left")
    pyautogui.dragTo(1200, 600, 0.2)
    pyautogui.dragTo(1400, 600, 0.2)
    pyautogui.dragTo(1400, 400, 0.2)
    pyautogui.dragTo(1200, 400, 0.2)


def pydirectinputtest():
    pydirectinput.moveTo(1200, 400)
    pydirectinput.mouseDown()
    pydirectinput.move(0, 200)
    time.sleep(0.3)
    pydirectinput.move(200, 0)
    time.sleep(0.3)
    pydirectinput.move(0, -200)
    time.sleep(0.3)
    pydirectinput.move(-200, 0)
    pydirectinput.mouseUp()


def pyautoguiocrtest():
    # x, y = pyautogui.locateCenterOnScreen("newtab.jpg")
    filepath = r"E:\0Other\Coding\1_Projects\Python\Projects\ArknightsMacro\refresh.jpg"
    file_exists = exists(filepath)
    print(file_exists)
    location = pyautogui.locateOnScreen("refresh.jpg")
    coord = pyautogui.center(location)
    # pyautogui.moveTo(coord.x, coord.y, duration=0.1)
    # pyautogui.leftClick()


def pythonimagesearch():
    pos = imagesearch("./github.jpg")
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
    else:
        print("image not found")
    pyautogui.moveTo(pos[0] - 1920, pos[1], duration=0.1)
    # click_image("./newtab.jpg", pos, "right", 0.1, offset=5)


if __name__ == "__main__":
    print("Hello World")
    pythonimagesearch()
