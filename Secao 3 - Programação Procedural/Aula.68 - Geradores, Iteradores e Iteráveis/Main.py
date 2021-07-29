import sys
import time

l1 = [x for x in range(0, 10000, 50)]
l2 = (x for x in range(0, 10000, 50))

print('l1 -->', type(l1))
print('l2 -->', type(l2))
print()

print('l1 -->', sys.getsizeof(l1), 'Bytes')
print('l2 -->', sys.getsizeof(l2), 'Bytes')

print('\n',l1)
