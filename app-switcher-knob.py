import subprocess
from subprocess import Popen
import pyautogui
import serial
import time

Arduino_Serial = serial.Serial('/dev/tty.usbmodem14201',9600)    

open_app_switcher    = '''tell application "System Events"
                            delay 0.1
                            key down command
                            keystroke tab
                            delay 1
                        end tell'''

close_app_switcher   = '''tell application "System Events"
                            key up command
                        end tell'''

key_left             = '''tell application "System Events"
                            key code 123
                        end tell'''

key_right             = '''tell application "System Events"
                            key code 124
                        end tell'''

touches              = 0
notouches            = 0

while True:
    arduino_data = Arduino_Serial.readline()
    print(arduino_data)
    if arduino_data == b'touch\r\n':
        touches += 1
        if touches>10:
            print("touch alert!!!")
            p = Popen(['osascript', '-e', open_app_switcher])
            touches = 0
            while True:
                arduino_data = Arduino_Serial.readline()
                print('Still touching 😎')
                if arduino_data == b'left\r\n':
                    p = Popen(['osascript', '-e', key_left])
                if arduino_data == b'right\r\n':
                    p = Popen(['osascript', '-e', key_right])
                if arduino_data == b'notouch\r\n':
                    notouches += 1
                if notouches > 10:
                    p = Popen(['osascript', '-e', close_app_switcher])
                    notouches = 0
                    break