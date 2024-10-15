import pyautogui as ai
import random as r
import time
ai.FAILSAFE = True #make it to False to make others life hell
try :
    for i in range(11002340):
        ai.click()
        time.sleep(3)
        x,y =r.randint(0,2300), r.randint(0,2300)
        ai.click(x, y)
        xCord, yCord = ai.position()
        screenshot = ai.screenshot()  # Takes a screenshot
        screenshot.save(f"screenshot{i}.jpg")

        print("Coordinate x {}, Coordinate y {}".format(xCord, yCord))
except Exception as ex:
    print(f"{ex} reached maixmum out of the loop")
