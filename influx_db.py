from datetime import datetime
import os

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "simon.opheim+influxdb@pm.me"
bucket = "simon.opheim+influxdb's Bucket"

client = InfluxDBClient(
    url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)


def saveToDb(eCO2, TVOC, room="office"):

    point = Point("airQuality") \
        .tag("room", room) \
        .field("TVOC", TVOC) \
        .field("eCO2", eCO2) \
        .time(datetime.utcnow(), WritePrecision.NS)

    write_api.write(bucket, org, point)
