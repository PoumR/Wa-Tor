import random
from poisson import Poisson

class Requin(Poisson):
    """Classe représentant un requin prédateur dans un monde simulé, héritant de la classe Poisson.

    Attributs:
        position_x (int): Coordonnée horizontale actuelle sur la grille.
        position_y (int): Coordonnée verticale actuelle sur la grille.
        symbole (str): Représentation visuelle du requin (🦈).
        energie (int): Niveau d'énergie actuel du requin (géré par la faim et les repas).
        compteur_repro_requin (int): Compteur interne mesurant le temps écoulé avant la prochaine reproduction.
        vivant (bool): État de vie de l'entité (True si vivant, False si mort).
    """
    def __init__(self, position_x, position_y, temps_reproduction_requin, energie_initiale=8):
        super().__init__(position_x, position_y, temps_reproduction_requin)
        self.symbole = '🦈'
        self.energie = energie_initiale
        self.compteur_repro_requin = 0
        self.vivant = True

    def reproduire(self, autre, ancienne_x, ancienne_y):
        """Gère la reproduction du requin s'il a atteint son temps de reprpdiction.
        
        Crée un nouveau requin sur l'ancienne case lors du déplacement.
        """
        if self.compteur_repro_requin >= self.temps_reproduction_poisson:
            r = Requin(ancienne_x, ancienne_y, self.temps_reproduction_poisson)
            autre.poser(r)
            self.compteur_repro_requin = 0
            return True
        return False

    def manger(self, autre, choix_prio):
        """Gère la prédation si le requin choisit de manger un poisson."""
        # choix_prio contient [x, y, objet_poisson]
        requin_mange = choix_prio[2]
        
        # Le poisson meurt et on libère sa case sur la grille
        requin_mange.vivant = False
        autre.grille[requin_mange.position_y][requin_mange.position_x] = None 

        # On augmente l'énergie du requin 
        self.energie += 3
        if self.energie >= 12:
            self.energie = 12
        return True

    def se_deplacer(self, autre):
        """Gère le déplacement, la chasse, l'évolution de l'énergie et la reproduction du requin."""

        if not self.vivant:
            return

        position = []
        prio = []

        # Regarde les cases adjacentes (poissons ou de cases vides)
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if abs(x) + abs(y) == 1:
                    nouveau_x = (self.position_x + x) % autre.largeur
                    nouveau_y = (self.position_y + y) % autre.hauteur
                    case = autre.check(nouveau_x, nouveau_y)

                    # Si la case contient un poisson (qui n'est pas un requin), c'est une proie
                    if case is not None and isinstance(case, Poisson) and not isinstance(case, Requin):
                        prio.append([x, y, case])
                    elif case is None:
                        position.append([x, y])

        choix = None
        action_manger = False

        # Priorité à une case contenant un poisson
        if prio:
            choix = random.choice(prio)
            action_manger = True
        elif position:
            choix = random.choice(position)

        #Si le requin peut bouger (pour manger ou pour avancer dans l'eau)
        if choix:
            ancienne_x, ancienne_y = self.position_x, self.position_y
            autre.grille[ancienne_y][ancienne_x] = None

            # On tente la reproduction sur l'ancienne case
            self.reproduire(autre, ancienne_x, ancienne_y)

            # Mise à jour des coordonnées du requin
            self.position_x = (self.position_x + choix[0]) % autre.largeur
            self.position_y = (self.position_y + choix[1]) % autre.hauteur

            # Mange sinon perte d'énergie
            if action_manger:
                self.manger(autre, choix)
            else:
                self.energie -= 1

            # Placement du requin à sa nouvelle position
            autre.grille[self.position_y][self.position_x] = self
            self.compteur_repro_requin += 1
        else:
            # Même s'il est bloqué, il perd de l'énergie
            self.energie -= 1

        # Mort du requin si énergie à 0
        if self.energie <= 0:
            self.vivant = False
            autre.grille[self.position_y][self.position_x] = None