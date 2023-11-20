import numpy as np
import matplotlib.pyplot as plt


def chain_ploting(d: int, N: int):
    x = np.zeros(N)
    y = np.zeros(N)
    z = np.zeros(N)
    for i in range(1, N):
        label = True
        while label:
            label = False
            xt, yt, zt = random_vector(d)

            x[i] = x[i - 1] + xt
            z[i] = z[i - 1] + zt
            y[i] = y[i - 1] + yt

            for j in range(i):
                distance = (
                    (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2
                ) ** (1 / 2)
                if distance < d:
                    label = True
                    break
    return x, y, z


def random_vector(d):
    x = 1 - 2 * np.random.random()
    y = 1 - 2 * np.random.random()
    z = 1 - 2 * np.random.random()
    s = (x**2 + y**2 + z**2) ** (1 / 2)
    return x / s * d, y / s * d, z / s * d


if __name__ == "__main__":
    x, y, z = chain_ploting(1, 100)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(x, y, z, "-o")
    plt.show()
