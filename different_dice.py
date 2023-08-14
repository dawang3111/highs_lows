from die import Die
import pygal

# 创建一个D6和一个D10
die_1 = Die(8)
die_2 = Die(8)
# 掷骰子多次，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

max_result = die_1.num_sides + die_2.num_sides
# 分析结果
frequencies = []
for value in range(2, max_result + 1):
    frequency = results.count(value) / 50000
    frequencies.append(frequency)
#print(frequencies)

# 可视化结果
hist = pygal.Bar()
hist.title = "Results of rolling two D8 50,000 times."
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
#                  '13', '14', '15', '16']
hist.x_labels = [x for x in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_visual.svg')
