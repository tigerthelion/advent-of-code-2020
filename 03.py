"""

https://adventofcode.com/2020/day/3

"""
with open("inputs/03.txt") as f:
    # read in and parse data
    map = []
    data = f.readlines()
    for line in data:
        lsplt = line.split()
        map.append(lsplt[0])

rows = len(map)
col = 3
colmax = len(map[0]) - 1
rowi = 0
seek = 0
trees = 0
while rowi < rows:
    if map[rowi][seek] == '#':
        trees += 1

    if seek > colmax - col:
        seek = seek - colmax - 1

    seek += col

    rowi += 1
print(trees)
