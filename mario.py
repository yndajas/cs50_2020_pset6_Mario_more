from cs50 import get_int

height = 0

# get height until it's within range 1-8
while height not in range(1, 9):
    height = get_int("Height: ")

# for loop starting at one and going until height
for row in range(1, height + 1):
    # print left spaces + left hashes + gap + right hashes
    print(" " * (height - row) + "#" * row + "  " + "#" * row)