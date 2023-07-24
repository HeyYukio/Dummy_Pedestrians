
import socket 
import json
import time
import random

# SETTINGS

settings = {
    'host': '10.0.0.7',
    'port': 9091,
    
    "pedestrians_rnd": True,
    "fixed_pededstrians_number": 1,
    "max_pedestrians": 10,

    "time_rnd": False,
    "fixed_pedestrians_interval": 3, 
    "time_rand_interval_min": 90, 
    "time_rand_interval_max": 180, 
    
}

def get_pedestrians_interval():

    if settings['time_rnd'] == True:
        return random.randint(settings['time_rand_interval_min'], settings['time_rand_interval_min'])
    else:
        return settings['fixed_pedestrians_interval']

def get_detections():

    global id
    data = {"id":id, "category": "Pessoa", "time": "20220620232932.273", "detections": [], "evidence": None}
    if settings['pedestrians_rnd'] == True:
        interval = random.randint(1, settings['max_pedestrians'])
        for i in range (0,interval):
            data['detections'].append([41.32, [883, 230, 921, 288]])
    else:
        for i in range (0,settings['fixed_pededstrians_number']):
            data['detections'].append([41.32, [883, 230, 921, 288]])

    id += 1
    return data
    

def sendData():
    PORT = 9091 

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((settings['host'], settings['port']))
    
    while True:

        # data = {"id":id, "category": "Pessoa", "time": "20220620232932.273", "detections": [[41.32, [883, 230, 921, 288]], [61.37, [922, 226, 955, 291]], [ 75.22, [428, 211, 458, 287]], [85.89, [227, 223, 269, 342]]], "evidence": None}
        # data = {"id":id, "category": "Pessoa", "time": "20220620232932.273", "detections": [], "evidence": None}

        data = get_detections()
        json_data = json.dumps(data)

        s.sendall( (json_data+'\n').encode() )
        time.sleep( get_pedestrians_interval() )

    s.close()

id = 1
sendData()



