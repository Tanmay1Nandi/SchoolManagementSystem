
import requests
import time
import winsound

i=0

try:
    while True:
        response=requests.get('https://jeemainsession2.ntaonline.in/frontend/web/scorecard/index')
        print("requested")
        if (response.status_code != 404):
            print(response.status_code)
            duration = 100 
            freq = 540  
            winsound.Beep(freq, duration)
        elif (response.status_code == 404):
            print('NOTHING SO FAR',response.status_code,i)
            i=i+1
        else:
            duration = 100 
            freq = 540  
            winsound.Beep(freq, duration+100)
            print(response.status_code)
        
        time.sleep(2)        
except:
    duration = 1000 
    freq = 440  
    winsound.Beep(freq, duration)



