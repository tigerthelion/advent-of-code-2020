"""
Part 1
For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

Part 2
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. 
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""
import re

count = 0
with open("inputs/02.txt") as f:
    # read in and parse data
    passwords = []
    data = f.readlines()
    for line in data:
        # 0 is low, 1 is high, 2 is letter, 3 is password
        res = re.split(r"(^[0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", line)
        passwords.append(res[1:-1])


# Part 1
for p in passwords:
    p_len = len(p[3])
    c = 0  # character count
    i = 0  # iteration count
    while(i < p_len):
        # if there arent enough letters to make up the difference, quit #TODO
        remaining = p_len - i
        if int(p[0]) - c > remaining:
            break

        if p[3][i] == p[2]:
            c += 1
        i += 1
    if c in range(int(p[0]), int(p[1])+1):
        count += 1

print(count)

# Part 2
count = 0
for p in passwords:
    char = p[2]
    pos1 = p[3][int(p[0]) - 1]
    pos2 = p[3][int(p[1]) - 1]

    if not pos1 == pos2 and (char == pos1 or char == pos2):
        count += 1


print(count)
