import json
import matplotlib.pyplot as plt
import numpy as np

R = 8.3145
with open('gas.json', 'r') as gas_info:
    data = json.load(gas_info)

a = 1
b = 4


v = [v for v in np.arange(-15, 15, 0.01)]

def van_der_waals(V, K):
    '''
    :param a: constant depending of the gas (bar L^2 mol^-2)
    :param b: constant depending of the gas (L mol^-1)
    :param T: temperature, must be constant
    :param V: Volume
    :return: P , pression (Pa)
    '''

    return (K / (V - b)) - (a / V ** 2)


def ideal_gas(V, T):
    if V == 0:
        V = b
    return R * T / V


def clausius(V, T):
    return R * T / (V - b)

y1 = []
for j in range(len(v)):
    res = van_der_waals(v[j], 5)
    y1.append(res)

plt.plot(v, y1)

plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.ylim(-15, 15)
plt.legend()
plt.show()
