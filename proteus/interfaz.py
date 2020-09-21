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
        accion=(msg.payload.decode("utf").split("")[0])
        intclave=(msg.payload.decode("utf-8").split("")[1])
        inttext=(msg.payload.decode("utf-8").split("")[2])
        print(accion)
        if intclave1==inttext1:
            if accion=="led1encendida":
                 led1act()
        print(intclave1)
        print(inttext1)
        if intclave1==inttext1:
            if accion=="led1apagada":
                 led1dest()
        print(intclave1)
        print(inttext1)
        if intclave1==inttext1:
            if accion=="led2encendida":
                 led2act()
        print(intclave1)
        print(inttext1)
        if intclave1==inttext1:
            if accion=="led2apagada":
                 led2dest()
        print(intclave1)
        print(inttext1)
mqttc = mqtt.Client() 
mqttc.on_message = on_message
mqttc.username_pw_set("mdpilatuna.fie@unach.edu.ec","quitociudadhermosa") 
mqttc.connect("maqiatto.com", 1883) 
mqttc.subscribe("mdpilatuna.fie@unach.edu.ec/dispositivo", 0)
rc=0
print("iniciando.....")
i=0
while rc ==0:
        time.sleep(2)
        rc=mqttc.loop()
        i=i+1
        hactual=datetime.datetime.now().strftime("%a,%d,%b,%Y,%H,%S")
        print(hactual)
        