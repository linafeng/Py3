# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='SimHei', size=13)

num = np.array([13325, 9403, 9227, 8651])
ratio = np.array([0.75, 0.76, 0.72, 0.75])
men = num * ratio
women = num * (1 - ratio)
x = ['聊天', '支付', '团购\n优惠券', '在线视频']

width = 0.5
idx = np.arange(len(x))
plt.bar(idx, men, width, color='red', label='男性用户')
plt.bar(idx, women, width, bottom=men, color='yellow', label='女性用户')  # 这一块可是设置bottom,top，如果是水平放置的，可以设置right或者left。
plt.xlabel('应用类别')
plt.ylabel('男女分布')
plt.xticks(idx + width / 2, x, rotation=40)

# bar图上显示数字

for a, b in zip(idx, men):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=12)
for a, b, c in zip(idx, women, men):
    plt.text(a, b + c + 0.5, '%.0f' % b, ha='center', va='bottom', fontsize=12)

plt.legend()
plt.show()
