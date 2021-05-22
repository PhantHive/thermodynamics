import json

import numpy as np


class Function:

    def __init__(self, crv=1, gas=None):
        self.gas = gas
        self.alpha = self.beta = 1
        self.crv = crv
        self.R = 8.3145  # Universal gas constant
        self.x = [p / 100.0 for p in range(50, 251, 1)]
        self.v_neg = [v for v in np.arange(-10, 0, 10 ** -5)]
        self.v_pos = [-x for x in self.v_neg]
        # x < 0
        self.vdw_neg = [v for v in np.arange(-15, - 0.29, 0.01)]
        # x > 0
        self.vdw_pos1 = [v for v in np.arange(0.1, 3.55, 0.1)]
        self.vdw_pos2 = [v for v in np.arange(3.99, 4.01, 0.001)]
        self.vdw_pos3 = [v for v in np.arange(4.15, 15, 0.1)]

        self.y1 = []
        self.y2 = []
        self.y3 = []
        self.y4 = []
        self.y5 = []
        self.y6 = []
        self.set_data()

    # first graph
    def E_attr(self, r):
        return -2 * self.beta / r ** 6

    def E_rep(self, r):
        return self.alpha / r ** 12

    def E_inter(self, r):
        return self.E_rep(r) + self.E_attr(r)

    # second graph
    def der_attr(self, r):
        return +12 * self.beta / r ** 7

    def der_rep(self, r):
        return -12 * self.alpha / r ** 13

    def t_force(self, r):
        return self.der_rep(r) + self.der_attr(r)

    # thrid graph
    def van_der_waals(self, a, b, V, T):
        '''
        :param a: constant depending of the gas (bar L^2 mol^-2)
        :param b: constant depending of the gas (L mol^-1)
        :param T: temperature, must be constant
        :param V: Volume
        :return: P , pression (Pa)
        '''
        return (self.R * T / (V - b)) - (a / V ** 2)

    def ideal_gas(self, V, T):
        return self.R * T / V

    def clausius(self, V, T, b):
        return self.R * T / (V - b)

    def set_data(self):

        if self.crv == 1:
            for j in range(len(self.x)):
                y_res1 = self.E_rep(self.x[j])
                y_res2 = self.E_attr(self.x[j])
                y_res3 = self.E_inter(self.x[j])
                self.y1.append(y_res1)
                self.y2.append(y_res2)
                self.y3.append(y_res3)

        if self.crv == 2:
            for j in range(len(self.x)):
                y_res1 = self.der_rep(self.x[j])
                y_res2 = self.der_attr(self.x[j])
                y_res3 = self.t_force(self.x[j])
                self.y1.append(y_res1)
                self.y2.append(y_res2)
                self.y3.append(y_res3)

        if self.crv == 3:

            for j in range(len(self.v_pos)):
                p1 = self.ideal_gas(self.v_pos[j], 300)
                p2 = self.ideal_gas(self.v_pos[j], 400)
                p3 = self.ideal_gas(self.v_pos[j], 500)

                p4 = self.ideal_gas(self.v_neg[j], 300)
                p5 = self.ideal_gas(self.v_neg[j], 400)
                p6 = self.ideal_gas(self.v_neg[j], 500)

                self.y1.append(p1)
                self.y2.append(p2)
                self.y3.append(p3)

                self.y4.append(p4)
                self.y5.append(p5)
                self.y6.append(p6)

        if self.crv == 4:

            with open('gas.json', 'r') as gas_info:
                data = json.load(gas_info)
            K = 5
            T = K / self.R
            if self.gas is None:
                a = 1
                b = 4
            else:
                a = data[self.gas]["a"]
                b = data[self.gas]["b"]

            print(a, b)

            for j in range(len(self.vdw_neg)):
                p1 = self.van_der_waals(a, b, self.vdw_neg[j], T)
                self.y1.append(p1)
            for x in range(len(self.vdw_pos1)):
                p1 = self.van_der_waals(a, b, self.vdw_pos1[x], T)
                self.y2.append(p1)
            for y in range(len(self.vdw_pos2)):
                p1 = self.van_der_waals(a, b, self.vdw_pos2[y], T)
                self.y3.append(p1)
            for z in range(len(self.vdw_pos3)):
                p1 = self.van_der_waals(a, b, self.vdw_pos3[z], T)
                self.y4.append(p1)

    def get_data(self):
        return self.x, self.y1, self.y2, self.y3

    def get_data_IG(self):
        return self.v_pos, self.v_neg, self.y1, self.y2, self.y3, self.y4, self.y5, self.y6

    def get_data_VDW(self):
        return self.vdw_neg, self.vdw_pos1, self.vdw_pos2, self.vdw_pos3, \
               self.y1, self.y2, self.y3, self.y4
