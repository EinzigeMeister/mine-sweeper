from helpers import Display, GameBoard, Choices, Login
if __name__ == '__main__':

    display = Display()
    display.welcome_message()
    user_logged_in = None
    while not user_logged_in:
        user_logged_in = Login()
    menu_option_selected = 0
    while not menu_option_selected ==4:
        print(user_logged_in.user)
        print('cont')
        menu_option_selected = Choices.main_menu(user_logged_in.user)
        if menu_option_selected == 1:
            Choices.show_user_results(user_logged_in.user)
        if menu_option_selected == 2:
            Choices.show_recent_results
        if menu_option_selected == 3:
            Choices.play_game(user_logged_in.user)
        if menu_option_selected == 4:
            print("Goodbye!")

