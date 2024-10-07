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

if len(sys.argv) < 2:
   brokerhost = 'localhost'
else:
   brokerhost = sys.argv[1]

# simulate queuing of events from parc

clientid = 'Gigabits-006'
brokerusername = 'gigabits'
brokerpassword = '096sF9Pz7N531uY'
brokerport = 1883
topic = 'gigabits/telemetry/Gigabits-006'

data = {}

client = mqtt.Client(clientid)
client.connect(brokerhost,port=brokerport)

while (True):

   humidity = float(randint(3,17))/18.0 + 29.0
   temperature = float(randint(3,18))/19.0 + 72.0
   pressure = float(randint(7,34))/15.0 + 1000.0
   gas = float(randint(5,25))/24.0 + 35.0
   hygrometer = float(randint(11,57))/28.0+640.0

   #data['data'] = {
   data = {
      'humidity' : humidity,
      'temperature' : temperature,
      'barometricpressure' : pressure,
      'gas' : gas,
      'hygrometer' : hygrometer
   }

   datas = json.dumps(data)

   ret=client.publish(topic,payload=datas)
   print("Return from publish = {}".format(ret))

   time.sleep(5)
