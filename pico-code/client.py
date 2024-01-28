from machine import Pin
import utime
import urequests
import network

#######Room ID############
room_id = 2
###########WiFi Stuff###############

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

SSID = 'samsung'
PASSWORD = 'preyasu1234'

while not wlan.isconnected():
    print('Connecting to network...')
    wlan.connect(SSID, PASSWORD)
    utime.sleep(1)
print('Network config:', wlan.ifconfig())


######### Https Requests #################

url = 'http://192.168.43.242:5000/'

def get_request():
    response = urequests.get(url + 'get/get_over')
#     print('Response code:', response.status_code)
#     print('Response text:', response.text)
    return response.text
    
def post_request(ID, count, temp, state):
    params = {
    "id": str(ID),
    "count": str(count),
    "temp": str(temp),
    "state": state
}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = urequests.post(url + 'post', json=params, headers=headers)
#     print('Response code:', response.status_code)
#     print('Response text:', response.text)
    response.close()


#################### SENSOR STUFF ##############################

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
trigger1 = Pin(5, Pin.OUT)
echo1 = Pin(4, Pin.IN)

light = Pin(14, Pin.OUT)

prev_dist = 1000
prev_dist1 = 1000
count = 0
thresh = 5
prev_count = 0
prev_time = utime.time()

state = 'OFF'

in_flag = False
out_flag = False


def distance():
    timepassed=0
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    return timepassed

def distance1():
    timepassed=0
    trigger1.low()
    utime.sleep_us(2)
    trigger1.high()
    utime.sleep_us(5)
    trigger1.low()
    while echo1.value() == 0:
        signaloff = utime.ticks_us()
    while echo1.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    return timepassed


########## Temperature Stuff ############
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)


#Main Loop
while True:
    
    reading = sensor_temp.read_u16() * conversion_factor 
    temp = 27 - (reading - 0.706)/0.001721
    
    measured_time = distance()
    measured_time1 = distance1()
    dist = (measured_time * 0.0343) / 2
    dist1 = (measured_time1 * 0.0343) / 2
    if dist < thresh and prev_dist > thresh and dist1 > thresh:
        if out_flag:
            out_flag = False
        else:
            count += 1
            in_flag = True
        
        out_flag = False
    elif dist > thresh and dist1 < thresh and prev_dist1 > thresh:
        if in_flag:
            in_flag = False
        else:
            count -= 1
            out_flag = True
    
    print(f'Distance1: {dist}')
    print(f'Distance2: {dist1}')
    print(f'Count: {count}')
    
    prev_dist = dist
    prev_dist1 = dist1
    
    
    if prev_count != count:
        if count != 0:
            state = 'ON'
            post_request(room_id, count, temp, state)
        else:
            state = 'OFF'
            post_request(room_id, count, temp, state)
        prev_count = count
    
    if utime.time() - prev_time >= 1:
        status = get_request()
        if status == 'yes':
            if state == 'ON':
                state = 'OFF'
            else:
                state = 'ON'
#             print('yessed')
        elif status == 'no':
            pass
#             print('noed')
        prev_time = utime.time()
#         print(state)
    
    if state == 'ON':
        light.high()
    else:
        light.low()
