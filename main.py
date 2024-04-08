# Get Enum name by value in Python

from enum import Enum

class Sizes(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


print(Sizes(1).name)  # 👉️ SMALL
print(Sizes(2).name)  # 👉️ MEDIUM
print(Sizes(3).name)  # 👉️ LARGE
