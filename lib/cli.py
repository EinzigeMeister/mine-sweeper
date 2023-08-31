from helpers import Display, GameBoard, Choices, Login, session
import os
if __name__ == '__main__':
    choices = Choices()
    display = Display()
    os.system('clear')
    display.welcome_message()
    user_logged_in = None
    while not user_logged_in:
        user_logged_in = Login()
    menu_option_selected = 0
    while not menu_option_selected ==4:
        menu_option_selected = choices.main_menu(user_logged_in)
        if menu_option_selected == 1:
            choices.show_user_results(user_logged_in)
        if menu_option_selected == 2:
            choices.show_recent_results(user_logged_in)
        if menu_option_selected == 3:
            choices.play_game(user_logged_in)
        if menu_option_selected == 4:
            print("Goodbye!")

