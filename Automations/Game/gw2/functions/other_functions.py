import random
import keyboard
import pyautogui
import cv2
import time
import numpy as np
import pyperclip


def write_text(text):
    pyperclip.copy(text)
    keypress('ctrl', 'v')
    time.sleep(0.5)


def keypress(key1, key2=None):
    delay = random.randint(100, 300)
    if key2 is None:
        keyboard.press(key1)
        time.sleep(delay/1000)  # Milliseconds
        keyboard.release(key1)
    else:
        keyboard.press(key1)
        keyboard.press(key2)
        time.sleep(delay/1000)  # Milliseconds
        keyboard.release(key1)
        keyboard.release(key2)


def is_image_found(pos, path, delay, move_mouse):
    template_image = cv2.imread(path)
    max_timeout = int((delay/1000) / (delay/10000))

    if max_timeout < 1:
        max_timeout = 1

    for i in range(max_timeout):

        x1 = pos[0]
        y1 = pos[1]
        x2 = pos[2]
        y2 = pos[3]

        target_image = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))

        template_gray = cv2.cvtColor(np.array(template_image), cv2.COLOR_BGR2GRAY)
        target_gray = cv2.cvtColor(np.array(target_image), cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(template_gray, target_gray, cv2.TM_CCOEFF_NORMED)

        threshold = 0.7

        # Alternate method instead of using findNonZero to bypass
        _, result_binary = cv2.threshold(result, threshold, 1, cv2.THRESH_BINARY)
        locations = np.argwhere(result_binary == 1)

        # Search NonZeroes
        if len(locations) > 0:
            print('Image found')

            if move_mouse:
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                x, y = max_loc

                time.sleep(0.2)
                pyautogui.moveTo(x, y)

            return True

        time.sleep(delay / 10000)

    print('Image not found')
    return False


def save_image(x1, y1, x2, y2, path):
    target_image = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    target_image.save(path)
