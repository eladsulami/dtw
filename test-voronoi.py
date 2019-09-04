import numpy as np
from math import inf
from optparse import OptionParser
import matplotlib.pyplot as plt


def distance(a, b):
    return abs(a - b)


def get_sums(line, x, rev):
    res = []
    c_sum = 0
    index_range = range(len(line))
    index_range = reversed(index_range) if rev else index_range
    for p in index_range:
        dist = distance(line[p], x)
        c_sum += dist
        if rev:
            res.insert(0, c_sum)
        else:
            res.append(c_sum)

    return res


def draw(s_xs, s_ys, colors):
    # for p in range(test_points):

    plt.scatter(s_xs, s_ys, c=colors, s=np.ones(len(s_xs)))

    plt.show()


def main(line_points, test_points, line_high):
    # for i in range(runs):
    while True:
        print("-------------------------------------")
        c_line = np.random.randint(low=0, high=line_high, size=(1, line_points))
        colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'orange', 'SkyBlue', 'LightSkyBlue', 'DarkMagenta', 'Turquoise', 'OrangeRed', 'PowderBlue', 'SeaGreen', 'PapayaWhip', 'Red', 'DarkSeaGreen', 'Orange', 'NavajoWhite', 'LightGoldenRodYellow', 'CornflowerBlue', 'LightYellow', 'Azure', 'DarkBlue', 'Plum', 'DarkSlateGrey', 'Black', 'LightGreen', 'Cornsilk', 'WhiteSmoke', 'MistyRose', 'LightGrey', 'Gainsboro', 'DarkViolet', 'YellowGreen', 'Chartreuse', 'Blue', 'DarkSlateBlue', 'Moccasin', 'DarkSalmon', 'Maroon', 'LightGray', 'Peru', 'LightBlue', 'SlateGray', 'DeepSkyBlue', 'DodgerBlue', 'DarkGray', 'LemonChiffon', 'RosyBrown', 'Cyan', 'SaddleBrown', 'MediumTurquoise', 'DarkRed', 'PaleTurquoise', 'MediumVioletRed', 'MediumSlateBlue', 'Crimson', 'Teal', 'Indigo', 'Coral', 'HoneyDew', 'BlanchedAlmond', 'Purple', 'Sienna', 'DarkOliveGreen', 'DarkOrange', 'Chocolate', 'LawnGreen', 'DarkGreen', 'MintCream', 'DarkSlateGray', 'PaleGoldenRod', 'PaleVioletRed', 'GhostWhite', 'SandyBrown', 'LightCoral', 'LightSteelBlue', 'DimGray', 'Navy', 'Lavender', 'SteelBlue', 'RebeccaPurple', 'Fuchsia', 'IndianRed', 'Aqua', 'DarkCyan', 'DarkKhaki', 'DarkTurquoise', 'LightSlateGrey', 'Grey', 'AliceBlue', 'Aquamarine', 'Salmon', 'MediumBlue', 'LightPink', 'Tan', 'LightCyan', 'BlueViolet', 'Thistle', 'Green', 'Violet', 'HotPink', 'MediumSpringGreen', 'PeachPuff', 'BurlyWood', 'DeepPink', 'MidnightBlue', 'Linen', 'Gray', 'Brown', 'Snow', 'SlateBlue', 'OliveDrab', 'GreenYellow', 'MediumSeaGreen', 'Silver', 'LavenderBlush', 'Bisque', 'LightSlateGray', 'Beige', 'White', 'DarkGrey', 'Lime', 'Orchid', 'ForestGreen', 'CadetBlue', 'SpringGreen', 'AntiqueWhite', 'PaleGreen', 'SlateGrey', 'OldLace', 'SeaShell', 'DimGrey', 'Gold', 'Wheat', 'DarkOrchid', 'LightSalmon', 'Magenta', 'RoyalBlue', 'DarkGoldenRod', 'MediumOrchid', 'MediumPurple', 'FloralWhite', 'LimeGreen', 'Khaki', 'GoldenRod', 'Ivory', 'Pink', 'FireBrick', 'Olive', 'Yellow', 'Tomato', 'LightSeaGreen', 'MediumAquaMarine']

        s_xs, s_ys = np.random.randint(low=0, high=line_high*1.5, size=(2, test_points))
        # s_xs = np.random.random(test_points) * (line_high * 1.5)
        # s_ys = np.random.random(test_points) * (line_high * 1.5)
        res = []
        for i in range(test_points):
            point1_arr = get_sums(c_line[0], s_xs[i], False)
            point2_arr = get_sums(c_line[0], s_ys[i], True)
            k, val = get_min(point1_arr, point2_arr, line_points)
            res.append(colors[k])

        print(c_line, get_functions(c_line[0]))

        draw(s_xs, s_ys, res)

        print(s_xs, s_ys)
        break


def get_min(point1_arr, point2_arr, points):
    min_index = -1
    min_val = inf
    for p in range(points - 1):
        if point1_arr[p] + point2_arr[p + 1] < min_val:
            min_val = point1_arr[p] + point2_arr[p + 1]
            min_index = p

    return min_index, min_val


def get_functions(line):
    res = ["y = x"]
    a = line[1] * 2
    res.append("y = -x + " + str(a))
    for i in range(1, len(line) - 2):
        a += (line[i + 1] - line[i]) * 2
        res.append("y = -x + " + str(a))

    return res


if __name__ == "__main__":
    c_line = [80, 73, 23, 87, 54, 18, 84, 93,  7]

    point1_arr1 = get_sums(c_line, 30.5848941, False)
    point2_arr1 = get_sums(c_line, 90.95, True)
    k1, val1 = get_min(point1_arr1, point2_arr1, len(c_line))

    point1_arr2 = get_sums(c_line, 84.09, False)
    point2_arr2 = get_sums(c_line, 91.03, True)
    k2, val2 = get_min(point1_arr2, point2_arr2, len(c_line))

    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("--test-points", "-p", dest="test_points", type="int", action="store",
                      help="Number of points for each run",
                      default=300000)
    parser.add_option("--line-points", "-l", dest="line_points", type="int", action="store",
                      help="Number of points for each run",
                      default=9)
    parser.add_option("--line-high", "-b", dest="line_high", type="int", action="store",
                      help="Number of points for each run",
                      default=100)
    opt, args = parser.parse_args()
    main(opt.line_points, opt.test_points, opt.line_high)
