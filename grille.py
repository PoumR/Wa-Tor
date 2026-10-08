class Grille: 
    def __init__(self,largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

        self.grille = [[' ' for _ in range(largeur)] for _ in range(hauteur)]

    def afficher(self):
        for ligne in self.grille:
            print(' '.join(ligne))

# Crée une grille de 10x5
g = Grille(10, 5)

g.afficher()