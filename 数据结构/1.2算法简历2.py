for n1 in range(0, 1001):
    for n2 in range(0, 1001):
        n3 = 1000 - n1 - n2
        if n1 ** 2 + n2 ** 2 == n3 ** 2:
            print('[%d,%d,%d]' % (n1, n2, n3))
'''运行时间变短了'''

