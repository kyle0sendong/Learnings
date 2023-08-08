from Game.gw2.functions.other_functions import *
import win32gui


def reset_cursor():
    time.sleep(0.2)
    pyautogui.click(25, 192)
    time.sleep(0.2)
    pyautogui.click(25, 162)


def open_tp():

    for i in range(5):

        window_pos = [0, 0, 697, 727]
        window_name = 'Guild Wars 2'
        window_handle = win32gui.FindWindow(None, window_name)
        win32gui.SetForegroundWindow(window_handle)

        reset_cursor()
        pyautogui.moveTo(50, 50)
        keypress('f2')
        time.sleep(2)
        image_found = is_image_found(window_pos, './screenshots/tp_lion.png', 3000, True)

        if image_found:
            time.sleep(0.5)
            # Move tp to the top
            pyautogui.dragTo(200, 20, duration=1)
            break
