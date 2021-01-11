"""

https://adventofcode.com/2020/day/3

"""
with open("inputs/03.txt") as f:
    # read in and parse data
    map = ""

    data = f.readlines()
    cols = len(data[0].split()[0])
    rows = 0
    for line in data:
        lsplt = line.split()

        map += lsplt[0]
        rows += 1
print(map)
print(rows)
print(cols)

register = []
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for i in slopes:

    # rows = len(map)
    # col = 3
    # colmax = len(map[0]) - 1
    # rowi = 0
    # seek = 0
    # trees = 0
    # while rowi < rows:
    #     if map[rowi][seek] == '#':
    #         trees += 1

    #     if seek > colmax - col:
    #         seek = seek - colmax - 1

    #     seek += col

    #     rowi += row_seek
    # print(trees)

    # [1,1], [1,2], [1,4], [1, 6], [2, 1]
    # [2,2], [2,5], [2,9], [2, 13], [4, 2]


def calc_trees(hill, slope: tuple):
    rows = len(map)
    col, row = slope
