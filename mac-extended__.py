import subprocess
from subprocess import Popen
import serial
from pynput import keyboard
from pynput.keyboard import Key, Controller

kybrd = Controller()

alt_pressed = False

def on_press(key):
    if key == keyboard.Key.alt:
        global alt_pressed
        alt_pressed = True
        print("alt presed")

def on_release(key):
    if key == keyboard.Key.alt:
        global alt_pressed
        alt_pressed = False
        print("alt not presed")

def zoom_in ():
    kybrd.press(Key.cmd)
    kybrd.press('+')
    kybrd.release('+')
    kybrd.release(Key.cmd)

def zoom_out ():
    kybrd.press(Key.cmd)
    kybrd.press('-')
    kybrd.release('-')
    kybrd.release(Key.cmd)

def open_app_switcher():
    kybrd.press(Key.cmd)
    kybrd.press(Key.tab)
    kybrd.release(Key.tab)
    
def close_app_switcher():
    kybrd.release(Key.cmd)

def key_left():
    kybrd.press(Key.left)
    kybrd.release(Key.left)

def key_right():
    kybrd.press(Key.right)
    kybrd.release(Key.right)

# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

# ...or, in a non-blocking fashion:

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

Arduino_Serial = serial.Serial('/dev/tty.usbmodem14201',9600)    

touches              = 0
notouches            = 0
old_distance         = 0

while True:
    arduino_data     = Arduino_Serial.readline()
    print(alt_pressed)
    if arduino_data == b'touch\r\n':
        touches += 1
        if touches>10:
            print("touch alert!!!")
            open_app_switcher()
            # p = Popen(['osascript', '-e', open_app_switcher])
            touches = 0
            while True:
                arduino_data = Arduino_Serial.readline()
                print('Still touching 😎')
                if arduino_data == b'left\r\n':
                    key_left()
                    # p = Popen(['osascript', '-e', key_left])
                if arduino_data == b'right\r\n':
                    key_right()
                    # p = Popen(['osascript', '-e', key_right])
                if arduino_data == b'notouch\r\n':
                    notouches += 1
                if notouches > 10:
                    close_app_switcher()
                    # p = Popen(['osascript', '-e', close_app_switcher])
                    notouches = 0
                    break
    elif alt_pressed == True and arduino_data == b'You moved closer\r\n':
        print('You moved closer')
        zoom_out()
        # p = Popen(['osascript', '-e', zoom_out])
    elif alt_pressed == True and arduino_data == b'You moved away\r\n':
        print('You moved away')
        zoom_in()
        # p = Popen(['osascript', '-e', zoom_in])