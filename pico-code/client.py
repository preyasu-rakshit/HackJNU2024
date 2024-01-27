from machine import Pin
import utime
import urequests
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

SSID = 'samsung'
PASSWORD = 'preyasu1234'

while not wlan.isconnected():
    print('Connecting to network...')
    wlan.connect(SSID, PASSWORD)
    utime.sleep(1)
print('Network config:', wlan.ifconfig())

'''
Https Requests
'''

url = 'http://192.168.43.242:5000/'

def get_request(param):
    response = urequests.get(url + 'get/' + param)
    print('Response code:', response.status_code)
    print('Response text:', response.text)
    response.close()
    
def post_request(id, count, ):
    params = {
    "id": '1',
    "count": '5',
    "state": 'ON'
}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = urequests.post(url + 'post', json=params, headers=headers)
    print('Response code:', response.status_code)
    print('Response text:', response.text)
    response.close()

 
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
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
                 
# while True:
#     measured_time = distance()     
#     distance_cm = (measured_time * 0.0343) / 2
#     print(distance_cm)

get_request('hi')
