from player import Player

combos = dict.fromkeys(("Ones", "Twos", "Threes", "Fours",
          "Fives", "Sixes", "Bonus", "Pair", 
          "2Pairs", "3K", "4K", "SS", "LS", "FH",
          "CH", "YA"), [None, None])

class Scoreboard:
    def __init__(self, sheet):
        self.sheet = sheet
    
    def update_score(self, score, player, combo):
        if player=="user1":
            combos[combo][0] = score
        else:
            combos[combo][1] = score