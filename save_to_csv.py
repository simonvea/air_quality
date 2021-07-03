import csv
from datetime import date, datetime
import os

fields = ['Time', 'eCO2', 'TVOC']


def saveAirQualityToCSV(eCO2, TVOC):

    now = datetime.now().strftime("%H:%M:%S")
    today = date.today().strftime("%Y-%m-%d")
    row = [now, eCO2, TVOC]
    folder = "data"
    filename = today + '_air_quality.csv'
    file = folder + "/" + filename

    if os.path.exists(file):
        with open(file, 'a') as f:
            write = csv.writer(f)
            write.writerow(row)

    else:
        with open(file, 'w') as f:
            write = csv.writer(f)
            write.writerow(fields)
            write.writerow(row)
