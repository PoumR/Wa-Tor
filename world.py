import time

class World:
    """Classe représentant le monde de la simulation, gérant le déroulement temporel et l'exécution des tours.

    Attributs:
        grille (Grille): Espace de simulation sous forme de grille contenant toutes les entités.
        tour_actuel (int): Compteur mesurant le nombre de tours/itérations écoulés depuis le début.
    """
    def __init__(self, grille):
        self.grille = grille
        self.tour_actuel = 0

    def executer_tour(self):
        """Exécute un tour complet de simulation : déplacement des entités, gérer les entitées mortes et affichage."""

        # Incrémente le compteur de tours au début de chaque cycle
        self.tour_actuel += 1

        # Traite chaque entité en toute sécurité (utilisation d'une copie pour éviter les erreurs en cours de boucle)
        for entite in list(self.grille.entites):
            entite.se_deplacer(self.grille)
        
        # Nettoyage des entités mortes
        self.grille.entites = [e for e in self.grille.entites if e.vivant]

        # Actualise l'affichage de la grille et des statistiques pour le tour
        self.grille.afficher(self.tour_actuel)

    def lancer_simulation(self, vitesse_pause=0.6):
        """Lance la boucle principale de la simulation en continu avec un délai ajustable."""
        # Réinitialise la console une seule fois avant de démarrer pour avoir un affichage propre
        print("\033[2J", end="")
        
        self.grille.afficher(self.tour_actuel)
        try:
            while True:
                self.executer_tour()
                time.sleep(vitesse_pause)
        except KeyboardInterrupt:
            print("\nSimulation arrêtée par l'utilisateur.")