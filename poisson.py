import random

class Poisson:
    def __init__(self, position_x, position_y, temps_reproduction_poisson):
        self.position_x = position_x
        self.position_y = position_y
        self.temps_reproduction_poisson = temps_reproduction_poisson
        self.symbole = '🦀'
        self.vivant = True
        self.compteur_repro_poisson = 0

    def reproduire(self, autre, ancienne_x, ancienne_y):
        if self.compteur_repro_poisson >= self.temps_reproduction_poisson:
            p = Poisson(ancienne_x, ancienne_y, self.temps_reproduction_poisson)
            autre.poser(p)
            self.compteur_repro_poisson = 0
            return True
        return False

    def se_deplacer(self, autre):
        if not self.vivant:
            return

        position = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if abs(x) + abs(y) == 1:
                    nouveau_x = (self.position_x + x) % autre.largeur 
                    nouveau_y = (self.position_y + y) % autre.hauteur 
                    if autre.check(nouveau_x, nouveau_y) is None:
                        position.append([x, y])

        if position:
            ancienne_x, ancienne_y = self.position_x, self.position_y
            autre.grille[ancienne_y][ancienne_x] = None

            self.reproduire(autre, ancienne_x, ancienne_y)

            choix = random.choice(position)
            self.position_x = (self.position_x + choix[0]) % autre.largeur 
            self.position_y = (self.position_y + choix[1]) % autre.hauteur 

            autre.grille[self.position_y][self.position_x] = self
            self.compteur_repro_poisson += 1
        else:
            autre.grille[self.position_y][self.position_x] = self