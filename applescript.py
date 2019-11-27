from subprocess import Popen
import subprocess

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
#-_-_-_-_-_-_-_-_-_-_-_-_-_Simple apple script-_-_-_-_-_-_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

script  = '''tell application "System Events"
            delay 0.1
            key down command
            keystroke tab
            delay 1
            key up command
            end tell'''
p = Popen(['osascript', '-e', script])

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
#-_-_-_-_-_-_-_-_-_-_ Run anything on the Terminal _-_-_-_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# subprocess.run("open https://www.youtube.com/watch?v=El9K_EEv8cU", shell=True)
# subprocess.run("osascript -e 'set Volume 5'", shell=True)
# subprocess.run("/Applications/Mission\ Control.app/Contents/MacOS/Mission\ Control 1", shell=True)
# subprocess.run('osascript -e "tell applications \\"System Events\\"" -e "key code 103" -e "end tell"', shell=True)



#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
#-_-_-_-_-_-_-_-_-_-_-_-_- Using a Function -_-_-_-_-_-_-_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# def exec_applescript(script):
#     p = Popen(['osascript', '-e', script])

# exec_applescript('say "I am singing la la la la" using "Alex" speaking rate 140 pitch 60')
# exec_applescript('say "Still singing, hahaha" using "Alex" speaking rate 140 pitch 66')
