from time import sleep
from datetime import *
from os import system

while i:=True:
    t1 = input("Set the alarm time in [hh:mm:ss] format: ")
    try:
        c_t1 = datetime.strptime(t1,"%H:%M:%S")
        c_t1 = c_t1 - datetime(1900,1,1)
        break
    except:
        print("Set the correct time with format")

t2 = datetime.now()
c_t2 = t2.strftime("%H:%M:%S")
c_t2 = datetime.strptime(c_t2,"%H:%M:%S")
c_t2 = c_t2 - datetime(1900,1,1)

sec_t1 = c_t1.total_seconds()
sec_t2 = c_t2.total_seconds()

if sec_t1<sec_t2:
    sec_t1 = sec_t2 + 86400 - (sec_t2-sec_t1)   #total seconds in 24hrs = 86400
    print("Your alarm is set for tomorrow at",c_t1)
else:
    print("Your alarm is set for today at",c_t1)

sec = sec_t1-sec_t2
sleep(sec)
system('play -nq -t alsa synth {} sine {}'.format(60, 3000))