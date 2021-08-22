from player import Player

class GreatMother(Player) :
    personality = ["La mamie des mamie qui va en slowmotion est là, avec beaucoup de retard super grand mère arrivera bientot"]
    insult_ =["si lente","une tortue"]

    def __init__(self, name, pts_life,malus):
        super()._init_(name, pts_life,malus)