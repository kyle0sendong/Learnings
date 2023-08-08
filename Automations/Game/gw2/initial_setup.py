import win32gui
import win32con


def change_window_size(window_name):
    window_handle = win32gui.FindWindow(None, window_name)
    new_width = 697
    new_height = 727
    win32gui.SetWindowPos(window_handle, win32con.HWND_TOP, 0, 0, new_width, new_height, win32con.SWP_SHOWWINDOW)

