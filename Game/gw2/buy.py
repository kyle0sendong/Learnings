from Game.gw2.functions.tp_functions import *

tp_icon_pos = [21, 161]
tp_home_icon_pos = [248, 70, 306, 111]
favorites_pos = [80, 359]
search_pos = [78, 144]
first_item_pos = [300, 198]
item_trade_pos = [366, 333, 458, 347]
quantity_pos = [287, 192]
price_pos = [404, 223]
place_order_pos = [306, 287]
success_pos = [445, 192, 471, 211]
ok_pos = [318, 291]
close_pos = [672, 45]


def buy(item_name, quantity, price):

    open_tp()

    time.sleep(2)
    pyautogui.click(tp_icon_pos[0], tp_icon_pos[1])

    for i in range(5):
        image_found = is_image_found(tp_home_icon_pos, './screenshots/tp_home_icon.png', 5000, False)

        if image_found:
            time.sleep(1)
            pyautogui.click(favorites_pos[0], favorites_pos[1])

            time.sleep(2)
            pyautogui.click(search_pos[0], search_pos[1])

            time.sleep(2)
            write_text(item_name)

            time.sleep(1)
            pyautogui.click(first_item_pos[0], first_item_pos[1])

            time.sleep(2)
            item_trade_opened = is_image_found(item_trade_pos, './screenshots/buy_indicator.png', 20000, False)

            if item_trade_opened:

                for j in range(quantity):

                    pyautogui.doubleClick(quantity_pos[0], quantity_pos[1])
                    write_text('250')
                    time.sleep(0.2)

                    pyautogui.doubleClick(price_pos[0], price_pos[1])
                    write_text(price)
                    time.sleep(0.2)

                    pyautogui.click(place_order_pos[0], place_order_pos[1])
                    time.sleep(0.2)

                    success = is_image_found(success_pos, './screenshots/success.png', 15000, False)

                    if success:
                        time.sleep(0.5)
                        pyautogui.click(ok_pos[0], ok_pos[1])

                # Close TP
                time.sleep(3)
                pyautogui.click(close_pos[0], close_pos[1])

                break


buy('piece of common unidentified gear', 5, '82')

# save_image(success_pos[0], success_pos[1], success_pos[2], success_pos[3], './screenshots/success.png')
# item_trade_opened = is_image_found(success_pos, './screenshots/success.png', 10000, False)
