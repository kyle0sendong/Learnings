import pandas as pd

df = pd.read_csv('data.csv')

# Bingo Card Test
bingo_card = [

    # [[9, 10, 5, 3, 12],
    #  [18, 23, 19, 16, 30],
    #  [34, 44, 0, 32, 41],
    #  [60, 53, 58, 56, 50],
    #  [72, 68, 69, 62, 65]],
    #
    [[5, 3, 14, 11, 12],
     [25, 16, 20, 23, 26],
     [44, 34, 0, 43, 32],
     [50, 56, 59, 53, 58],
     [72, 65, 71, 67, 68]],

    # [[12, 11, 14, 3, 5],
    #  [26, 23, 20, 16, 25],
    #  [32, 43, 0, 34, 44],
    #  [58, 53, 69, 49, 50],
    #  [72, 67, 71, 65, 68]],
    #
    # [[4, 19, 33, 58, 75],
    #  [2, 22, 41, 47, 68],
    #  [10, 26, 0, 54, 61],
    #  [12, 29, 35, 55, 73],
    #  [8, 24, 44, 60, 70]],
    #
    # [[5, 17, 38, 54, 68],
    #  [3, 29, 31, 47, 62],
    #  [14, 28, 0, 52, 70],
    #  [6, 24, 40, 55, 72],
    #  [2, 27, 36, 59, 74]],
    #
    # [[7, 24, 30, 53, 65],
    #  [5, 28, 41, 60, 72],
    #  [14, 20, 0, 56, 68],
    #  [12, 22, 34, 58, 71],
    #  [4, 29, 35, 48, 75]],
    #
    # [[6, 23, 39, 58, 67],
    #  [3, 27, 32, 46, 64],
    #  [13, 26, 0, 53, 63],
    #  [11, 24, 37, 54, 73],
    #  [9, 19, 40, 57, 75]],
    #
    # [[10, 22, 36, 55, 71],
    #  [5, 28, 42, 49, 61],
    #  [15, 20, 0, 52, 64],
    #  [8, 23, 31, 53, 69],
    #  [7, 18, 33, 56, 73]],
    #
    #
    # [[9, 17, 30, 52, 65],
    #  [1, 20, 44, 49, 62],
    #  [11, 26, 0, 50, 66],
    #  [14, 28, 38, 55, 72],
    #  [8, 19, 36, 59, 73]],
    #
    # [[6, 23, 30, 58, 74],
    #  [3, 29, 37, 50, 65],
    #  [12, 25, 0, 56, 61],
    #  [11, 27, 42, 51, 69],
    #  [5, 18, 34, 59, 72]],
    #
    # [[5, 21, 31, 50, 61],
    #  [1, 27, 32, 58, 67],
    #  [12, 29, 0, 53, 72],
    #  [9, 18, 34, 56, 71],
    #  [3, 25, 37, 49, 73]],
    #
    # [[7, 23, 39, 55, 67],
    #  [5, 28, 31, 49, 61],
    #  [14, 22, 0, 54, 75],
    #  [11, 26, 40, 53, 69],
    #  [3, 17, 36, 58, 73]],
]


# Gathering all bingo card's numbers for patterns
def get_card_number_patterns():
    # Stores all the numbers that are relevant for extra pattern
    all_card_number_patterns = []

    for i in range(len(bingo_card)):
        left_diagonal_pattern = [bingo_card[i][0][0], bingo_card[i][1][1], bingo_card[i][3][3], bingo_card[i][4][4]]
        right_diagonal_pattern = [bingo_card[i][0][4], bingo_card[i][1][3], bingo_card[i][3][1], bingo_card[i][4][0]]
        corner_pattern = [bingo_card[i][0][0], bingo_card[i][0][4], bingo_card[i][4][0], bingo_card[i][4][4]]
        t_pattern = [bingo_card[i][0][0], bingo_card[i][0][1], bingo_card[i][0][2], bingo_card[i][0][3],
                     bingo_card[i][0][4], bingo_card[i][1][2], bingo_card[i][3][2], bingo_card[i][4][2]]

        x_pattern = [bingo_card[i][0][0], bingo_card[i][1][1], bingo_card[i][3][3], bingo_card[i][4][4],
                     bingo_card[i][0][4], bingo_card[i][1][3], bingo_card[i][3][1], bingo_card[i][4][0]]

        all_corner_pattern = [bingo_card[i][0][0], bingo_card[i][0][1], bingo_card[i][0][2], bingo_card[i][0][3],
                              bingo_card[i][0][4], bingo_card[i][4][0], bingo_card[i][4][1], bingo_card[i][4][2],
                              bingo_card[i][4][3], bingo_card[i][4][4], bingo_card[i][1][0], bingo_card[i][2][0],
                              bingo_card[i][3][0], bingo_card[i][1][4], bingo_card[i][2][4], bingo_card[i][3][4]]

        # Horizontal Pattern, 2, 3, & 4
        h0 = [bingo_card[i][0][0], bingo_card[i][0][1], bingo_card[i][0][2], bingo_card[i][0][3], bingo_card[i][0][4]]
        h1 = [bingo_card[i][1][0], bingo_card[i][1][1], bingo_card[i][1][2], bingo_card[i][1][3], bingo_card[i][1][4]]
        h2 = [bingo_card[i][2][0], bingo_card[i][2][1], bingo_card[i][2][3], bingo_card[i][2][4]]
        h3 = [bingo_card[i][3][0], bingo_card[i][3][1], bingo_card[i][3][2], bingo_card[i][3][3], bingo_card[i][3][4]]
        h4 = [bingo_card[i][4][0], bingo_card[i][4][1], bingo_card[i][4][2], bingo_card[i][4][3], bingo_card[i][4][4]]

        # Put all of these patterns into one array then append to card number patterns
        all_patterns = [left_diagonal_pattern, right_diagonal_pattern, corner_pattern, t_pattern, x_pattern,
                        all_corner_pattern, h0, h1, h2, h3, h4]

        all_card_number_patterns.append(all_patterns)

    return all_card_number_patterns


# Check numbers for patterns in each game for my bingo card
card_number_patterns = get_card_number_patterns()

# Collect all numbers that appeared per game
num_columns = len(df)
num_rows = 75
game_numbers = []
for i in range(num_columns):
    num_appeared = []
    for j in range(num_rows):
        is_true = df.iloc[i][j]

        if is_true:
            num_appeared.append(j + 1)

    game_numbers.append(num_appeared)

games = 0
wins = 0
losses = 0
account_size = 100
risk = 5
total_risk = len(card_number_patterns) * risk
game_counter = 1
# Start back testing for cards
for current_game in game_numbers:

    if len(current_game) > 10:
        games += 1
        print(f'\nCurrent Game Numbers: {current_game}')
        account_size -= total_risk
        print(f'Game {game_counter}: {account_size}')
        game_counter += 1
        total_profit = 0

        for i in range(len(card_number_patterns)):
            horizontal_counter = 0
            x_counter = 0
            print(f'Card {i + 1}: ', end='')

            # Left diagonal
            if all(number in current_game for number in card_number_patterns[i][0]):
                profit = risk * 1.1
                total_profit += profit
                account_size += profit
                x_counter += 1
                print(f'Left Diagonal + {profit} | ', end='')

            # Right Diagonal
            if all(number in current_game for number in card_number_patterns[i][1]):
                profit = risk * 1.1
                total_profit += profit
                account_size += profit
                x_counter += 1
                print(f'Right Diagonal + {profit} | ', end='')

            # Corner Pattern
            if all(number in current_game for number in card_number_patterns[i][2]):
                profit = risk * 2
                total_profit += profit
                account_size += profit
                print(f'Corner + {profit} | ', end='')

            # T Pattern
            if all(number in current_game for number in card_number_patterns[i][3]):
                profit = risk * 11.5
                total_profit += profit
                account_size += profit
                print(f'T Pattern + {profit} | ', end='')

            # X Pattern
            if x_counter == 2:
                profit = risk * 11.5
                total_profit += profit
                account_size += profit
                print(f'X Pattern + {profit} | ', end='')

            # All Corner Pattern
            if all(number in current_game for number in card_number_patterns[i][5]):
                profit = risk * 200
                total_profit += profit
                account_size += profit
                print(f'All Corner + {profit} | ', end='')

            # H0
            if all(number in current_game for number in card_number_patterns[i][6]):
                horizontal_counter += 1

            # H1
            if all(number in current_game for number in card_number_patterns[i][7]):
                horizontal_counter += 1

            # H2
            if all(number in current_game for number in card_number_patterns[i][8]):
                horizontal_counter += 1

            # H3
            if all(number in current_game for number in card_number_patterns[i][9]):
                horizontal_counter += 1

            # H4
            if all(number in current_game for number in card_number_patterns[i][10]):
                horizontal_counter += 1

            if horizontal_counter == 2:
                profit = risk * 5.5
                total_profit += profit
                account_size += profit
                print(f'2L + {profit} | ', end='')

            if horizontal_counter == 3:
                profit = risk * 30
                total_profit += profit
                account_size += profit
                print(f'3L + {profit} | ', end='')

            if horizontal_counter == 4:
                profit = risk * 360
                total_profit += profit
                account_size += profit
                print(f'4L + {profit} | ', end='')
            print()

        if total_profit - total_risk > 0:
            wins += 1
        else:
            losses += 1

        print(f'Profit: {total_profit} Risk: {total_risk} Net: {total_profit - total_risk}')

print(f'\nTotal Win = {wins}')
print(f'Total Loss = {losses}')
print(f'Winrate = {wins/games * 100}%')
# test1 = [1,2,3,4,5]
# test2 = [1,2,3,4,5,6]
#
# if all(element in test2 for element in test1):
#     print('asd')
