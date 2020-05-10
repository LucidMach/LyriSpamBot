"""
This Code Is Written by NukeSuraj
"""

import pyautogui as pg
import time    

# Name Of The Person to Be .....
uname = ""      

# The Song Lyrics
song = """Light 'em up, light 'em up
Tell me where you are, tell me where you are
Summer nights, bright lights
And the shootin' stars, they break my heart
Callin' you now, but you're not pickin' up
Shadows so close if that's still enough
Light a match, light a match
Baby, in the dark, show me where you are
Oh, love
How I miss you every single day
When I see you on those streets
Oh, love
Tell me there's a river I can swim that will bring you back to me
'Cause I don't know how to love someone else
I don't know how to forget your face
No, love
God, I miss you every single day and now you're so far away
So far away
It's breakin' me, losin' you
We were far from perfect
But we were worth it
Too many fights, and we cried
But never said we're sorry
Stop sayin' you love me
You're callin' me now, but I can't pick up
Your shadow's still close, and I'm still in love
The summer's over now
But somehow it still breaks my heart
We could have had this talk
Oh
Oh, love
How I miss you every single day
When I see you on those streets
Oh, love
Tell me there's a river I can swim that will bring you back to me
'Cause I don't know how to love someone else
I don't know how to forget your face
No, love
God, I miss you every single day and now you're so far away
So far away
So far away, oh
So far away
So far away
Oh, love
How I miss you every single day
When I see you on those streets
Oh, love
Tell me there's a river I can swim that will bring you back to me
'Cause I don't know how to love someone else
I don't know how to forget your face
Oh, love
God, I miss you every single day when you're so far away"""

t = 0.5

wa = "https://web.whatsapp.com/"
ig = "https://www.instagram.com/"

def urlhandler(url):
    pg.click(x=235,y=76)
    time.sleep(t)
    pg.typewrite(url)
    time.sleep(t)
    pg.hotkey('enter')
    time.sleep(10)
    pg.click(x=116,y=228)
    time.sleep(t)
    pg.typewrite(uname)
    time.sleep(t)
    pg.click(x=135,y=412)
    time.sleep(t)
    pg.click(x=945,y=913)
    time.sleep(t)
    pg.typewrite(song)
    pg.hotkey('enter')

pg.hotkey('win','2')
time.sleep(1)
pg.hotkey('ctrl','t')
time.sleep(1)
urlhandler(wa)
