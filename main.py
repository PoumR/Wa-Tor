from grille import Grille
from world import World

if __name__ == "__main__":
    # 1. Création de la grille
    ma_grille = Grille(35, 35)

    # 2. Peuplement initial
    ma_grille.peupler(nb_poisson=350, nb_requin=12, temps_reproduction_poisson=3, temps_reproduction_requin=18)

    # 3. Initialisation du Monde
    mon_monde = World(ma_grille)

    # 4. Lancement de la simulation
    mon_monde.lancer_simulation(vitesse_pause=0.6)