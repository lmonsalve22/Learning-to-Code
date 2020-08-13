import csv
import matplotlib.pyplot as plt 
from datetime import datetime

filename = './project_data_files/sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_line = next(reader)

    highs, low, date = [], [], []
    for row in reader:
        highs.append(int(row[1]))

        low.append(int(row[2]))

        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        date.append(current_date)

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(date, highs)
plt.plot(date, low)
plt.tick_params(axis='both', which='major')
fig.autofmt_xdate()

plt.show()