import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
line = ''

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

for i in range(n):
    matrix[i] = [char for char in matrix[i]]

for column in range(m):
    for row in range(n):
        line += matrix[row][column]

res = re.sub('(?<=a-zA-Z0-9)^a-zA-Z0-9+(?=a-zA-Z0-9)', '00', line)

print(res)
