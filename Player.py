import string


class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    @staticmethod
    def chose_name():
        # le joueur choisit un nom
        name = input("Veuillez choisir un nom")
        return name

    @staticmethod
    def chose_diff():
        chosen_diff = input("Veuillez choisir une difficulté : f pour facile et d pour difficile ").lower()
        while True :

            if chosen_diff == 'f' or chosen_diff == 'd':
                # print(chosen_diff)
                return chosen_diff

            else:
                chosen_diff = input("f ou d ? ").lower()

        # return facile, difficile

    @staticmethod
    def _chose_letter():
        chosen_letter = input("Veuillez choisir une lettre")

        if len(chosen_letter) > 1:
            raise LettreEnTropError("Choisissez une seule lettre !")

        if chosen_letter not in string.ascii_letters:
            raise NonLettreError("Non non non, c'est une lettre qu'il faut !")

        else:
            print(f"Voyons si la lettre {chosen_letter} est contenue dans le mot")
        return chosen_letter


class NonLettreError(Exception):
    pass


class LettreEnTropError(Exception):
    pass
