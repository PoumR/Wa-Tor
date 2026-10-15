import random
from poisson import Poisson
from requin import Requin

class Grille: 
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = [[None for _ in range(largeur)] for _ in range(hauteur)]
        self.entites = []

    def poser(self, entite):
        self.grille[entite.position_y][entite.position_x] = entite
        if entite not in self.entites:
            self.entites.append(entite)

    def afficher(self, count) -> None:
        """Affiche la grille dans le terminal."""
        print('\n' + '─' * (self.largeur * 3))
        for y in range(self.hauteur):
            ligne = []
            for x in range(self.largeur):
                entite = self.grille[y][x]
                if entite is None:
                    ligne.append('💧')
                else:
                    symbole = getattr(entite, 'symbole', '?')
                    ligne.append(f'{symbole}')
            print(''.join(ligne))
        print('─' * (self.largeur * 3))

        # Statistiques
        nb_poissons = sum(1 for e in self.entites if getattr(e, 'symbole', '') == '🦀' and e.vivant)
        nb_requins = sum(1 for e in self.entites if getattr(e, 'symbole', '') == '🦈' and e.vivant)
        nb_cases_vides = sum(1 for y in range(self.hauteur) for x in range(self.largeur) if self.grille[y][x] is None)

        print(f"Itération {count}  -  🦀 Poissons : {nb_poissons}  |  🦈 Requins : {nb_requins}  |  💧 Cases vides : {nb_cases_vides}")

    def check(self, x, y):
        return self.grille[y][x]

    def peupler(self, nb_requin, nb_poisson, temps_reproduction_poisson=8, temps_reproduction_requin=7):
        poissons_poser = 0
        while poissons_poser < nb_poisson:
            x = random.randint(0, self.largeur - 1)
            y = random.randint(0, self.hauteur - 1)
            if self.grille[y][x] is None:
                p = Poisson(x, y, temps_reproduction_poisson)
                self.poser(p)
                poissons_poser += 1

        requins_poser = 0
        while requins_poser < nb_requin:
            x = random.randint(0, self.largeur - 1)
            y = random.randint(0, self.hauteur - 1)
            if self.grille[y][x] is None:
                r = Requin(x, y, temps_reproduction_requin)
                self.poser(r)
                requins_poser += 1