import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)

    
########################################
broker_address="broker.emqx.io"

print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker

client.loop_start() #start the loop


print("Subscribing to topic","python/ICPBunny")
client.subscribe("python/ICPBunny")

try:
    while True:
        time.sleep(0.2) # wait
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
