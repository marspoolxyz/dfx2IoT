# python 3.8

import random
import time
from datetime import datetime

from paho.mqtt import client as mqtt_client


broker = 'g12774ce.us-east-1.emqx.cloud'
port = 15772
topic = "python/mqtt"
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


def heartbeat(client):
    msg_count = 0
    while True:
        time.sleep(10)
        msg = f"HeartBeat: {msg_count}"

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

        msg = current_time + " : " + msg
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

def publish(client):
    msg_count = 0
     
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        msg = input('Enter the message:')

        now = datetime.now()
        msg = f"HeartBeat: {msg_count}"
        result = client.publish(topic, msg)


        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

        msg = current_time + " : " + msg
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    #publish(client)
    heartbeat(client)


if __name__ == '__main__':
    run()
