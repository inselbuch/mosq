#
#	(C) Copyright 2021 Transpara LLC, All rights reserved.
#
#	simulator for parc mqtt data into mqtt
#
#	February 22, 2021 - Inselbuch
#
import os
import sys
import time
import json
from random import randint
from datetime import datetime
from dateutil.tz import tz
import time
import paho.mqtt.client as mqtt

topic = 'gigabits/telemetry/Gigabits-006'

def on_message(client,userdata,message):
   now = datetime.now()
   x = str(message.payload.decode('utf-8'))
   j = json.loads(x)
   print('message received {} {}'.format(now,j))
   #print('message topic=',message.topic)
   #print('message qos=',message.qos)
   #print('message retain flag=',message.retain)

if len(sys.argv) < 2:
   broker_address="localhost" 
else:
   broker_address=sys.argv[1]

print("Connecting to {}".format(broker_address))

client = mqtt.Client("receive") #create new instance
client.on_message=on_message
client.connect(broker_address) #connect to broker
print("Connected.")
client.loop_start()
client.subscribe(topic)
while (True):
   time.sleep(1)
client.loop_stop()

