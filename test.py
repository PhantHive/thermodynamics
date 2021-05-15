import json
import matplotlib.pyplot as plt
import numpy as np

R = 8.3145
with open('gas.json', 'r') as gas_info:
    data = json.load(gas_info)

a = data["CO2"]["a"]
b = data["CO2"]["b"]


def van_der_waals(V, T):
    '''
    :param a: constant depending of the gas (bar L^2 mol^-2)
    :param b: constant depending of the gas (L mol^-1)
    :param T: temperature, must be constant
    :param V: Volume
    :return: P , pression (Pa)
    '''
    if V == 0:
        V = b
    return R * T / (V - b) - a / V ** 2


def ideal_gas(V, T):
    if V == 0:
        V = b
    return R * T / V


def clausius(V, T):
    return R * T / (V - b)


for t in np.arange(300, 501, 100):
    vval = []
    pval = []
    for v in np.arange(-10, 11, 10**-5):
        p = ideal_gas(v, t)
        vval.append(v)
        pval.append(p)

    plt.plot(vval, pval, label='$T=$' + str(t))

plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.ylim(-4000, 4000)
plt.legend()
plt.show()
