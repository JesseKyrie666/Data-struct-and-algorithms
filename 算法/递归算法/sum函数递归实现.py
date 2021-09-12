import random
test_arr = []

for i in range(10):
    ran_num = random.randint(1, 10000)
    test_arr.append(ran_num)
print(test_arr)

def mysum(arr):
    res = 0
    if not arr:
        return 0
    else:
        # 取出索引为第一个的数据，
        res =arr[0]+mysum(arr[1:])
    return res
res = mysum(test_arr)
print(res)

