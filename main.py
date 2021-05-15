import random

import matplotlib.pyplot as plt
import numpy as np


def dark_style():
    # style
    plt.style.use("seaborn-dark")
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#151515'  # bluish dark grey
    for param in ['text.color', 'xtick.color', 'grid.color', 'ytick.color', 'axes.labelcolor']:
        plt.rcParams[param] = 'white'  # very light grey

    plt.grid(color='#2A3459')  # bluish dark grey, but slightly lighter than background

    # ==========================


def neon_curve(x, y1, y2=None, y3=None):
    n_lines = 10
    diff_linewidth = 1.05
    alpha_value = 0.03

    for n in range(1, n_lines + 1):
        plt.plot(x, y1,
                 linewidth=2 + (diff_linewidth * n),
                 alpha=alpha_value,
                 color='#08F7FE')

        plt.plot(x, y2,
                 linewidth=2 + (diff_linewidth * n),
                 alpha=alpha_value,
                 color='#00ff41')

        plt.plot(x, y3,
                 linewidth=2 + (diff_linewidth * n),
                 alpha=alpha_value,
                 color='#FE53BB')


class Curve:

    def __init__(self, labels, title):
        self.labels = labels
        self.title = title
        dark_style()

    def plot_data(self, x, y1, y2=None, y3=None):
        plt.plot(x, y1, label=self.labels[0], color='#08F7FE')
        plt.plot(x, y2, label=self.labels[1], color='#00ff41')
        plt.plot(x, y3, label=self.labels[2], color='#FE53BB')
        plt.legend(facecolor="black", frameon=True)

        plt.title(self.title, y=-0.14, fontsize=15, style="italic")

        neon_curve(x, y1, y2, y3)

        plt.grid(which='both', b=True, color="0.5")
        plt.grid(which='minor', b=True, color="0.2", alpha=0.5)

        plt.show()

    @staticmethod
    def color_zone(crv):

        if crv == 1:
            plt.axvspan(0, 1, facecolor='#08F7FE', alpha=0.15, label='zone répulsive')
            plt.axvspan(1, 2, facecolor='#00ff41', alpha=0.15, label='zone attractive')
            plt.axvspan(2, 2.5, facecolor='#FE53BB', alpha=0.15, label='zone sans interaction')
        else:
            plt.axvspan(0.5, 1, facecolor='#980D8E', alpha=0.15)

    @staticmethod
    def set_lim(x_min, x_max, y_min, y_max):
        plt.xlim((x_min, x_max))
        plt.ylim((y_min, y_max))
        plt.xticks([0.5, 1, 1.5, 2, 2.5])
        plt.gca().spines['bottom'].set_position(('data', 0))

        if y_max == 6:
            y_step = 0.4
        else:
            y_step = 0.1

        grid_x_ticks = np.arange(x_min, x_max, 0.1)
        grid_y_ticks = np.arange(y_min, y_max, y_step)

        plt.gca().set_xticks(grid_x_ticks, minor=True)
        plt.gca().set_yticks(grid_y_ticks, minor=True)


class Function:

    def __init__(self, crv=1):
        self.alpha = self.beta = 1
        self.crv = crv
        self.x = [p / 100.0 for p in range(50, 251, 1)]
        self.y_inter = []
        self.y_rep = []
        self.y_attr = []
        self.set_data()

    def E_attr(self, r):
        return -2 * self.beta / r ** 6

    def E_rep(self, r):
        return self.alpha / r ** 12

    def E_inter(self, r):
        return self.E_rep(r) + self.E_attr(r)

    def der_attr(self, r):
        return -12 * self.beta / r ** 7

    def der_rep(self, r):
        return +12 * self.alpha / r ** 13

    def t_force(self, r):
        return self.der_rep(r) + self.der_attr(r)

    def set_data(self):
        for j in range(len(self.x)):

            if self.crv == 1:
                y_res1 = self.E_rep(self.x[j])
                y_res2 = self.E_attr(self.x[j])
                y_res3 = self.E_inter(self.x[j])
                self.y_rep.append(y_res1)
                self.y_attr.append(y_res2)
                self.y_inter.append(y_res3)

            if self.crv == 2:
                y_res1 = self.der_rep(self.x[j])
                y_res2 = self.der_attr(self.x[j])
                y_res3 = self.t_force(self.x[j])
                self.y_rep.append(y_res1)
                self.y_attr.append(y_res2)
                self.y_inter.append(y_res3)

    def get_data(self):
        return self.x, self.y_inter, self.y_rep, self.y_attr


if __name__ == '__main__':
    labels = ["Energie d'interaction réduite totale",
              "Energie réduite de répulsion",
              "Energie réduite d'attraction"]

    crv = int(input("Choix du graph:\n\n"
                    "1: Potentiel de Lennard Jones\n"
                    "2: Force d'interaction entre molécules\n\n"
                    "1 ou 2: "))

    potential_data = Function(crv)

    if crv == 1:
        potential_curve = Curve(labels, "Potentiel de Lennard Jones")
        potential_curve.set_lim(0.5, 2.5, -1.5, 1.5)
    else:
        potential_curve = Curve(labels, "Force d'interaction entre molécules")
        potential_curve.set_lim(0.5, 2.5, -6, 6)

    potential_curve.color_zone(crv)

    x, y1, y2, y3 = potential_data.get_data()
    potential_curve.plot_data(x, y1, y2, y3)
