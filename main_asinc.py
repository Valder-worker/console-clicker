import asyncio
import keyboard
import mouse

async def check():
    global ch
    if ch:
        ch = False
        print('Отключен')
    else:
        ch = True
        print('Включен')

async def main():
    keyboard.add_hotkey('ALT + Z', check)
    while True:
        await asyncio.sleep(0.005)
        if ch:
            mouse.double_click(button='left')

asyncio.run(main())