import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO
import datetime
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
a=open("sensor.txt","w")
def led1act():
        GPIO.output(18,True)
        time.sleep(0.5)
        a.write(hactual+str("LED 1 ENCENDIDO")+"\n")
        c=("LED 1 ACTIVADO")
        mqtt.publish("mdpilatuna.fie@unach.edu.ec/servidor",str(c))
def led1dest():
        GPIO.output(18,False)
        time.sleep(1)
        a.write(hactual+str("LED 1 PAGADO")+"\n")
        c=("LED 1 APAGADO")
        mqtt.publish("mdpilatuna.fie@unach.edu.ec/servidor",str(c))
def led2act():
        GPIO.output(22,True)
        time.sleep(0.5)
        a.write(hactual+str("LED 2 ENCENDIDO")+"\n")
        c=("LED 2 ACTIVADO")
        mqtt.publish("mdpilatuna.fie@unach.edu.ec/servidor",str(c))
def led2dest():
        GPIO.output(22,False)
        time.sleep(1)
        a.write(hactual+str("LED 2 PAGADO")+"\n")
        c=("LED 2 APAGADO")
        mqtt.publish("mdpilatuna.fie@unach.edu.ec/servidor",str(c))
def on_message(client,obj,msg):
        accion=(msg.payload.decode("utf").split("")[])
        
        