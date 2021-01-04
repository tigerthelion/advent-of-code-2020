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


def run_part_one(data):
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

"""
Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

"""
def binary_search(data, a):
    l = 0
    h = len(data) - 1
    m = h // 2
    while h >= l:
        d = data[m]
        if d == a:
            return d
        elif d > a: 
            h = m -1
        else:
            l = m + 1
        m = (l + h) // 2
    return None
             



def run_part_two(data):
    for i in range(len(data) - 1):
        for j in range(i, len(data) - 1):
            sum = data[i]+data[j]
            a = 2020 - sum
            if a > 0:
                # This is sloppy.. I could tighten this up #TODO
                ans = binary_search(data, a)
                if not ans:
                    continue
                
                if ans + sum == 2020:
                    print(data[i], data[j], ans)
                    print(data[i] * data[j] * ans)
                    return
               


run_part_two(data)