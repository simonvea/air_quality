from sgp30 import SGP30
import time
import sys

sgp30 = SGP30()

# Only starts actual measurments after 15s of values.
# < 500 CO2 and < 50 TVOC is good air quality
#  500-100 CO2 is a little uncomfortable, 50-750 TVOC is uncomfortable
# 1000-2500 CO2 will make you tired, 750-6000 TVOC will lead to headache and depressive
# 2500-5000 CO2 is unhealthy, >6000 TVOC will lead to headache and other nerve problems

# result = sgp30.command('set_baseline', (0xFECA, 0xBEBA))
# result = sgp30.command('get_baseline')
# print(["{:02x}".format(n) for n in result])

print("Sensor warming up, please wait...")
def crude_progress_bar():
    sys.stdout.write('.')
    sys.stdout.flush()

sgp30.start_measurement(crude_progress_bar)
sys.stdout.write('\n')

while True:
    result = sgp30.get_air_quality()
    print(result)
    time.sleep(1.0)
