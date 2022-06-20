# python 3.8

import random
import time

from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent
from ic.candid import encode, decode, Types

from datetime import datetime

from paho.mqtt import client as mqtt_client

from random import seed
from random import randint


seed(1)

# Identity and Client are dependencies of Agent
iden = Identity()
client = Client()
agent = Agent(iden, client)

broker = 'g12774ce.us-east-1.emqx.cloud'
port = 15772
topic = "supernova/dfx2iot"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'gladguy'
password = 'rehan123'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def iot_data(client):
    msg_count = 0
    while True:
        time.sleep(10)

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

        value = randint(25, 32)

        print("Current Time =", current_time)
        print("Temperature =", value)

        msg = f"Temperature : {value} on "

        msg = msg +  current_time + " to MQTT "  
        result = client.publish(topic, value)

        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Sending `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    iot_data(client)


if __name__ == '__main__':
    run()
