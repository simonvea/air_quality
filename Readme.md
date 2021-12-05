# Collectt Air Quality

This is a small script to run and save air quality data using a sensor on a raspberry pi.

## Saving the data
Data is saved approx every minute as an average for that minute.

Two options for saving the data are available.

### Locally
Locally it is saved as csv in the data subfolder. A new CSV file is created for each day.

### InfluxDB
It is also able to be saved to influxDb. This requires a token.

Influx db token is saved as an environmental variable in /etc/environment as INFLUXDB_TOKEN

## Lights
Locally the current air quality is displayed using three LED lights, based on the following criteria.

* < 500 CO2 and < 50 TVOC is good air quality. Green light.
* 500-100 CO2 is a little uncomfortable, 50-750 TVOC is uncomfortable. Yellow light.
* 1000-2500 CO2 will make you tired, 750-6000 TVOC will lead to headache and depressive. Red light.
* 2500-5000 CO2 is unhealthy, >6000 TVOC will lead to headache and other nerve problems. Red light.

## Run
To start as a background process, run:

```bash
nohup ./collect_air_quality.py > output.log &
```

It only starts actual measurments after 15s of values.