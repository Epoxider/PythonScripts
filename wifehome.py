import os
from gtts import gTTS
import time

hostname = 'wifes '

alarm = 'Wife is home'
language = 'en'
soundfile = gTTS(text=alarm,lang=language, slow=False)
soundfile.save('alarm.mp3')

while True:
    response = os.system('ping -c 1 '+hostname)
    if response == 0:
        print('Wife is on network')
        os.system('mpg321 alarm.mp3')
        break
    else:
        print('wife is not home')
        time.sleep(2)
