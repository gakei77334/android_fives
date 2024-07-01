from ppadb.client import Client
from PIL import Image
import numpy
import time
import random

adb = Client()
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

def screencap(x, y):
    image = device.screencap()
    with open('test.png', 'wb') as f:
        f.write(image)
    image = Image.open('test.png')
    image = numpy.array(image, dtype=numpy.uint8)

    pixel = image[x, y]
    pixel_red = pixel[2]
    print('Red:', pixel_red)
    return pixel_red

def open_fives():
    # Wake up the device
    device.shell('input keyevent 26')
    print('Waking up the device...')
    time.sleep(2)  # Wait for the device to wake up

    # Swipe to unlock
    device.shell('input swipe 350 1220 350 500')
    print('Swiping to unlock...')
    time.sleep(2)  # Wait for the swipe gesture to complete
    
    device.shell('input keyevent KEYCODE_HOME')
    print('Home Button')
    device.shell('input tap 82 844')
    print('Open Virgin App')
    time.sleep(7)
    device.shell('input tap 605 697')
    print('Tap into Fives')
    time.sleep(5)
    device.shell('input swipe 350 1109 350 397 1500')
    print('Swiped')
    

while True:
    open_fives()
    
    pixel_red = screencap(729, 63)
    if 8 < pixel_red < 12:
        device.shell('input tap 63 729')
        print('First Player Revealed')
        
    pixel_red = screencap(729, 280)
    if 8 < pixel_red < 12:
        device.shell('input tap 280 729')
        print('Second Player Revealed')
        
    pixel_red = screencap(729, 480)
    if 8 < pixel_red < 12:
        device.shell('input tap 480 729')
        print('Third Player Revealed')
        
    pixel_red = screencap(1125, 172)
    if 8 < pixel_red < 12:
        device.shell('input tap 260 1129')
        print('Fourth Player Revealed')
        
    pixel_red = screencap(1148, 388)
    if 8 < pixel_red < 12:
        device.shell('input tap 388 1148')
        print('Fifth Player Revealed')
        
    else:
        print('Nothing to reveal')
    
    time.sleep(60)
    device.shell('input tap 524 1234')
    print('Menu Button...')
    device.shell('input tap 591 382')
    print('Clearing all windows...')
    device.shell('input keyevent 26')
    print('Now going to sleep...')
    time.sleep(24 * 60 * 60)

