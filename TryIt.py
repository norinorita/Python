squares = [x ** 2 for x in range(1, 11)]
print filter(lambda x: x in range(30, 71), squares)
