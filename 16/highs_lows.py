import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2021_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    dates = []
    for row in reader:
        date = datetime.strptime(row[2], "%Y/%m/%d")
        high = int(row[7])
        highs.append(high)
        dates.append(date)
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.title('Daily high temperatures-2021', fontsize=24)
plt.xlabel('', fontsize=16)
# 绘制斜制标签，确保太长的标签能完整显示
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='y', which='minor', labelsize=16,reset=True)

plt.show()
