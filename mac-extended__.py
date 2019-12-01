import subprocess
from subprocess import Popen
import serial
from pynput import keyboard
from pynput.keyboard import Key, Controller

kybrd = Controller()

cmd_pressed = False

def on_press(key):
    if key == keyboard.Key.alt:
        global cmd_pressed
        cmd_pressed = True
        print("cmd presed")

def on_release(key):
    if key == keyboard.Key.alt:
        global cmd_pressed
        cmd_pressed = False
        print("cmd not presed")


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

key_right            = '''tell application "System Events"
                            key code 124
                        end tell'''

# zoom_in              = '''tell application "System Events"
#                             key code 24 using {command down}
#                         end'''

# zoom_out             = '''tell application "System Events"
#                             key code 27 using {command down}
#                         end'''


touches              = 0
notouches            = 0
old_distance         = 0

while True:
    arduino_data     = Arduino_Serial.readline()
    print(cmd_pressed)
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
    elif cmd_pressed == True and arduino_data == b'You moved closer\r\n':
        print('You moved closer')
        zoom_out()
        # p = Popen(['osascript', '-e', zoom_out])
    elif cmd_pressed == True and arduino_data == b'You moved away\r\n':
        print('You moved away')
        zoom_in()
        # p = Popen(['osascript', '-e', zoom_in])