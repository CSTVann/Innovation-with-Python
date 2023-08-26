num_inputs = 1
for i in range(num_inputs):
    n = int(input(f"Enter the value of n for input : "))
    checkerboard = [[(i + j) % 2 for j in range(n)] for i in range(n)]
    print(f"Checkerboard pattern for n = {n}:")
    for row in checkerboard:
        print(*row)
    print()
    break