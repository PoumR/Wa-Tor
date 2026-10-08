import random

class Poisson:
    def __init__(self, temps_reproduction_poisson, position_x, position_y):
        self.temps_reproduction_poisson = temps_reproduction_poisson
        self.position_x = position_x
        self.position_y = position_y


    def se_deplacer(position_x, position_y):
        position_disponible = []
        if position_x + 1 == '.':
            position_disponible.append(position_x + 1)
        if position_x - 1 == '.':
            position_disponible.append(position_x - 1)
        '''if position_y + 1 == '.':
            position_disponible.append(position_y + 1)
        if position_y - 1 == '.':
            position_disponible.append(position_y - 1)'''

        position_x = random.choice(position_disponible)
        

          


    def se_reproduire(self):
        if self.temps_reproduction_poisson == 8:
            pass

    def mourir(age):
            pass