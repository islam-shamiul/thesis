import paho.mqtt.client as mqtt #import the client1
import cv2
import io
from PIL import Image
import numpy as np
import base64

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
def process_message(client, userdata, msg):
    print("massege received:",str(msg.payload.decode("utf-8")))
    """img = base64.b64decode(msg.payload)
    npimg = np.frombuffer(img,np.uint8)
    source = cv2.imdecode(npimg, 1)
    cv2.imshow("image",source)
    f = open('output.jpg', "wb")
    f.write(msg.payload)
    print("Image Received")
    #image = Image.open(io.BytesIO(f))
    #image.show()
    
   
    f.close()"""
broker_address="192.168.0.101" 
client = mqtt.Client("s1") 
client.on_connect = on_connect
client.on_message = process_message

#create new instance

client.connect(broker_address) #connect to broker

client.subscribe("test/message")
client.loop_forever()
