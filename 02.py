"""
For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

"""
import re

count = 0
with open("inputs/02.txt") as f:
    data = f.readlines()
    for line in data:
        res = re.split(r"(^[0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", line)
        print(res)
        # 1 is low, 2 is high, 3 is letter, 4 is password
        p_len = len(res[4])
        c = 0  # character count
        i = 0  # iteration count
        while(i < p_len):
            # if there arent enough letters to make up the difference, quit #TODO
            # if int(res[1]) - c > (p_len - i - 1) or int(res[2]) - c > (p_len - i - 1)  :
            #     break

            if res[4][i] == res[3]:
                c += 1
            i += 1
        if c in range(int(res[1]), int(res[2])+1):
            count += 1
    print(count)
