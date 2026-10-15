import random

class Poisson:
    def __init__(self, position_x, position_y, temps_reproduction_poisson):
        '''Initialise un poisson avec une position x et y, un temps de reproduction,
        un symbole et un état initial.'''
        self.position_x = position_x
        self.position_y = position_y
        self.temps_reproduction_poisson = temps_reproduction_poisson
        self.symbole = '🦀'
        self.vivant = True
        self.compteur_repro_poisson = 0

    def reproduire(self, autre, ancienne_x, ancienne_y):
        '''Gère la logique de reproduction des poissons.'''
        #Si le compteur est atteint, un nouveau poisson est créé
        if self.compteur_repro_poisson >= self.temps_reproduction_poisson:
            p = Poisson(ancienne_x, ancienne_y, self.temps_reproduction_poisson)
            autre.poser(p)
            #On remet le compteur de reproduction 
            self.compteur_repro_poisson = 0
            return True
        return False

    def se_deplacer(self, autre):
        '''Permet au poisson de se déplacer dans la grille, si le poisson est vivant;
        identifie les cases libres pour s'y déplacer aléatoirement.'''
        #Si le poisson n'est pas vivant, il ne sera pas inclus
        if not self.vivant:
            return

        #On initialise une liste qui récupère les positions disponibles
        position = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if abs(x) + abs(y) == 1:
                    nouveau_x = (self.position_x + x) % autre.largeur 
                    nouveau_y = (self.position_y + y) % autre.hauteur 
                    #Si la case est vide, alors le poisson peut s'y déplacer
                    if autre.check(nouveau_x, nouveau_y) is None:
                        position.append([x, y])

        #S'il y a des positions disponibles autour de lui alors il en choisit une au hasard, sinon il ne se déplace pas
        if position:
            #On remplace son ancienne position par une case vide
            ancienne_x, ancienne_y = self.position_x, self.position_y
            autre.grille[ancienne_y][ancienne_x] = None

            #On place un poisson à l'ancienne position s'il atteint la reproduction
            self.reproduire(autre, ancienne_x, ancienne_y)

            #Choisit une position parmi celles récupérées
            choix = random.choice(position)
            self.position_x = (self.position_x + choix[0]) % autre.largeur 
            self.position_y = (self.position_y + choix[1]) % autre.hauteur 

            #On place le poisson sur la nouvelle position
            autre.grille[self.position_y][self.position_x] = self
            #On incrémente le compeur de reproduction
            self.compteur_repro_poisson += 1
        else:
            autre.grille[self.position_y][self.position_x] = self