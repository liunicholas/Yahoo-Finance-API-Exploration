from yfinance import *

stock = Ticker("spy")
hist = stock.history(period="max")

openList = []
closeList = []
dateList = []
for i in range(hist.shape[0]):
    line = hist.iloc[i]
    openList.append(line["Open"])
    closeList.append(line["Close"])
    dateList.append([hist.index[i].year,hist.index[i].month,hist.index[i].day])

# import matplotlib.pyplot as plt, mpld3
# plt.plot(openList)
# plt.show()
# mpld3.show()

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import numpy as np

# stringDate = str(dateList[0][0]) + "-" + str(dateList[0][1]) + "-" + str(dateList[0][2])
# length = len(dateList) - 1
# stringDate2 = str(dateList[length][0]) + "-" + str(dateList[length][1]) + "-" + str(dateList[length][2])
# times = pd.date_range(start=stringDate, freq='D', end=stringDate2)

fig, ax = plt.subplots(1)
# fig.autofmt_xdate()
# x = np.array(times)
y = np.array(openList)
plt.plot(y)

# x = np.array(times)
y = np.array(closeList)
plt.plot(y)

# xfmt = mdates.DateFormatter('%d-%m-%y')
# ax.xaxis.set_major_formatter(xfmt)

plt.show()
