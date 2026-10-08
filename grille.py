class Grille: 
    def __init__(self,largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        # Crée une grille remplie d'eau
        self.grille = [['.' for _ in range(largeur)] for _ in range(hauteur)]


    def poser(self, x, y, especes):
        self.grille[y][x] = especes

    def check(self, x, y):
            return self.grille[y][x]

    def afficher(self):
        for ligne in self.grille:
            print(' '.join(ligne))

# Crée une grille de 10x5
grille = Grille(10, 5)

grille.poser(2,1, 'P')

grille.afficher()