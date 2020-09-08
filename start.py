import random as rd

from backend.player import Player

if __name__ == "__main__":

    print("Welcome to the Bellagio !")
    # Constante
    choice = ["c", "n", "color", "number"]
    color = ["red", "black"]
    exit = ["o", "n", "yes", "no"]
    # Création du joueur
    player = Player("", 1000)
    player.generate_player()
    player_name = player.player_name
    print("Bonjourno", player_name, "!")
    play = True

    while play:

        # Choix du joueur.
        player_choice = 37
        while player_choice not in choice:
            player_choice = input("What's your choice ? [Color/Number] ").lower()
            # Le joueur choisit une couleur.
        if player_choice == "c" or player_choice == "color":
            while player_choice not in color:
                player_choice = input("Which color ? [Black/Red] ").lower()
                if player_choice == "r":
                    player_choice = "red"
                elif player_choice == "b":
                    player_choice = "black"
        # Le joueur choisit un nombre.
        elif player_choice == "n" or player_choice == "number":
            while player_choice < 0 or player_choice > 36:
                while not player_choice.isnumeric():
                    player_choice = input("Which number ? [0-36] ")
                player_choice = int(player_choice)

        # Pari du joueur.
        player_token = player.player_token
        player_drop = 0
        print("You have", player_token, "tokens.")
        while player_drop < 5 or player_drop > player_token:
            player_drop = "n"
            while not player_drop.isnumeric():
                player_drop = input("What's your bet ? [5-" + str(player_token) + "] ")
            player_drop = int(player_drop)
        player.player_drop(player_drop)
        print("All bets are off !")

        # La roulette tourne.
        number = rd.randint(0, 36)

        # Association du nombre à sa couleur.
        if number == 0:
            color_number = "green"
        elif number % 2 == 1:
            color_number = "black"
        else:
            color_number = "red"
        result = [number, color_number]
        print(result[0], result[1])

        # Résultat.
        if player_choice == result[0]:
            print("Win by the number !!")
            player.player_loot("number")
        elif player_choice == result[1]:
            print("Win by the color !!")
            player.player_loot("color")
        else:
            print("Perdu...")
            print("Vous avez perdu", player_drop, "jetons...")

        # Choix de continuer.
        end = 0
        while end not in exit:
            end = input("Voulez-vous continuer ? [Yes/No] ").lower()
        if end == "n" or end == "no":
            play = False

    print("Arrivederci", player_name, "!")
