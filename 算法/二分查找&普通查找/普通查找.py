import random
import time

# 获取1000个范围从1-10000的随机数据,生成列表
num_list = []
for i in range(1000):
    ran_num = random.randint(1, 10000)
    num_list.append(ran_num)
li = sorted(num_list)


def normal_search(list, item):
    i = 0
    while True:
        if list[i] == item:
            return 'find it'
        elif list[i] != item:
            i += 1
        if i == 999:
            break
    return 'no such item'


# 测试运行时长
start_time = time.time()
res = normal_search(li, 666)
end_time = time.time()
my_time = end_time - start_time

print(res, my_time)
