from math import floor, ceil
import os
from constantes import MENU_REPORT_TOURNAMENT_PLAYERS, MENU_REPORT_PLAYER_NAME, MENU_REPORT_EXIT,\
    MENU_REPORT_TOURNAMENT_SCORES, MENU_REPORT_PLAYER_FNAME, MENU_RESULT_TOURNAMENT_LIST,\
    MENU_RESULT_TOURNAMENT_DETAIL, REPORT_TABLE_WIDTH, PLAYER_MAX_LENGTH, REPORT_MATCH_WIDTH, MENU_REPORT_EXPORT_HTML


class ReportView:
    """ Result class """

    def report_menu(self):
        """ Menu 3 """
        choix = None
        while choix != MENU_REPORT_TOURNAMENT_PLAYERS and choix != MENU_REPORT_PLAYER_NAME and choix !=\
                MENU_REPORT_EXIT and choix != MENU_REPORT_TOURNAMENT_SCORES and choix != \
                MENU_REPORT_PLAYER_FNAME and choix != MENU_RESULT_TOURNAMENT_LIST and choix != \
                MENU_RESULT_TOURNAMENT_DETAIL and choix != MENU_REPORT_EXPORT_HTML:
            self.clear_screen()
            print("+-------------------------------+")
            print("|       MENU RAPPORTS           |")
            print("+-------------------------------+")
            print("| 1 - score d'un tournoi/joueurs|")
            print("| 2 - score d'un tournoi/score  |")
            print("| 3 - liste des joueurs/nom     |")
            print("| 4 - list des joueurs/prénom   |")
            print("| 5 - liste des tournois        |")
            print("| 6 - détail d'un tournoi       |")
            print("| 7 - export tournois html      |")
            print("| 8 - revenir au menu principal |")
            print("+-------------------------------+")
            choix = input("Quel est votre choix : ")
            if not choix.isnumeric():
                print("Merci de préciser un choix numérique.")
                choix = None
            else:
                choix = int(choix)
        self.clear_screen()
        return choix

    def display_scores_players(self, tournaments_scores, rounds_list_details, tournament_start_date,
                               tournament_end_date, tournament_name, players_scores):
        """ method to display all scores for one tournament displayed with names details """
        self.clear_screen()
        rounds_list = tournaments_scores[0]
        matchs_list = tournaments_scores[1]
        p1names_list = tournaments_scores[2]
        p2names_list = tournaments_scores[3]
        p1scores_list = tournaments_scores[4]
        p2scores_list = tournaments_scores[5]
        round_max = tournaments_scores[6]
        index = 0

        # print report's table (title)
        print("+" + "=" * REPORT_TABLE_WIDTH + "+")
        blank_width = (REPORT_TABLE_WIDTH - len('Tournoi "' + tournament_name + '"') - 2) / 2
        blank_width2 = (REPORT_TABLE_WIDTH - len("Du : " + str(tournament_start_date) + " au : "
                                                 + str(tournament_end_date)) - 1) / 2
        print('+' + ' ' * floor(blank_width) + ' Tournoi "' + tournament_name + '" ' + ' ' * ceil(blank_width) + '+')
        print("+" + " " * floor(blank_width2) + " Du : " + str(tournament_start_date) + " au : "
              + str(tournament_end_date) + " " * ceil(blank_width2) + "+")
        print("+" + "=" * REPORT_TABLE_WIDTH + "+")
        for round_nb in range(1, int(round_max) + 1):
            round_start = rounds_list_details[round_nb - 1]['startDate']
            round_end = rounds_list_details[round_nb - 1]['endDate']
            # print title round number
            blank_width = (REPORT_TABLE_WIDTH - len("Round " + str(round_nb)) - 2) / 2
            blank_width2 = (REPORT_TABLE_WIDTH - len("Du : " + str(round_start) + " au : " + str(round_end))) / 2
            print("+" + " " * floor(blank_width) + " Round  " + str(round_nb) + " " * ceil(blank_width) + "+")
            print("+" + " " * floor(blank_width2) + "Du : " + str(round_start) + " au : "
                  + str(round_end) + " " * ceil(blank_width2) + "+")
            print("+" + "-" * REPORT_TABLE_WIDTH + "+")
            # print scores table
            for round in rounds_list:
                if int(round) == round_nb:
                    match = matchs_list[index]
                    p1name = p1names_list[index]
                    p2name = p2names_list[index]
                    p1score = p1scores_list[index]
                    p2score = p2scores_list[index]
                    if p1score > p2score:
                        winner = p1name
                    elif p1score < p2score:
                        winner = p2name
                    else:
                        winner = "match nul"
                    blank_width = (REPORT_TABLE_WIDTH - len("Match " + str(match) + " opposant " + str(p1name) +
                                                            " à " + str(p2name))) / 2
                    print("+" + " " * floor(blank_width) + "Match " + str(match) + " opposant " + str(p1name) +
                          " à " + str(p2name) + " " * ceil(blank_width) + "+")
                    blank_width = (REPORT_TABLE_WIDTH - len("Vainqueur : " + str(winner))) / 2
                    print("+" + " " * floor(blank_width) + "Vainqueur : " + winner + " " * ceil(blank_width) + "+")
                    index += 1
            print("+" + "-" * REPORT_TABLE_WIDTH + "+")
        # print final results
        blank_width = (REPORT_TABLE_WIDTH - len("Résultats(triés par score)")) / 2
        print("+" + " " * floor(blank_width) + "Résultats(triés par score)" + " " * ceil(blank_width) + "+")
        print("+" + "-" * REPORT_TABLE_WIDTH + "+")
        for i in range(len(players_scores[0])):
            blank_width = (REPORT_TABLE_WIDTH - len("- " + str(players_scores[0][i]) + " - score : "
                                                    + str(players_scores[1][i])))
            print("+ - " + str(players_scores[0][i]) + " - score : " + str(players_scores[1][i])
                  + " " * (blank_width - 1) + "+")
        print("+" + "-" * REPORT_TABLE_WIDTH + "+")
        input("Appuyez sur [ENTRER] pour retourner au menu.")

    def display_scores_scores(self, tournaments_scores, rounds_list_details, tournament_start_date,
                              tournament_end_date, tournament_name, players_scores):
        """ method to display all scores for one tournament displayed with scores details """
        self.clear_screen()
        rounds_list = tournaments_scores[0]
        matchs_list = tournaments_scores[1]
        p1names_list = tournaments_scores[2]
        p2names_list = tournaments_scores[3]
        p1scores_list = tournaments_scores[4]
        p2scores_list = tournaments_scores[5]
        round_max = tournaments_scores[6]
        index = 0

        # print report's table (title)
        print("+" + "=" * REPORT_TABLE_WIDTH + "+")
        blank_width = (REPORT_TABLE_WIDTH - len('Tournoi "' + tournament_name + '"') - 2) / 2
        blank_width2 = (REPORT_TABLE_WIDTH - len("Du : " + str(tournament_start_date) + " au : "
                                                 + str(tournament_end_date)) - 1) / 2
        print('+' + ' ' * floor(blank_width) + ' Tournoi "' + tournament_name + '" ' + ' ' * ceil(blank_width) + '+')
        print("+" + " " * floor(blank_width2) + " Du : " + str(tournament_start_date) + " au : "
              + str(tournament_end_date) + " " * ceil(blank_width2) + "+")
        print("+" + "=" * REPORT_TABLE_WIDTH + "+")
        for round_nb in range(1, int(round_max) + 1):
            round_start = rounds_list_details[round_nb - 1]['startDate']
            round_end = rounds_list_details[round_nb - 1]['endDate']
            # print title round number
            blank_width = (REPORT_TABLE_WIDTH - len("Round " + str(round_nb)) - 2) / 2
            blank_width2 = (REPORT_TABLE_WIDTH - len("Du : " + str(round_start) + " au : " + str(round_end)))/2
            print("+" + " " * floor(blank_width) + " Round  " + str(round_nb) + " " * ceil(blank_width) + "+")
            print("+" + " " * floor(blank_width2) + "Du : " + str(round_start) + " au : "
                  + str(round_end) + " " * ceil(blank_width2) + "+")
            print("+" + "-" * REPORT_TABLE_WIDTH + "+")
            # print scores table
            for round in rounds_list:
                if int(round) == round_nb:
                    match = matchs_list[index]
                    p1name = (p1names_list[index])[:PLAYER_MAX_LENGTH]
                    p2name = (p2names_list[index])[:PLAYER_MAX_LENGTH]
                    p1score = p1scores_list[index]
                    p2score = p2scores_list[index]
                    blank_match_width = (REPORT_MATCH_WIDTH - len(str(" Match ")) - len(str(match)))
                    blank_score_width = (REPORT_TABLE_WIDTH - REPORT_MATCH_WIDTH - len(str(p1score))
                                         - len(str(p2score)) - len("|+"))/3
                    p1_blank = (PLAYER_MAX_LENGTH - len(p1name))
                    p2_blank = (PLAYER_MAX_LENGTH - len(p2name))
                    print("+" + " Match " + str(match) + " " * int(blank_match_width) + " | " + " " * floor(p1_blank)
                          + str(p1name) + " VS " + str(p2name) + " " * ceil(p2_blank) + " +")
                    if isinstance(p1score, float):
                        score_float = "+"
                    else:
                        score_float = " +"
                    print("+ Scores            | " + " " * floor(blank_score_width) + str(p1score) + " "
                          * floor(blank_score_width) + str(p2score) + " " * floor(blank_score_width)
                          + str(score_float))
                    index += 1
            print("+" + "-" * REPORT_TABLE_WIDTH + "+")
        # print final results
        blank_width = (REPORT_TABLE_WIDTH - len("Résultats(triés par score)")) / 2
        print("+" + " " * floor(blank_width) + "Résultats(triés par score)" + " " * ceil(blank_width) + "+")
        print("+" + "-" * REPORT_TABLE_WIDTH + "+")
        for i in range(len(players_scores[0])):
            blank_width = (REPORT_TABLE_WIDTH - len("- " + str(players_scores[0][i]) + " - score : "
                                                    + str(players_scores[1][i])))
            print("+ - " + str(players_scores[0][i]) + " - score : " + str(players_scores[1][i])
                  + " " * (blank_width - 1) + "+")
        print("+" + "-" * REPORT_TABLE_WIDTH + "+")
        input("Appuyez sur [ENTRER] pour retourner au menu.")

    def choice(self, question):
        """ method for asking to restart request """
        # self.question = question
        choix = ""
        while choix.upper() != "O" or choix.upper() != "N":
            choix = input(question)
            if choix.upper() == "O" or choix == "":
                return "O"
            elif choix.upper() == "N":
                return "N"

    def display_tournament_details(self, tournament):
        """ method to display tournament details for reporting menu """
        ReportView().clear_screen()
        print(f'Tournoi "{tournament.tournament_name}" se déroulant à {tournament.tournament_town} et comportant'
              f' {tournament.tournament_nb_round} round(s).')
        print(f"Description : {tournament.tournament_description}.")
        if tournament.tournament_end_date:
            print(f"Ce tournoi a démarré le {tournament.tournament_start_date} et s'est terminé"
                  f" le {tournament.tournament_end_date}.")
        if tournament.tournament_start_date and not tournament.tournament_end_date:
            print(f"Ce tournoi a démarré le {tournament.tournament_start_date} mais n'est pas terminé,"
                  f" {tournament.tournament_current_round} round(s) sur {tournament.tournament_nb_round} joué(s).")
        if tournament.tournament_start_date:
            print("Il y'a eu " + str(int(len(tournament.tournament_list_rounds) *
                                         len(tournament.tournament_list_players)/2))
                  + " match(s) joué(s).")
        if not tournament.tournament_start_date:
            print("Ce tournoi n'a pas encore démarré.")

    def text_to_print(self, text):
        """ method to print text from controller """
        print(text)

    def clear_screen(self):
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system('cls')
