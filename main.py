from curves import Curve
from function import Function

if __name__ == '__main__':
    # labels for Lennard Jones graph
    labels_LJ = ["Energie d'interaction réduite totale",
                 "Energie réduite de répulsion",
                 "Energie réduite d'attraction"]
    # labels for interactive molecular forces
    labels_FIM = ["Force totale",
                  "Dérivé de l'énergie répulsive",
                  "Dérivé de l'énergie d'attraction"]
    # Ideal gas graph
    labels_IG = ["T = 300K",
                 "T = 400K",
                 "T = 500K"]

    crv = int(input("Choix du graph:\n\n"
                    "1: Potentiel de Lennard Jones\n"
                    "2: Force d'interaction entre molécules\n"
                    "3: Test\n\n"
                    "1, 2 ou 3: "))

    data = Function(crv, "CO2")

    if crv == 1:
        curve = Curve(labels_LJ, "Potentiel de Lennard Jones", "$\\frac{E_{p}}{\\varepsilon}$", "$\\frac{1}{r}$")
        curve.set_lim(0.5, 2.5, -1.5, 1.5)
    elif crv == 2:
        curve = Curve(labels_FIM, "Force d'interaction entre molécules", "$\\frac{F}{F_{0}}$", "r")
        curve.set_lim(0.5, 2.5, -6, 6)
    else:
        curve = Curve(labels_IG, "Représentation graphique mathématique\n de l'équation"
                                 " des gaz parfaits", "P", "V")
        curve.set_lim(-10, 10, -4000, 4000, True)

    curve.color_zone(crv)

    v, x, y1, y2, y3 = data.get_data()

    if crv == 3:
        curve.plot_data(v, y1, y2, y3)
    else:
        curve.plot_data(x, y1, y2, y3)
