import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import matplotlib
import csv

matplotlib.use("AGG")

x = []
eCO2 = []
TVOC = []

path = "data/" + "2021-07-03_air_quality.csv"

with open(path, 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    # Skip header
    next(lines)
    for row in lines:
        x.append(row[0])
        eCO2.append(int(row[1]))
        TVOC.append(int(row[2]))


format = "%H:%M:%S"
xfmt = mdates.DateFormatter("%H:%M")


def convertTime(time):
    return dt.datetime.strptime(time, format)


times = list(map(convertTime, x))

fig, axs = plt.subplots(2, 1)

coPlot = axs[0]
vocPlot = axs[1]

coPlot.plot(times, eCO2, color='g', linestyle='solid',
            label="CO2", marker="")
vocPlot.plot(times, TVOC, color='g', linestyle='solid',
             marker='', label="TVOC")

coPlot.xaxis.set_major_formatter(xfmt)
vocPlot.xaxis.set_major_formatter(xfmt)

coPlot.axhline(500)
vocPlot.axhline(50)
coPlot.set(ylabel="eCO2 (ppm)")
vocPlot.set(ylabel='TVOC (ppb)', xlabel="Tid")
coPlot.set_title('2021-07-03', fontsize=20)
coPlot.grid()
vocPlot.grid()

plt.savefig("image.png")
