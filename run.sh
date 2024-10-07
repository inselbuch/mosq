docker run -d \
   --name mosquitto \
   --network transpara \
   -p 1883:1883 \
   -p 9001:9001 \
   -v /home/inselbuch/mosq/mosquitto.conf:/mosquitto/config/mosquitto.conf \
   eclipse-mosquitto
