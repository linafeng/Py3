# -*- coding:utf-8 -*-
i = 1
while i < 10:
    print("循环")
    i += 1
count = 0
list1 = [1, 2, 3, 4, 5, 6]
for i in list1:
    count = count + i
print(count)

# break
count = 0
for i in list1:
    if i == 5:
        break
    count = count + i
print(count)

# continue
count = 0
for i in list1:
    if i == 5:
        continue
    count = count + i
print(count)
