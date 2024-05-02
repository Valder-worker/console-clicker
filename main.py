#pip install keyboard
#pip install mouse

import time
import keyboard
import mouse
print('Запуск и остановка клавишами ALT + Z')
ch = False
def check():
    global ch
    if ch:
        ch = False
        print('Отключен')
    else:
        ch = True
        print('Включен')

keyboard.add_hotkey('ALT + Z', check)

while True:
    time.sleep(0.005)
    if ch:
        mouse.double_click(button='left')