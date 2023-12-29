import math as m
import re

with open('input3.txt', 'r') as file:
    board = list(file)

chars = {}
for r in range(140):
    for c in range(140):
        if board[r][c] not in '01234566789.':
            chars[(r, c)] = []

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1) for c in range(n.start()-1, n.end()+1)}
        for o in edge & chars.keys():
            print(o)
            chars[o].append(int(n.group()))

sum_of_all_numbers = sum(sum(p) for p in chars.values())
sum_of_products_of_pairs = sum(m.prod(p) for p in chars.values() if len(p) == 2)

print(sum_of_all_numbers, sum_of_products_of_pairs)