from other_functions import *
import pandas as pd
import datetime
current_date = datetime.date.today()

start_record_pos = [114, 254, 177, 288]

counter = 0

while(True):
    _45_found = is_image_found(start_record_pos, './webscrape/screenshots/45.png', 1500, False)

    if (_45_found):

        print('found 45/48')
        display_balls_pos = [745, 270]
        pyautogui.leftClick(display_balls_pos[0], display_balls_pos[1])
        time.sleep(0.5)
        # Time to record bingo balls
        pos = [887, 180]
        rgb = [255, 101, 51]

        numbers = range(1, 76)
        df = pd.DataFrame(columns=numbers)

        bingo = [False]

        for i in range(0, 5):
            x = [222, 254, 287, 321, 354, 386, 418, 452, 485, 519, 553, 586, 617, 651, 684]
            y = [320, 347, 377, 407, 434]

            for j in range(0, 15):
                ball = pyautogui.pixelMatchesColor(x[j], y[i], rgb)
                bingo.append(ball)

        df = df._append(pd.Series(bingo), ignore_index=True)
        df.to_csv('./webscrape/data/' + str(current_date) + '.csv', mode='a', header=False, index=False)
        print('done recording')

        time.sleep(180)
        # Refresh page
        refresh_pos = [277, 46]
        pyautogui.leftClick(refresh_pos[0], refresh_pos[1])
        time.sleep(5)
        print('Refreshed page. 5 seconds')
        print('Waiting for next record of data.\n')
        counter = 0

    else:
        counter += 1

    if counter > 800:
        counter = 0
        print('Reached counter. Refreshing the page')
        # Refresh page
        refresh_pos = [277, 46]
        pyautogui.leftClick(refresh_pos[0], refresh_pos[1])
        time.sleep(1)

