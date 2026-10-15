import time

class World:
    def __init__(self, grille):
        self.grille = grille
        self.tour_actuel = 0

    def executer_tour(self):
        self.tour_actuel += 1
        for entite in list(self.grille.entites):
            entite.se_deplacer(self.grille)
        
        # Nettoyage des entités mortes
        self.grille.entites = [e for e in self.grille.entites if e.vivant]
        self.grille.afficher(self.tour_actuel)

    def lancer_simulation(self, vitesse_pause=0.6):
        self.grille.afficher(self.tour_actuel)
        try:
            while True:
                self.executer_tour()
                time.sleep(vitesse_pause)
        except KeyboardInterrupt:
            print("\nSimulation arrêtée par l'utilisateur.")