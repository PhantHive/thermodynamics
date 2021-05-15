import json

import numpy as np


class Function:

    def __init__(self, crv=1, gas=None):
        self.gas = gas
        self.alpha = self.beta = 1
        self.crv = crv
        self.R = 8.3145  # Universal gas constant
        self.x = [p / 100.0 for p in range(50, 251, 1)]
        self.v = [v for v in np.arange(-10, 11, 10 ** -5)]
        self.y1 = []
        self.y2 = []
        self.y3 = []
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
        return -12 * self.beta / r ** 7

    def der_rep(self, r):
        return +12 * self.alpha / r ** 13

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
        return self.R * T / (V - b) - a / V ** 2

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
            '''with open('gas.json', 'r') as gas_info:
                data = json.load(gas_info)

            if self.gas is None:
                self.gas = "He"

            a = data[self.gas]["a"]
            b = data[self.gas]["b"]
            '''

            self.y1 = []
            self.y2 = []
            self.y3 = []

            for j in range(len(self.v)):
                p1 = self.ideal_gas(self.v[j], 300)
                p2 = self.ideal_gas(self.v[j], 400)
                p3 = self.ideal_gas(self.v[j], 500)

                self.y1.append(p1)
                self.y2.append(p2)
                self.y3.append(p3)

    def get_data(self):
        return self.v, self.x, self.y1, self.y2, self.y3
