#!/usr/bin/env python3

# Author: Kang Kang
# Auther ID: kang-kang
# Date Created: 2025/05/11

import sys


if len(sys.argv) == 2:
    timer = int(sys.argv[1])
    while timer != 0:
        print(timer)
        timer = timer - 1
else:
    timer = 3
    while timer != 0:
        print(timer)
        timer = timer - 1

print("blast off!")
