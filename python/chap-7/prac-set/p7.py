n = 3

for i in range(1, n + 1):
    starCount = " "
    space = " "
    for star in range(0, 2 * i - 1, 1):
        starCount += "*"
    space = " " * (n - i)
    print(space, starCount)


