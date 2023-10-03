import pyautogui
from python_imagesearch.imagesearch import *


def detect_elite():
    elite = None
    for i in range(3):
        # how do we get it to recognize image that's not identical?
        # lowering precision will also give the wrong result
        pos = imagesearch(f"../resources/e{i}.png", 0.1)
        if pos[0] != -1:
            # pyautogui.moveTo(pos[0], pos[1], duration=0.1)
            elite = i
    return elite


print(detect_elite())
