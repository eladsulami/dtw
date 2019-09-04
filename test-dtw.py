import numpy as np
from math import inf
from optparse import OptionParser
import matplotlib.pyplot as plt


def distance_inf(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def get_sums(c_xs, c_ys, x, y, rev):
    res = []
    c_sum = 0
    index_range = range(len(c_xs))
    index_range = reversed(index_range) if rev else index_range
    for p in index_range:
        dist = distance_inf((c_xs[p], c_ys[p]), (x, y))
        c_sum += dist
        if rev:
            res.insert(0, c_sum)
        else:
            res.append(c_sum)

    return res


def draw(c_xs, c_ys, s_xs, s_ys, min_index, points):
    plt.plot(c_xs, c_ys, 'ro-')
    plt.plot(s_xs, s_ys, 'bo-')
    for p in range(points):
        if p <= min_index:
            plt.plot([c_xs[p], s_xs[0]], [c_ys[p], s_ys[0]], 'yo-')
        if p > min_index:
            plt.plot([c_xs[p], s_xs[1]], [c_ys[p], s_ys[1]], 'yo-')

    plt.plot(c_xs[0], c_ys[0], 'g*')
    plt.plot(s_xs[0], s_ys[0], 'g*')
    plt.show()


def main(points):
    # for i in range(runs):
    print("-------------------------------------")
    c_xs, c_ys = np.random.randint(low=0, high=20, size=(2, points))

    s_xs, s_ys = np.random.randint(low=0, high=20, size=(2, 2))

    point1_arr = get_sums(c_xs, c_ys, s_xs[0], s_ys[0], False)
    point2_arr = get_sums(c_xs, c_ys, s_xs[1], s_ys[1], True)

    min_index = get_min(point1_arr, point2_arr, points)

    print(c_xs, c_ys, s_xs, s_ys, point1_arr, point2_arr, min_index)

    draw(c_xs, c_ys, s_xs, s_ys, min_index, points)


def get_min(point1_arr, point2_arr, points):
    min_index = -1
    min_val = inf
    for p in range(points - 1):
        if point1_arr[p] + point2_arr[p + 1] < min_val:
            min_val = point1_arr[p] + point2_arr[p + 1]
            min_index = p

    return min_index


if __name__ == "__main__":
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("--points", "-p", dest="points", type="int", action="store", help="Number of points for each run",
                      default=5)
    opt, args = parser.parse_args()
    main(opt.points)
