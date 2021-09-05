import pyautogui as pt
from time import sleep
import random
l = ["|", "/", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "[", "]", "{", "}", ":", ";", '"', "<", ">", ",", ".", "?", "`", "~", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "😉", "😑", "😎", "😊", "😅"]
def spam():
    for i in range(200):
        pt.typewrite(random.choice(l))
        pt.typewrite(random.choice(l))
        pt.typewrite(random.choice(l))
        pt.typewrite(random.choice(l))
        pt.typewrite(random.choice(l))
        pt.typewrite(random.choice(l))
        pt.typewrite(random.choice(l))
        pt.typewrite(random.choice(l))
        pt.typewrite(random.choice(l))
        pt.typewrite(random.choice(l))
        pt.typewrite(random.choice(l))
        pt.typewrite(random.choice(l))
        pt.typewrite(random.choice(l))
        pt.press("enter")

def hacking():
    for i in range(1):
        pt.typewrite("Hacking...")
        pt.press("enter")
        pt.typewrite("Penetration completed system shutingdown....")
        pt.press("enter")

sleep(5)
hacking()
spam()
"""

"""

    
