# IA Q-learning - Tic-Tac-Toe

Ce projet implémente une intelligence artificielle basée sur l'algorithme de **Q-learning** pour jouer au jeu du **Tic-Tac-Toe** (morpion). L'objectif est d'entraîner un robot à jouer de manière optimale en apprenant à partir de nombreuses parties simulées.

## Principe du jeu

Le **Tic-Tac-Toe** est un jeu à deux joueurs où chacun place à tour de rôle son symbole (X ou O) sur une grille 3x3. Le premier qui aligne trois de ses symboles horizontalement, verticalement ou en diagonale gagne la partie. Si la grille est remplie sans vainqueur, la partie est déclarée nulle (égalité).

## Algorithme utilisé : Q-learning

L'algorithme de **Q-learning** est une méthode d'apprentissage par renforcement qui permet au robot d'améliorer sa stratégie en mettant à jour une table de valeurs **Q** associée aux états du jeu.

### Paramètres d'apprentissage
- **Alpha (taux d'apprentissage)** : 0.1
- **Gamma (facteur de récompense)** : 0.8
- **Récompense de victoire** : +10000
- **Récompense de défaite** : -10000
- **Récompense d'égalité** : +10000
- **Épsilon (exploration vs exploitation)** : diminue progressivement pour favoriser l'exploitation à mesure que l'agent apprend.

## Structure du projet

- `main.py` : Code principal, entraînement et test de l'IA.
- `src/Player.py` : Classe du joueur (IA ou humain) et logique de choix d'action.
- `src/stats.py` : Fonctions de gestion de l'historique et mise à jour du Q-table.
- `README.md` : Ce fichier de présentation du projet.

## Exécution du programme

1. Assurez-vous d'avoir **Python** installé sur votre machine.
2. Créez un environnement virtuel (venv) :
   ```bash
   python -m venv venv
   ```
3. Activez l'environnement virtuel :

   Pour Windows :
   ```bash
   .\venv\Scripts\activate  
   ```
   Pour Linux :
   ```bash
   source ./venv/bin/activate
   ```

4. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

5. Lancez le programme :

   Pour Windows :
   ```bash
   python main.py
   ```
   Pour Linux :
   ```bash
   python3 main.py
   ```

6. Pour quitter l'environnement :
   ```bash
   deactivate
   ```

## Phases du programme

1. **Entraînement de l'IA** :
   - Un grand nombre de parties sont simulées (par défaut 100 000 ou plus).
   - La table **Q** est mise à jour après chaque partie pour améliorer les décisions du robot.
   - Le Q-table est sauvegardé pour être réutilisé lors des prochains lancements.
2. **Évaluation** :
   - L'IA affronte un joueur aléatoire ou humain.
   - Les statistiques de victoire, défaite et égalité sont affichées.

## Résultats et statistiques

Après l'entraînement, le programme affiche les performances de l'IA :

- Exemple (après 200 000 parties d'entraînement) :
  ```
  92.49% de victoire
  1.77% de défaite
  5.74% d'égalité
  ```

## Améliorations possibles

- Ajouter une interface graphique pour rendre le jeu plus interactif.
- Expérimenter avec d'autres méthodes d'apprentissage par renforcement.
- Affiner les hyperparamètres pour améliorer l'efficacité de l'entraînement (alpha, gamma, epsilon).
- Entraîner l'IA contre un adversaire parfait (algorithme Minimax).

## Auteur

Projet développé par Louis Verbrugge
