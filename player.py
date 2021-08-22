
class Player :

    def _init_(self,name,pts_life, malus):
        self.name = name
        self._pts_life = pts_life 
        self._malus = malus
        
    def malus_action(self,malus):
        self._pts_life = self._pts_life - malus
        return self._pts_life


    def _get_pts_life(self):
        return self._pts_life

    def _set_pts_life(self,life):
        self._pts_life = life


    def _get_malus(self):
        return  self._malus
    
    def _set_malus(self,Malus):
        self._malus = Malus
        

    Life = property(_get_pts_life, _set_pts_life)
    X_malus = property(_get_malus,_set_malus)

