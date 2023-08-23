import csv
from datetime import datetime
from matplotlib import pyplot as plt

# the chart about sitka
filename_sitka = 'sitka_weather_2021_full.csv'
# the chart about death_valley
filename_death_valley = 'death_valley_2021_full.csv'
# put data from death_valley into chart
with open(filename_death_valley) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs_death = []
    dates_death = []
    lows_death = []
    for row in reader:
        try:
            date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[6])
            low = int(row[7])
        except ValueError:
            print(date, 'Missing data')
        else:
            highs_death.append(high)
            dates_death.append(date)
            lows_death.append(low)
# put data from stika into chart
with open(filename_sitka) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs_sitka = []
    dates_sitka = []
    lows_sitka = []
    awnds_sitka = []
    for row in reader:
        try:
            row[6] = (int(row[7])+int(row[8]))/2
            date = datetime.strptime(row[2], "%Y/%m/%d")
            high = int(row[7])
            low = int(row[8])
            awnd_sitka = float(row[3])
        except ValueError:
            print(date, 'Missing data')
        else:
            highs_sitka.append(high)
            dates_sitka.append(date)
            lows_sitka.append(low)
            awnds_sitka.append(awnd_sitka)
# 根据数据绘制图形
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates_death, highs_death, c='red', alpha=0.5)
# plt.plot(dates_death, lows_death, c='red', alpha=0.5)
# plt.fill_between(dates_death, highs_death, lows_death, facecolor='red', alpha=0.1)
# 绘制的是awnd
# plt.plot(dates_sitka, highs_sitka, c='blue', alpha=0.5)
# plt.plot(dates_sitka, lows_sitka, c='blue', alpha=0.5)
# plt.fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha=0.1)
plt.plot(dates_sitka, awnds_sitka, c='blue', alpha=0.5)
plt.title('Daily awnd -2021', fontsize=24)
plt.xlabel('', fontsize=16)
# 绘制斜制标签，确保太长的标签能完整显示
#fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='y', which='minor', labelsize=16, reset=True)

plt.show()
