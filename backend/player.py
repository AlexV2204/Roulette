class Player:
    def __init__(self, name, token):
        self.player_name = name
        self.player_token = token

    def generate_player(self):
        self.player_name = input("What's your name ? ")
        return self.player_name

    def player_drop(self, bet):
        self.bet = bet
        self.player_token -= self.bet
        return self.player_token

    def player_loot(self, choice):
        self.choice = choice
        if self.choice == "color":
            self.player_gain = self.bet * 2
        else:
            self.player_gain = self.bet * 3
        print("Vous avez gagné", self.player_gain, "jetons !!")
        self.player_token += self.player_gain
        return self.player_token
