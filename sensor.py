
from __future__ import print_function
import serial, struct, sys, time, json
import pymysql
from datetime import datetime

conn = pymysql.connect(host='localhost',user='root',password='1234',db='sensor',charset='utf8')

curs = conn.cursor()
sql = """insert into dust(nt,PM25,PM100)
        values (%s,%s,%s)"""

sql2 = """insert into sta(nt,PM25,PM100)
        values (%s,%s,%s)"""
DEBUG = 0
CMD_MODE = 2
CMD_QUERY_DATA = 4
CMD_DEVICE_ID = 5
CMD_SLEEP = 6
CMD_FIRMWARE = 7
CMD_WORKING_PERIOD = 8
MODE_ACTIVE = 0
MODE_QUERY = 1

ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.baudrate = 9600

ser.open()
ser.flushInput()

byte, data = 0, ""

def dump(d, prefix=''):
    print(prefix + ' '.join(x.encode('hex') for x in d))

def construct_command(cmd, data=[]):
    assert len(data) <= 12
    data += [0,]*(12-len(data))
    checksum = (sum(data)+cmd-2)%256
    ret = "\xaa\xb4" + chr(cmd)
    ret += ''.join(chr(x) for x in data)
    ret += "\xff\xff" + chr(checksum) + "\xab"

    if DEBUG:
        dump(ret, '> ')
    return ret

def process_data(d):
    r = struct.unpack('<HHxxBB', d[2:])
    pm25 = r[0]/10.0
    pm10 = r[1]/10.0
    checksum = sum(ord(v) for v in d[2:8])%256
    return [pm25, pm10]
    #print("PM 2.5: {} μg/m^3  PM 10: {} μg/m^3 CRC={}".format(pm25, pm10, "OK" if (checksum==r[2] and r[3]==0xab) else "NOK"))

def process_version(d):
    r = struct.unpack('<BBBHBB', d[3:])
    checksum = sum(ord(v) for v in d[2:8])%256
    print("Y: {}, M: {}, D: {}, ID: {}, CRC={}".format(r[0], r[1], r[2], hex(r[3]), "OK" if (checksum==r[4] and r[5]==0xab) else "NOK"))

def read_response():
    byte = 0
    while byte != "\xaa":
        byte = ser.read(size=1)

    d = ser.read(size=9)

    if DEBUG:
        dump(d, '< ')
    return byte + d

def cmd_set_mode(mode=MODE_QUERY):
    ser.write(construct_command(CMD_MODE, [0x1, mode]))
    read_response()

def cmd_query_data():
    ser.write(construct_command(CMD_QUERY_DATA))
    d = read_response()
    values = []
    if d[1] == "\xc0":
        values = process_data(d)
    return values

def cmd_set_sleep(sleep=1):
    mode = 0 if sleep else 1
    ser.write(construct_command(CMD_SLEEP, [0x1, mode]))
    read_response()

def cmd_set_working_period(period):
    ser.write(construct_command(CMD_WORKING_PERIOD, [0x1, period]))
    read_response()

def cmd_firmware_ver():
    ser.write(construct_command(CMD_FIRMWARE))
    d = read_response()
    process_version(d)

def cmd_set_id(id):
    id_h = (id>>8) % 256
    id_l = id % 256
    ser.write(construct_command(CMD_DEVICE_ID, [0]*10+[id_l, id_h]))
    read_response()

if __name__ == "__main__":
    while True:
        cmd_set_sleep(0)
        cmd_set_mode(1);
        for t in range(15):
            values = cmd_query_data();
            if values is not None:
                print("PM2.5: ", values[0], ", PM10: ", values[1])
                a=datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                curs.execute(sql,(a,values[0],values[1]))
                if values[0] < 50 :
                    PM25sta = 0 
                elif values[0] >= 50 and values[0] < 100:
                    PM25sta = 1
                elif values[0] >= 100 and values[0] <150:
                    PM25sta = 2
                else:
                    PM25sta = 3
                
                if values[1] <50 :
                    PM100sta=0
                elif values[1] >= 50 and values[1] < 100:
                    PM100sta=1
                elif values[1] >= 100 and values[1] < 150:
                    PM100sta=2
                else:
                    PM100sta=3

                curs.execute(sql2,(a,PM25sta,PM100sta))
                conn.commit()
                time.sleep(20)

        # open stored data
        with open('/var/www/html/aqi.json') as json_data:
            data = json.load(json_data)

        # check if length is more than 100 and delete first element
        if len(data) > 100:
            data.pop(0)

        # append new values
        data.append({'pm25': values[0], 'pm10': values[1], 'time': time.strftime("%d.%m.%Y %H:%M:%S")})

        # save it
        with open('/var/www/html/aqi.json', 'w') as outfile:
            json.dump(data, outfile)

       # print("Going to sleep for 5min...")
        cmd_set_mode(0);
        cmd_set_sleep()
        
        conn.close()
