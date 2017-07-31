# python3

import sys


def get_max_pairwise_product(vector):
    first_max = second_max = -sys.maxsize
    for e in vector:
        if e > first_max:
            second_max = first_max
            first_max = e
		elif e > second_max:
			second_max = e

    return first_max * second_max

l = int(input())
vector = map(lambda s: int(s), input().split(' ')[:l])
print(get_max_pairwise_product(vector))
