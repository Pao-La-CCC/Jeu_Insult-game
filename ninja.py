from player import Player

class Ninja(Player) :
    personality = ["Super Ninja est tellement sombre qu'il ne se voit pas dans l'ombre"]
    insult_ =["Tes shurikens","habits noirs","ninjas","de ton masque","les taupes","de Jackie Chan"]

    def __init__(self,name,pts_life,malus):
        super()._init_(name,pts_life,malus)