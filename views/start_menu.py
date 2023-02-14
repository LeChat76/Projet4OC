import os
MENU_PLAYERS = 1
MENU_TOURNAMENT = 2
MENU_RESULTS = 3
MENU_QUIT = 4


class MainMenu:

    def main_menu(self):
        """ Root menu """
        choix = None
        while choix != MENU_TOURNAMENT and choix != MENU_PLAYERS and choix != MENU_RESULTS and choix != MENU_QUIT:
            self.clear_screen()
            print("+-------------------------------+")
            print("|            MENU               |")
            print("+-------------------------------+")
            print("| 1 - joueurs                   |")
            print("| 2 - tournois                  |")
            print("| 3 - résultats                 |")
            print("| 4 - quitter                   |")
            print("+-------------------------------+")
            choix = input("Quel est votre choix : ")
            if not choix.isnumeric():
                print("Merci de préciser un choix numérique.")
                choix = None
            else:
                choix = int(choix)

        return choix

    @staticmethod
    def clear_screen():
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system('cls')
