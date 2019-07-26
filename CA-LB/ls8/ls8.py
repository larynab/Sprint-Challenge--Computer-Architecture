#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()
cpu.load()
cpu.run()

#OLD CODE-----------------------------------------------------------------------------------
# print(sys.argv)
# print(len(sys.argv))
# with open(sys.argv[1], 'r') as my_file:
#     print(my_file.read())

# if len(sys.argv) != 2:
#     print(f"usage: {sys.argv[0]}")
#     sys.exit(1)

# try:
#     with open(sys.argv[1]) as my_file:
#         for line in my_file:
#             num = line.split("#", 1)[0]
#             if num.strip() == '':
#                 continue
#             print(int(num))

# except FileNotFoundError:
#     print(f"{sys.argv[0]}: {sys.argv[1]} not found")
#     sys.exit(2)

#main take in arguments, using load method the arg at 1.
