# python3.8

import random

from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent
from ic.candid import encode, decode, Types

from datetime import datetime

from paho.mqtt import client as mqtt_client

#********************************************************#
# Identity and Client are dependencies of Agent
iden = Identity()
client = Client()
agent = Agent(iden, client)
#********************************************************#

#********************************************************#
broker = 'g12774ce.us-east-1.emqx.cloud'
port = 15772
topic = "supernova/dfx2iot_dev1"
# generate client ID with pub prefix randomly
client_id = f'supernova-dfx-iot-{random.randint(0, 1000)}'
username = 'SuperNova'
password = 'supernova'
#********************************************************#


def connect_mqtt() -> mqtt_client:
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


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print("Temperature from MQTT Broker: " + msg.payload.decode())

        Temperature = int(msg.payload.decode())
        params = [
            {'type': Types.Nat, 'value': Temperature}
        ]
        
        result = agent.update_raw("e6v3r-ciaaa-aaaaf-qaebq-cai", "addIoTData", encode(params))
        result = agent.update_raw("uca7j-eqaaa-aaaah-qbiha-cai", "addIoTData", encode(params))


    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
