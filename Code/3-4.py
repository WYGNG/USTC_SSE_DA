# 代码3-4 不同菜品在某段时间的销售量的分布情况
import pandas as pd
import matplotlib.pyplot as plt
catering_dish_profit = './catering_dish_profit.xls'  # 餐饮数据
data = pd.read_excel(catering_dish_profit)  # 读取数据，指定“日期”列为索引

# 绘制饼图
x = data['盈利']
labels = data['菜品名']
plt.figure(figsize=(8, 6))  # 设置画布大小
plt.pie(x, labels=labels)  # 绘制饼图
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.title('菜品销售量分布（饼图）')  # 设置标题
plt.axis('equal')
plt.show()

# 绘制条形图
x = data['菜品名']
y = data['盈利']
plt.figure(figsize=(8, 4))  # 设置画布大小
plt.bar(x, y)
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.xlabel('菜品')  # 设置x轴标题
plt.ylabel('销量')  # 设置y轴标题
plt.title('菜品销售量分布（条形图）')  # 设置标题
plt.show()  # 展示图片
