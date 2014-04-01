import time
import RPi.GPIO as io
io.setmode(io.BCM)

logFile = '/home/pi/garageDoorLog.txt'

def doLog(logStr):
    msg = "%s: %s" % (time.strftime("[%Y_%d_%m (%a) - %H:%M:%S]", time.localtime()), logStr)
    print msg
    f = open(logFile, 'a')
    f.write(msg + '\n')
    f.close()

def alert(buzzer_pin):
    io.output(buzzer_pin, io.HIGH)
    time.sleep(0.3)
    io.output(buzzer_pin, io.LOW)
    time.sleep(0.1)
    io.output(buzzer_pin, io.HIGH)
    time.sleep(0.3)
    io.output(buzzer_pin, io.LOW)

class GarageMonitor:
    """ 
    Using proximity sensor on garage door, we monitor the open/close status,
    and indicate when it is open by outputting a DIO state.
    """
    (STOPPED, RUNNING) = range(2)

    def __init__(self):
        self.PIR_pin  = 17
        self.door_pin = 18
        self.sleep_time = 2.0
        self.time_last_opened = 0.0
        self.time_last_closed = 0.0
        self.state = STOPPED
        doLog("initialized GarageMonitor object")

    def processDoorOpen(self, time_opened):
        doLog("Door is open!!!")
        io.output(led_pin, io.HIGH)

    def processDoorClosed(self, time_closed):
        doLog ("Door is closed!!!")
        io.output(led_pin, io.LOW)

doLog("****************************** Starting up...")    
doLog("Sleep time = %f" % (sleep_time)) 
#outputs:
r1_pin  = 22
r2_pin  = 23
r3_pin  = 24
r4_pin  = 25
buzzer_pin = 4
io.setup(r1_pin, io.OUT) 
io.setup(r2_pin, io.OUT) 
io.setup(r3_pin, io.OUT) 
io.setup(r4_pin, io.OUT) 
io.setup(buzzer_pin, io.OUT) 
#inputs:   
door_pin = 18
PIR_pin = 17
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP) # activate input with PullUp
door_state = -1
while True:
    new_door_state = io.input(door_pin)
    if new_door_state != door_state:
        door_state = new_door_state
        if door_state == 0:
            processDoorOpen()
        elif door_state == 1:
            processDoorClosed()
    time.sleep(sleep_time)
