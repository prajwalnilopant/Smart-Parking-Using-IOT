from ubidots import ApiClient
import RPi.GPIO as GPIO
import time

api = ApiClient('A1E-6784a6c3b518b1fe33d4d51f2dd4fed1574e')#API_Key

#Variable IDs
variable1 = api.get_variable('5b2603bec03f970e9613cf48')
variable2 = api.get_variable('5b2603cbc03f970db08d6423')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(13,GPIO.IN)
GPIO.setup(19,GPIO.IN)

a=GPIO.input(13)
c=GPIO.input(19)
if(a==False):
    print("slot 1 is Engaged")
else:
    print("slot 1 is Vaccant")

if(c==False):
    print("slot 2 is Engaged")
else:
    print("slot 2 is Vaccant")
while 1:
    b=GPIO.input(13)
    d=GPIO.input(19)
    if(a!=b):
        status1=0
        if(b==False):
            print("slot 1 is Engaged")
            status1=1
            variable1.save_value({'value':status1})
        else:
            print("slot 1 is Vaccant")
            status1=0
            variable1.save_value({'value':status1})#saving to cloud
    a=b
    
    if (c!=d):
        status2=0
        if(d==False):
            print("slot 2 is Engaged")
            status2=1
            variable2.save_value({'value':status2})
        else:
            print("slot 2 is Vaccant")
            status2=0
            variable2.save_value({'value':status2})

    c=d
    

        
