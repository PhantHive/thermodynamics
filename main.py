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

    labels_VDW = [
        "equation mathematique de \nVan der Waals",
        "asymptote en zéro",
        "asymptote en b"
    ]

    crv = int(input("Choix du graph:\n\n"
                    "1: Potentiel de Lennard Jones\n"
                    "2: Force d'interaction entre molécules\n"
                    "3: Gaz Parfait\n"
                    "4: Van Der Waals\n\n"
                    "1, 2, 3 ou 4: "))

    data = Function(crv)

    if crv == 1:
        curve = Curve(labels_LJ, "Potentiel de Lennard Jones", "$\\frac{r_{0}}{r}$", "$\\frac{E_{p}}{\\varepsilon}$")
        curve.set_lim(0.5, 2.5, -1.5, 1.5)
    elif crv == 2:
        curve = Curve(labels_FIM, "Force d'interaction entre molécules", "$\\frac{r}{r_{0}}$", "$\\frac{F}{F_{0}}$")
        curve.set_lim(0.5, 2.5, -6, 6)
    elif crv == 3:
        curve = Curve(labels_IG, "Représentation graphique mathématique\n de l'équation"
                                 " des gaz parfaits", "P", "V")
        curve.set_lim(-10, 10, -4000, 4000, True)
    else:
        curve = Curve(labels_VDW, "Equation mathématique de Van der Waals", "P", "V")
        curve.set_lim(-15, 15, -15, 15, True)

    curve.color_zone(crv)

    x, y1, y2, y3 = data.get_data()

    if crv == 3:
        v_pos, v_neg, y1, y2, y3, y4, y5, y6 = data.get_data_IG()
        curve.plot_data(v_pos, y1, y2, y3, y4, y5, y6, v_neg)
    elif crv == 4:
        vdw_neg, vdw_pos1, vdw_pos2, vdw_pos3, y1, y2, y3, y4 = data.get_data_VDW()
        curve.plot_data_vdw(vdw_neg, vdw_pos1, vdw_pos2, vdw_pos3, y1, y2, y3, y4)
    else:
        curve.plot_data(x, y1, y2, y3)
