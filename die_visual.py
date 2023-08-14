import pygal

from die import Die

# 创建两个D6
die1 = Die()
die2 = Die()
die3 = Die()
# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(10000):
    # 三个骰子相加
    # result = die1.roll() + die2.roll() + die3.roll()
    # 两个骰子相乘
    result = die1.roll() * die2.roll()
    results.append(result)
max_result = die1.num_sides * die2.num_sides
# 分析结果
frequencies = []
for value in range(1, max_result + 1):
    frequency = results.count(value) / 10000
    frequencies.append(frequency)
#print(frequencies)

# 对结果进行可视化,该包为矢量图形文件，保证在不同的显示器显示大小一样
hist = pygal.Bar()
hist.title = "Results of rolling three D6 10000 times."
#hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_labels = [x for x in range(1, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
# 添加一类统计对象，前边参数表示对象名称，后边参数表示该对象在每一个横坐标上的值
hist.add('D6*D6', frequencies)
hist.render_to_file('die_visual.svg')
