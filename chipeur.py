from player import Player


class Chipeur(Player):
    personality = ["Ce renard tout aussi filou que roux est un voleur de renommée international qui n'a jamais su  "
                   "protéger son butin de la plus aventurière des petites filles : Mlle Dora."]

    insult_ = ["un renard", "ni discret","les voleurs"]

    def __init__(self, name, pts_life,malus):
        super()._init_(name, pts_life,malus)
