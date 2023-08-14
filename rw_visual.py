import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:

    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    point_number = list(range(rw.num_points))
    rw.fill_walk()
    # 绘制窗口大小
    plt.figure(dpi=128, figsize=(10, 6))
    '''
    # 隐藏坐标轴,要先放给plt.axes赋值变量
    current_axes = plt.axes()
    current_axes.get_xaxis().set_visible(False)
    current_axes.get_yaxis().set_visible(False)
    '''
    '''使用scatter散点的形式绘图
    # 渐变色的原理为c表示的列表为从绘制的第一个点开始按顺序每个点的颜色层级
    plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, edgecolors='none', s=10)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    '''
    plt.plot(rw.x_values, rw.y_values, linewidth=5)
    plt.show()
    # 操控器，用于通过输入判断是否执行该循环
    keep_running = input("Make another walk? (Y/N): ")
    if keep_running.lower() == 'n':
        break
