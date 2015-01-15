#Text-adventure prototype 1.0
import time
import multichoice
from multichoice import *
from time import *

print 'Your eyes slowly open... an old man stands over you.'
print '"Why hello my friend, what might your name be?"'
name = raw_input('Enter your name:')
print '"Ah,',name
print 'a good name... there was a hero named',name,'a long time ago."'
print 'The old man sits you up.'
print 'You are in a clay hut, and there are shelves on the walls that are filled with'
print 'different colored potions.'
print '"I found you in your burnt farm house, afteryou got raided by those nasty'
print ' barbaric thieves."'

b_remember()
if b_feel() == True:
    print 'yay'
elif b_feel() == False:
    print 'ah'
