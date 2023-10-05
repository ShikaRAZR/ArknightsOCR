"""
Script to run through arknights daily using ocr
https://pypi.org/project/PyAutoGUI/
https://github.com/drov0/python-imagesearch 
"""
from os.path import exists
from screeninfo import get_monitors
from python_imagesearch.imagesearch import *
import time
import pyautogui
import pydirectinput
import operator_card

pyautogui.PAUSE = 0
pydirectinput.PAUSE = 0
pyautogui.FAILSAFE = False


def pyautogui_test():
    pyautogui.moveTo(1200, 400)
    pyautogui.mouseDown(button="left")
    pyautogui.dragTo(1200, 600, 0.2)
    pyautogui.dragTo(1400, 600, 0.2)
    pyautogui.dragTo(1400, 400, 0.2)
    pyautogui.dragTo(1200, 400, 0.2)


def pydirectinput_test():
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


def pyautogui_ocr_test():
    # x, y = pyautogui.locateCenterOnScreen("newtab.jpg")
    filepath = r"E:\0Other\Coding\1_Projects\Python\Projects\ArknightsMacro\refresh.jpg"
    file_exists = exists(filepath)
    print(file_exists)
    location = pyautogui.locateOnScreen("refresh.jpg")
    coord = pyautogui.center(location)
    # pyautogui.moveTo(coord.x, coord.y, duration=0.1)
    # pyautogui.leftClick()


def python_imagesearch(filepath, precision):
    pos = imagesearch(filepath, precision)
    if pos[0] != -1:
        x_pos = pos[0]
        y_pos = pos[1]
        if len(get_monitors()) > 1:
            x_pos = pos[0] - 1920
        print("Position : ", x_pos, y_pos)
        return (x_pos, y_pos)
    else:
        print("image not found")
    # click_image("./newtab.jpg", pos, "right", 0.1, offset=5)
    return None


def screenshot_imagesearch():
    img1 = pyautogui.screenshot(region=(-1893, 109, 500, 400))
    # img1.save("../testimages/screenshot.png")
    # print(pyautogui.position())


def chikamaintest():
    img_paths = [
        "../resources/e2.png",
        "../testimages/yt.jpg",
        "../testimages/SariaOp.jpg",
    ]
    pos = python_imagesearch(img_paths[2], 0.8)
    if pos != None:
        pyautogui.moveTo(pos[0], pos[1], duration=0.1)
        print("Mouse Moved")
    screenshot_imagesearch()


def meltymaintest():
    print(operator_card.detect_elite())


if __name__ == "__main__":
    print("Hello World")
    # meltymaintest()
    # chikamaintest()
