import pygetwindow as gw
import win32gui


def get_all_opened_window():
    def enum_windows_callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            if window_title:
                windows.append(window_title)

    windows = []

    # Enumerate through all top-level windows and collect their titles
    win32gui.EnumWindows(enum_windows_callback, windows)

    for window_title in windows:
        print(window_title)


def get_window_position(window_name):
    window = gw.getWindowsWithTitle(window_name)[0]
    print(f'Top Left: {window.topleft}, Bottom Right: {window.bottomright}')


def get_window_size(window_name):
    window_handle = win32gui.FindWindow(None, window_name)

    # Get the window's position and size
    window_rect = win32gui.GetWindowRect(window_handle)

    # Calculate the width and height of the window
    window_width = window_rect[2] - window_rect[0]
    window_height = window_rect[3] - window_rect[1]

    print(f"Window size: {window_width} x {window_height}")
