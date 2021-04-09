import os, glob, time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
temperature = "ERROR"
bucket = "sensor_data"
username = 'SmartTrain'
password = 'password'
client = InfluxDBClient(url="ip&port", token=f"{username}:{password}", org="my-org")
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

while True:
    tag = time.ctime()
    temperature = read_temp()
    p = Point("my_measurement").tag("location", "Prague").field("temperature", temperature)
    print("The Temperature is: " + str(temperature))
    write_api.write(bucket=bucket, record=p)
    time.sleep(3)
