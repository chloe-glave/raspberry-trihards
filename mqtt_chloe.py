import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt


MQTT_CHLOE = "192.168.43.106" # Chloe's IP
MQTT_KAYDEN = "192.168.43.12" # Kayden's IP
MQTT_JACKY = "192.168.43.142" # Jacky's IP
MQTT_PATH = "test_channel" # the topic name

 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Chloe: "+str(msg.payload.decode('utf-8')))
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_CHLOE, 1883, 60)  # must be the IP of the person running the file
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()


publish.single(MQTT_PATH, "Chloe joined the server!", hostname=MQTT_CHLOE)

while True:
    msg = input()
    publish.single(MQTT_PATH, msg, hostname=MQTT_CHLOE)
    publish.single(MQTT_PATH, msg, hostname=MQTT_KAYDEN)
    publish.single(MQTT_PATH, msg, hostname=MQTT_JACKY)