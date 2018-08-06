#!/usr/bin/env python


# SETTING UP THE RPI, turning on blue light to show that rpi is ready to
# be used
import RPi.GPIO as#!/usr/bin/env python


# SETTING UP THE RPI, turning on blue light to show that rpi is ready to
# be used
import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
import warnings
import lcddriver


#creating LCD interface
lcd = lcddriver.lcd()

#measurement_wait = 5 # time of waiting between each temperature log (5 default)
def findDelayTime():
    print("Type in the amount of seconds you want between data logs (e.g. 60)")
    return int(input())
measurement_wait = findDelayTime()


# graphing function that updates graph once, per call
def updateGraph(xData, yData, temp, time):
    xData.append(time)
    yData.append(temp)
    plt.plot(xData, yData)
    plt.draw()
    plt.pause(0.01)

# records time in year- month - day, hour- minute - second
timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")  
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUTTON_GPIO_PIN = 21 #input pin for button
BLUE_GPIO_PIN = 6 # LED for  showing program running
RED_GPIO_PIN = 17 # LED for showing logging of data

GPIO.setup(BUTTON_GPIO_PIN, GPIO.IN) # input pin for button
GPIO.setup(BLUE_GPIO_PIN, GPIO.OUT) # LED for  showing program running
GPIO.setup(RED_GPIO_PIN, GPIO.OUT) # LED for showing logging of data
GPIO.output(BLUE_GPIO_PIN, GPIO.HIGH)

# Checking for button press and shutting down blue light and
# turning showing red light to indicate data is being recorded.
while True:
	if GPIO.input(BUTTON_GPIO_PIN):
		break
while GPIO.input(BUTTON_GPIO_PIN):
	pass
GPIO.output(BLUE_GPIO_PIN, GPIO.LOW)
GPIO.output(RED_GPIO_PIN, GPIO.HIGH)


# Opening new data file and recording data
# If button pressed, stops logging and turns off all light
filename = "".join(["temperaturedata", timestamp, ".log"]) 
datafile = open(filename, "w", 1)
beginTime = time.time() # time that we start logging data.

# setting up graph
warnings.filterwarnings("ignore",".*GUI is implemented.*")
xData = [] # Data list for x axis of graph
yData = [] # Data list for y axis of graph
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.xlabel('time (s)')
plt.ylabel('temperature (celsius)')
plt.title('Bee temperature graph')

while True:
    time_1 = time.time()
    tfile = open("/sys/bus/w1/devices/w1_bus_master1/28-0218321822ff/w1_slave")
    text = tfile.read()
    tfile.close()
    temperature_data = text.split()[-1]
    temperature = float(temperature_data[2:])
    temperature = temperature / 1000
    timePassed = float(int((time_1 - beginTime) * 100)) / 100
    datafile.write(str(timePassed)  + ": " + str(temperature) + " degrees celsius\n")
    time_2 = time.time()
    lcd.lcd_display_string("Temp in c: " + str(temperature), 1) #display to LCD
    lcd.lcd_display_string("Time in sec: " + str(timePassed), 2)
    updateGraph(xData, yData, temperature, timePassed)
    # Checking that the time between measuring temps are less than wait time.
    if (time_2 - time_1) < measurement_wait: 
            no_of_sleeps = int(round((measurement_wait - (time_2 - time_1)) / 0.1))
            for i in range(no_of_sleeps):
                    time.sleep(0.1)
                    if GPIO.input(BUTTON_GPIO_PIN):
                            break	
    if GPIO.input(BUTTON_GPIO_PIN):
            break
# Once button pressed, close the file and turn off the lights.
datafile.close()
GPIO.output(RED_GPIO_PIN, GPIO.LOW)



    
    
 GPIO
import time
import matplotlib.pyplot as plt
import warnings

#measurement_wait = 5 # time of waiting between each temperature log (5 default)
def findDelayTime():
    print("Type in the amount of seconds you want between data logs (e.g. 60)")
    return int(input())
measurement_wait = findDelayTime()


# graphing function that updates graph once, per call
def updateGraph(xData, yData, temp, time):
    xData.append(time)
    yData.append(temp)
    plt.plot(xData, yData)
    plt.draw()
    plt.pause(0.01)

# records time in year- month - day, hour- minute - second
timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")  
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUTTON_GPIO_PIN = 21 #input pin for button
BLUE_GPIO_PIN = 6 # LED for  showing program running
RED_GPIO_PIN = 17 # LED for showing logging of data

GPIO.setup(BUTTON_GPIO_PIN, GPIO.IN) # input pin for button
GPIO.setup(BLUE_GPIO_PIN, GPIO.OUT) # LED for  showing program running
GPIO.setup(RED_GPIO_PIN, GPIO.OUT) # LED for showing logging of data
GPIO.output(BLUE_GPIO_PIN, GPIO.HIGH)

# Checking for button press and shutting down blue light and
# turning showing red light to indicate data is being recorded.
while True:
	if GPIO.input(BUTTON_GPIO_PIN):
		break
while GPIO.input(BUTTON_GPIO_PIN):
	pass
GPIO.output(BLUE_GPIO_PIN, GPIO.LOW)
GPIO.output(RED_GPIO_PIN, GPIO.HIGH)


# Opening new data file and recording data
# If button pressed, stops logging and turns off all light
filename = "".join(["temperaturedata", timestamp, ".log"]) 
datafile = open(filename, "w", 1)
beginTime = time.time() # time that we start logging data.

# setting up graph
warnings.filterwarnings("ignore",".*GUI is implemented.*")
xData = [] # Data list for x axis of graph
yData = [] # Data list for y axis of graph
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.xlabel('time (s)')
plt.ylabel('temperature (celsius)')
plt.title('Bee temperature graph')

while True:
    time_1 = time.time()
    tfile = open("/sys/bus/w1/devices/w1_bus_master1/28-0218321822ff/w1_slave")
    text = tfile.read()
    tfile.close()
    temperature_data = text.split()[-1]
    temperature = float(temperature_data[2:])
    temperature = temperature / 1000
    timePassed = float(int((time_1 - beginTime) * 100)) / 100
    datafile.write(str(timePassed)  + ": " + str(temperature) + " degrees celsius\n")
    time_2 = time.time()
    updateGraph(xData, yData, temperature, timePassed)
    # Checking that the time between measuring temps are less than wait time.
    if (time_2 - time_1) < measurement_wait: 
            no_of_sleeps = int(round((measurement_wait - (time_2 - time_1)) / 0.1))
            for i in range(no_of_sleeps):
                    time.sleep(0.1)
                    if GPIO.input(BUTTON_GPIO_PIN):
                            break	
    if GPIO.input(BUTTON_GPIO_PIN):
            break
# Once button pressed, close the file and turn off the lights.
datafile.close()
GPIO.output(RED_GPIO_PIN, GPIO.LOW)



    
    

