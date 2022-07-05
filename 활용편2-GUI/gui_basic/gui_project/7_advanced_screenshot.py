import keyboard
from PIL import ImageGrab
import time

def screenshot():
    # 2020년 2월 1일 10시 20분 30초 -> _20200201_102030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))
        
keyboard.add_hotkey("F9", screenshot) # 사용자가 F9 누르면 스크린샷 찍음        

keyboard.wait("esc") #사용자가 esc를 누를 때 까지 프로그램 수행