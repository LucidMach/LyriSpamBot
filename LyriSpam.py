"""
author: @NukeSuraj
"""

import pyautogui as pg 
import time
import string


# Names(as saved in whatsapp) Of The People to Be .....
uname = ["Karthik","Raki","Varun"]    

# The Song Lyrics
#   sname = input("Enter Lyrics File:") #RapGod.txt/SoFarAway.txt for now or you can create your own text file
driver = webdriver.Chrome()
sname=input("Enter the song name:")
driver.get(f"http://google.com/?#q={sname} lyrics")
song = driver.find_element_by_class_name("Oh5wg").text


"""with open(sname,"r") as f:
    song = f.readlines()"""

t = 0.5

wa = "https://web.whatsapp.com/"

def urlhandler(url):
    pg.click(x=235,y=76) 
    time.sleep(t)
    pg.typewrite(url)
    time.sleep(t)
    pg.hotkey('enter')
    time.sleep(10)
    for name in uname:
        pg.click(x=116,y=228)
        time.sleep(t)
        pg.typewrite(name)
        time.sleep(t)
        pg.click(x=135,y=412)
        time.sleep(t)
        pg.click(x=804,y=974)
        for line in song:
            pg.typewrite(line)
            pg.hotkey('enter')
            #time.sleep(t)

pg.hotkey('win','2')
time.sleep(1)
pg.hotkey('ctrl','t')
time.sleep(1)
urlhandler(wa)
