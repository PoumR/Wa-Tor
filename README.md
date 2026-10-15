# Simulation Requins / Poissons

Simulation proies-prédateurs en Python, affichée directement dans le terminal.
Des poissons (🦀) et des requins (🦈) évoluent sur une grille : les poissons se déplacent et se reproduisent, les requins les chassent pour survivre.

## Aperçu

```
────────────────────────────────────────────────────────────
💧💧🦀💧💧💧🦈💧💧💧💧🦀💧💧💧💧💧💧💧💧
💧🦀💧💧💧💧💧💧🦀💧💧💧💧💧🦈💧💧💧💧💧
...
────────────────────────────────────────────────────────────
Itération 12  -  🦀 Poissons : 143  |  🦈 Requins : 18  |  💧 Cases vides : 239
```

## Prérequis

- Python 3.6 ou supérieur
- Aucune dépendance externe (uniquement la bibliothèque standard : `random`, `time`)
- Un terminal qui affiche correctement les emojis

## Lancement

```bash
python main.py
```

Pour arrêter la simulation, utiliser `Ctrl + C`.

## Règles de la simulation

La grille est **torique** : une entité qui sort d'un bord réapparaît du côté opposé. Les déplacements se font dans les 4 directions (haut, bas, gauche, droite).

### Poissons

- Se déplacent à chaque tour vers une case voisine vide, choisie au hasard.
- Se reproduisent quand leur compteur atteint `temps_reproduction_poisson` (8 par défaut) : un nouveau poisson apparaît sur la case qu'ils viennent de quitter.
- Restent sur place s'ils n'ont aucune case libre autour d'eux.

### Requins

- Priorité à la chasse : si un poisson est sur une case voisine, le requin s'y déplace et le mange (+1 énergie, plafonnée à 6).
- Sinon, il se déplace vers une case vide au hasard et perd 1 énergie.
- S'il est bloqué, il perd aussi 1 énergie.
- Il meurt quand son énergie tombe à 0.
- Il se reproduit quand son compteur atteint `temps_reproduction_requin` (7 par défaut), sur la case qu'il vient de quitter.
- Énergie initiale : 6.

## Structure du projet

```
.
├── main.py       # Point d'entrée : crée la grille, la peuple et lance le monde
├── world.py      # Classe World : boucle de simulation et gestion des tours
├── grille.py     # Classe Grille : plateau, placement, affichage, peuplement
├── poisson.py    # Classe Poisson : déplacement et reproduction
└── requin.py     # Classe Requin (hérite de Poisson) : chasse, énergie, mort
```

### Diagramme de classes (résumé)

- `World` possède une `Grille`.
- `Grille` contient une liste `entites` de `Poisson` et de `Requin`.
- `Requin` hérite de `Poisson` et redéfinit `reproduire` et `se_deplacer`, en ajoutant `manger` et l'attribut `energie`.

## Configuration

Les paramètres se règlent dans `main.py` :

```python
ma_grille = Grille(20, 20)                              # largeur, hauteur
ma_grille.peupler(nb_poisson=150, nb_requin=20)         # population initiale
mon_monde.lancer_simulation(vitesse_pause=0.6)          # pause entre deux tours (secondes)
```

Les temps de reproduction sont des paramètres de `Grille.peupler` :

```python
ma_grille.peupler(
    nb_poisson=150,
    nb_requin=20,
    temps_reproduction_poisson=8,
    temps_reproduction_requin=7,
)
```

L'énergie initiale d'un requin se règle dans le constructeur de `Requin` (`energie_initiale=6`).

> Attention : le nombre total d'entités (poissons + requins) ne doit pas dépasser le nombre de cases de la grille.


