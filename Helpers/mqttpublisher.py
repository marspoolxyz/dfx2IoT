import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    Messagerecieved=True
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def on_connect(client, userdata, flags,rc):
    if rc == 0:
        print("Client is connected");
        global connected
        connected=True
    
########################################

connected=False
Messagerecieved=False

broker_address="broker.emqx.io"

print("creating new instance")
client = mqtt.Client("ICPIotx") #create new instance
client.on_message=on_message #attach function to callback
client.on_connect=on_connect 
print("connecting to broker")
client.connect(broker_address) #connect to broker

client.loop_start() #start the loop

print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")
while connected!=True:
    time.sleep(0.2)

while Messagerecieved!=True:
    time.sleep(2)
    
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","Light is ON")
time.sleep(2) # wait

client.loop_stop() #stop the loop
