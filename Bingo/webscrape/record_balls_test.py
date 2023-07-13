import pyautogui
import pandas as pd

def display_balls(list):
    for i in range(1, (len(list)+1)):
        print(list[i-1], end=' ')
        if i % 15 == 0:
            print('\n')

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
df.to_csv('june14.csv', mode='a', header=True, index=False)
print('done')
