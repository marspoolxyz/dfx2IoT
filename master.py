import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")
 
Connected = False   #global variable for the state of the connection
 
broker_address="broker.emqx.io"
broker_address="g12774ce.us-east-1.emqx.cloud"
port = 8083
user = "gladguy"
password = "rehan123"
 
client = mqttClient.Client("python/ICPBunny")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address,port=port)          #connect to broker
#client.connect(broker_address)          #connect to broker

print("Connection....")

client.loop_start()        #start the loop

print("Connection...1.")
value = input('Enter the message:')
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
try:
    while True:
 
        value = input('Enter the message:')
        client.publish("python/ICPBunny",value)
 
except KeyboardInterrupt:
 
    client.disconnect()
    client.loop_stop()
