import random, Player


class Hangman :

    def __init__(self, nb_letters):
        self.nb_letters = nb_letters

    @ staticmethod
    def chose_word():
        with open("./words_8_letters.txt", mode='r', encoding="utf8") as file:
            listeMots = list()
            [listeMots.append(l.split()) for l in file]

        mot = [random.choice(m) for m in listeMots]
        mot = mot[0]
        return mot

    @ staticmethod
    def _check_letter(word):
        while True:
            try:
                letter = Player.Player._chose_letter().upper()
            except Player.NonLettreError as e:
                print(e.args)

            except Player.LettreEnTropError as e:
                print(e.args)
            else:
                break

        indexe = []
        correct = False

        if letter in word :
            correct = True
            for index, letters in enumerate(word):
                if letter == letters :
                    indexe.append(index)
            return letter, indexe, correct

        else :
            print('dommage')
            # Pendu.display_hangman()
            return letter, indexe, correct

    @staticmethod
    def display_word(word, displayed):

        # on récupère la bonne lettre et son indice après vérification par la fonction check
        good_letter, index, correct = Hangman._check_letter(word)
        # pour chaque bonne lettre on l'affiche  au bon endroit dans le mot
        for elmts in index:
            displayed[elmts] = good_letter.upper()

        print("".join(displayed))
        return displayed, correct

    def display_hangman(self):
        #
        # if try == 1 :
        #     display element 1
        # if try == 2 :
        #     display element 2

        pass

    @staticmethod
    def game_over(word, displayed):
        # tries = Hangman.count_tries(mot, tries)
        tries = 10
        while True :
            displayed, correct = Hangman.display_word(word, displayed)

            if correct :
                print(f'Bravo ! Il vous reste {tries} essais')
                if "".join(displayed) == word:
                    print(f"Vous avez gagné {tries} points")
                    replay = input('Voulez-vous rejouer ?')
                    return tries, replay

                else :
                    pass

            else :
                tries -= 1
                if tries == 0:
                    # print('le jeu est terminé', tries)
                    print(f'Vous avez perdu. Le mot était : {word}')
                    replay = input('voulez_vous rejouer ?')
                    return tries, replay

                elif tries > 0:
                    print(f'Dommage... Il vous reste : {tries} essais')
                    pass



