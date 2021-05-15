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

    def __init__(self, labels, title, xlabel, ylabel):
        self.labels = labels
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        plt.rcParams["text.usetex"] = True
        dark_style()

    def plot_data(self, x, y1, y2, y3):
        plt.plot(x, y1, label=self.labels[0], color='#08F7FE')
        plt.plot(x, y2, label=self.labels[1], color='#00ff41')
        plt.plot(x, y3, label=self.labels[2], color='#FE53BB')
        plt.legend(facecolor="black", frameon=True)

        plt.title(self.title, y=-0.14, fontsize=15, style="italic")
        plt.xlabel(self.xlabel, loc='right', fontsize=15)
        plt.ylabel(self.ylabel, loc='top', fontsize=15)
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
        elif crv == 2:
            plt.axvspan(0.5, 1, facecolor='#980D8E', alpha=0.15)
        else:
            plt.axvspan(-10, 0, 0.5, 1, facecolor='#987162', alpha=0.15)
            plt.axvspan(0, 10, 0, 0.5, facecolor='#987162', alpha=0.15, label='Partie non réelle')

    @staticmethod
    def set_lim(x_min, x_max, y_min, y_max, centrage=None):
        plt.xlim((x_min, x_max))
        plt.ylim((y_min, y_max))
        # plt.xticks([0.5, 1, 1.5, 2, 2.5])
        plt.gca().spines['bottom'].set_position(('data', 0))
        if centrage:
            plt.gca().spines['left'].set_position(('data', 0))

        if y_max == 6:
            y_step = 0.4
            x_step = 0.1

        else:
            x_step = 0.1
            y_step = 0.1

        if y_max != 4000:
            grid_x_ticks = np.arange(x_min, x_max, x_step)
            grid_y_ticks = np.arange(y_min, y_max, y_step)

            plt.gca().set_xticks(grid_x_ticks, minor=True)
            plt.gca().set_yticks(grid_y_ticks, minor=True)
