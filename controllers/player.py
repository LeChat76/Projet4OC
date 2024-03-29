import sys
from views.player import PlayerView
from models.player import PlayerModel
from constantes import MENU_PLAYER_CREATION, MENU_PLAYERS_DISPLAY, MENU_PLAYERS_DELETE, MENU_PLAYERS_EXIT


class PlayerController:
    """ Player controller """
    def __init__(self):
        self.player_view = PlayerView()

    def menu_player(self):
        """ Player menu """
        while True:
            choix = self.player_view.player_menu()
            if choix == MENU_PLAYER_CREATION:
                self.add_player()
            if choix == MENU_PLAYERS_DISPLAY:
                self.display_player()
            elif choix == MENU_PLAYERS_DELETE:
                self.delete_player()
            elif choix == MENU_PLAYERS_EXIT:
                break

    def add_player(self, associate_to_tournament=False):
        """ Method for recording new players """
        players_list = self.player_view.add_player(associate_to_tournament)
        players_obj_list = []
        for player in players_list:
            player = PlayerModel(player_uuid=player[4], player_fname=player[0],
                                 player_name=player[1], player_birthd=player[2], player_clubid=player[3])
            players_obj_list.append(player)
            player.save_player()
        return players_obj_list

    def delete_player(self):
        """ method to delete players """
        while True:
            players_list = PlayerModel.search_all_players()
            if players_list == "no_result":
                self.player_view.choice("Aucun joueur, merci d'en créer. Appuyez sur [ENTRER] pour revenir au menu.")
                break
            elif players_list == "error":
                self.player_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                               " le et recommencez.")
                sys.exit()
            player_to_delete = self.player_view.delete_player(players_list)
            player_deleted = player_to_delete.delete_player()
            self.player_view.text_to_print("Utilisateur " + player_deleted + " supprimé.")
            choix = self.player_view.choice("Supprimer un autre joueur(O/n)?")
            if choix == "N":
                break

    def display_player(self):
        """ method to display players by selecting name or all players """
        # test if players.json is empty
        players_list = PlayerModel.search_all_players()
        if players_list == "no_result":
            self.player_view.choice("Liste vide. Veuillez en créer. Appuyez sur [ENTRER] pour revenir au menu.")
        else:
            while True:
                players_list = PlayerModel.search_all_players()

                # case of error structure file players.json
                if players_list == "error":
                    self.player_view.text_to_print("Problème de structure sur fichier tournaments.json.\nVérifiez"
                                                   " le et recommencez.")
                    sys.exit()

                player_to_search = self.player_view.display_player()

                # case when you want to display all users [ENTER]
                if player_to_search == "display_all":
                    self.player_view.text_to_print(str(len(players_list)) + " résultat(s).")
                    for player in players_list:
                        self.player_view.text_to_print(player)
                    choix = self.player_view.choice("Faire une autre recherche (O/n)? ")
                    if choix == "N":
                        break

                # case when you specify a name and there is some results
                else:
                    players_list = PlayerModel.search_player(player_to_search)
                    if players_list == "no_result":
                        choix = self.player_view.choice("Aucun résultat. Faire une autre recherche (O/n)? ")
                        if choix.upper() == "N":
                            break
                    else:
                        self.player_view.text_to_print(str(len(players_list)) + " résultat(s):")
                        for player in players_list:
                            self.player_view.text_to_print(player)
                        choix = self.player_view.choice("Faire une autre recherche (O/n)? ")
                        if choix.upper() == "N":
                            break
