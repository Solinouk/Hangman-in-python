class Scores :

    def __init__(self, player_name, player_score):
        self. player_name = player_name
        self.player_score = player_score

    @staticmethod
    def store_score(name, score):
        # on stocke le score dans le fichier du joueur
        with open("./scores_pendu.txt", mode='a', encoding="utf8") as file:
            score_dict = dict()
            score_dict[name] = score
            file.write(str(score_dict))
        # print(listeMots)
        # print(score_dict)
        # return score_dict

    @ staticmethod
    def get_score(name) :
        with open("./scores_pendu.txt", mode='r', encoding="utf8") as file:

            for elmts in file :
                for names, score in enumerate(elmts) :
                    if name == names :

                        return names, score
                    else :
                        score = 0
                        return name, score


        # on récupère le score dans le fichier
        # par défaut le score est de zéro


