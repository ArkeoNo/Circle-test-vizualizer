import matplotlib.pyplot as plt
import math

nomFichier = "result.csv"
rayon = 1

with open(nomFichier, "r") as f:
    f.readline()  # Passe la ligne de titres
    plt.figure(figsize=(7, 7))
    ax = plt.subplot(1, 1, 1)
    # Retirer les axes, leur graduation et lÃ©gende
    ax.tick_params(left=False, right=False, labelleft=False,
                   labelbottom=False, bottom=False)

    lignes = f.readlines()
    for ligne in lignes:  # Pour chaque ligne du fichier
        # Convertit la ligne "15;0\n" en 2 entiers: angle et couleur
        angle, couleur = list(map(int, ligne.split(";")))
        # print(angle, couleur)

        # Dessine le point selon son angle et la constante rayon
        if couleur == 1:  # Vert
            ax.plot(rayon * math.cos(math.radians(angle)),
                    rayon * math.sin(math.radians(angle)), "ro")
        else:  # Rouge
            ax.plot(rayon * math.cos(math.radians(angle)),
                    rayon * math.sin(math.radians(angle)), "go")

    plt.show()  # Affiche le diagramme