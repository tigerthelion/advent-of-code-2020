"""
Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

"""

from helper import load_data

data = load_data("01.txt")
data.sort()


def run(data):
    for i in range(len(data)):
        for j in range(len(data)-1,0,-1):
            sum = data[i]+data[j]
            if sum > 2020:
                j -=1
            elif sum < 2020:
                i += 1
            else:
                print(data[i], data[j] , data[i] * data[j])
                return

run(data)