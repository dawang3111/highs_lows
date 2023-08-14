import matplotlib.pyplot as plt

# 折线图的形式
input_value = list(range(1, 5000))
squares = [value**3 for value in input_value]
# plt.plot(input_value, squares, linewidth=5)
#
'''折线图的方式设置标题，并给坐标轴加上标签'''
# plt.title('squares number', fontsize=24)
# plt.xlabel('value', fontsize=14)
# plt.ylabel('Squares of value', fontsize=14)
# plt.tick_params(axis='both', labelsize=14)
# plt.show()

# 散点图的形式
plt.scatter(input_value, squares, c=input_value, cmap=plt.cm.Blues, edgecolors='none', s=40)
#plt.scatter(input_value, squares, edgecolors='none', s=40)
# 设置标题和横纵坐标
plt.title('cube number', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('cube of value', fontsize=14)

# 设置标记刻度大小, which 表示的刻度大小
plt.tick_params(axis='both', which='major', labelsize=14)
# 设置取值范围
#plt.axis([0, 5001, 0, 1100000000000])
# 显示图表,且之后会释放图片内存
plt.show()
# 将最后的图表储存
#plt.savefig('square_number.png', bbox_inches='tight')
