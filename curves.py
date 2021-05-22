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


def neon_curve(x, y1, y2=None, y3=None, y4=None, y5=None, y6=None, v=None):
    n_lines = 10
    diff_linewidth = 1.05
    alpha_value = 0.03

    for n in range(1, n_lines + 1):
        plt.plot(x, y1,
                 linewidth=2 + (diff_linewidth * n),
                 alpha=alpha_value,
                 color='#08F7FE')

        # if Van Der Waals curve
        if y4 is not None:
            plt.plot(v, y4,
                     linewidth=2 + (diff_linewidth * n),
                     alpha=alpha_value,
                     color='#08F7FE')

        if y5 and y6 is not None:

            plt.plot(v, y5,
                     linewidth=2 + (diff_linewidth * n),
                     alpha=alpha_value,
                     color='#00ff41', )

            plt.plot(v, y6,
                     linewidth=2 + (diff_linewidth * n),
                     alpha=alpha_value,
                     color='#FE53BB')

        elif y2:
            plt.plot(x, y2,
                     linewidth=2 + (diff_linewidth * n),
                     alpha=alpha_value,
                     color='#00ff41', )

            plt.plot(x, y3,
                     linewidth=2 + (diff_linewidth * n),
                     alpha=alpha_value,
                     color='#FE53BB')


def neon_curve_VDW(vdw_neg, vdw_pos1, vdw_pos2, vdw_pos3, y1, y2, y3, y4):
    n_lines = 10
    diff_linewidth = 1.05
    alpha_value = 0.03

    for n in range(1, n_lines + 1):
        plt.plot(vdw_neg, y1,
                 linewidth=2 + (diff_linewidth * n),
                 alpha=alpha_value,
                 color='#08F7FE')

        plt.plot(vdw_pos1, y2,
                 linewidth=2 + (diff_linewidth * n),
                 alpha=alpha_value,
                 color='#00ff41')

        plt.plot(vdw_pos2, y3,
                 linewidth=2 + (diff_linewidth * n),
                 alpha=alpha_value,
                 color='#FE53BB')

        plt.plot(vdw_pos3, y4,
                 linewidth=2 + (diff_linewidth * n),
                 alpha=alpha_value,
                 color='#08F7FE')

        plt.vlines(0, -15, 15,
                   linewidth=2 + (diff_linewidth * n),
                   alpha=alpha_value,
                   color='#0019FF')


class Curve:

    def __init__(self, labels, title, xlabel, ylabel):
        self.labels = labels
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        plt.rcParams["text.usetex"] = True
        dark_style()

    def plot_data(self, x, y1, y2=None, y3=None, y4=None, y5=None, y6=None, v_neg=None):
        plt.plot(x, y1, label=self.labels[0], color='#08F7FE')

        if y2 is None:
            plt.plot(x, y1, label=self.labels[0], color='#08F7FE')

        if y2:
            plt.plot(x, y2, label=self.labels[1], color='#00ff41')
            plt.plot(x, y3, label=self.labels[2], color='#FE53BB')

        if y4 and y5 and y6 is not None:
            plt.plot(v_neg, y4, color='#08F7FE')
            plt.plot(v_neg, y5, color='#00ff41')
            plt.plot(v_neg, y6, color='#FE53BB')

        plt.legend(facecolor="black", frameon=True, loc="top")

        plt.title(self.title, y=-0.14, fontsize=15, style="italic")
        plt.xlabel(self.xlabel, loc='right', fontsize=15)
        plt.ylabel(self.ylabel, loc='top', fontsize=15)
        neon_curve(x, y1, y2, y3)

        plt.grid(which='both', b=True, color="0.5")

        plt.grid(which='minor', b=True, color="0.2", alpha=0.5)

        plt.show()

    def plot_data_vdw(self, vdw_neg, vdw_pos1, vdw_pos2, vdw_pos3, y1, y2, y3, y4):

        plt.plot(vdw_neg, y1, label=self.labels[0], color='#08F7FE')
        plt.vlines(0, -15, 15, label=self.labels[1], color='#0019FF')  # asymptote (x=zero)
        plt.plot(vdw_pos1, y2, label=self.labels[2],  color='#00ff41')
        plt.plot(vdw_pos2, y3,  color='#FE53BB')
        plt.plot(vdw_pos3, y4, color='#08F7FE')

        plt.legend(facecolor="black", frameon=True)

        plt.title(self.title, y=-0.14, fontsize=15, style="italic")
        plt.xlabel(self.xlabel, loc='right', fontsize=15)
        plt.ylabel(self.ylabel, loc='top', fontsize=15)

        neon_curve_VDW(vdw_neg, vdw_pos1, vdw_pos2, vdw_pos3, y1, y2, y3, y4)

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
            plt.axvspan(0.5, 1.1, facecolor='#980D8E', alpha=0.15)
        elif crv == 3:
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
            x_step = 0.05
        elif y_max == 15:
            y_step = 1
            x_step = 1
        else:
            x_step = 0.1
            y_step = 0.1

        if y_max != 4000:
            grid_x_ticks = np.arange(x_min, x_max, x_step)
            grid_y_ticks = np.arange(y_min, y_max, y_step)

            plt.gca().set_xticks(grid_x_ticks, minor=True)
            plt.gca().set_yticks(grid_y_ticks, minor=True)
