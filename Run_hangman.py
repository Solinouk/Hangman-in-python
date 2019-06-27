import Player, Scores, Hangman

def main_hangman() :
    p = Player.Player
    nom = p.chose_name()
    p.chose_diff()
    s = Scores.Scores
    nom, score = s.get_score(nom)
    h = Hangman.Hangman
    rejouer = 'o'

    while rejouer == 'o' :
        mot1 = h.chose_word()
        displayed = ['-','-','-','-','-','-','-','-']

        while True :
            # s.store_score(mot1, displayed)
            scores, rejouer = h.game_over(mot1, displayed)
            break
        score = score + scores
        s.store_score(nom, score)
        print(score)
    print("à bientôt !")

main_hangman()