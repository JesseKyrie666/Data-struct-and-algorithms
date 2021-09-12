import random
import time

# 获取1000个范围从1-10000的随机数据,生成列表
num_list = []
for i in range(1000):
    ran_num = random.randint(1, 10000)
    num_list.append(ran_num)
li = sorted(num_list)

# 二分查找算法
def binary_search(list,item):
    # 获取索引
    low = 0
    high = len(list)-1

    while low <=high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return "find it!"
        if guess > item:
            high = mid-1
        else:
            low = mid +1
    return 'no such item'

# 测试运行时长
start_time = time.time()
res = binary_search(li,666)
end_time = time.time()
my_time = end_time-start_time

print(res,my_time)





