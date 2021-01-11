"""
https://adventofcode.com/2020/day/3
"""

with open("inputs/03.txt") as f:
    # read in and parse data
    hill = []
    data = f.readlines()
    for line in data:
        lsplt = line.split()
        hill.append(lsplt[0])



runs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def calc_trees(hill, run: tuple):
    
    rowx = len(hill) # Max num of rows
    colx = len(hill[0]) - 1 # Max num of columns

    col, row = run 

    rowi, coli = 0, 0

    treect = 0

    while rowi < rowx:
        if hill[rowi][coli] == '#':
            treect += 1

        if coli > colx - col:
            coli = coli - colx - 1

        coli += col

        rowi += row

    print(run, treect)
    return treect


ans = 0
for run in runs:
    if ans == 0:
        ans = calc_trees(hill, run)
    else:
        ans *= calc_trees(hill, run)
print(ans)