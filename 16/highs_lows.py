import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    dates = []
    for row in reader:
        date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[4])
        highs.append(high)
        dates.append(row[2])
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.title('Daily high temperatures, July 2014', fontsize=24)
plt.xlabel('', fontsize=16)
# 绘制斜制标签，确保太长的标签能完整显示
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
