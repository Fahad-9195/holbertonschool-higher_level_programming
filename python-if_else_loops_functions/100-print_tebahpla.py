#!/usr/bin/python3

for i in range(122, 96, -1):  # من z=122 إلى a=97
    if (122 - i) % 2 == 0:    # ترتيب: حرف صغير → كبير → صغير → كبير...
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i - 32), end="")
