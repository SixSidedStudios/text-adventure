#Text-adventure prototype 1.0

print 'Your eyes slowly open... an old man stands over you.'
print '"Why hello my friend, what might your name be?"'
name = raw_input('Enter your name:')
print '"Ah,',name
print 'a good name... there was a hero named ',name,' a long time ago."'
print 'The old man sits you up.'
print 'You are in a clay hut, and there are shelves on the walls that are filled with different colored potions.'
print '"I found you in your burnt farm house, afteryou got raided by those nasty'
print ' barbaric thieves."'

def question1():
    print '"Well, I\'m very sorry... how do you feel?'

def remember():
    rememberance = raw_input('Do you remember this? Y/N:')
    if rememberance == 'y':
        question1()
    elif rememberance == 'n':
        print '"Ah, well... the riders torched your barn and killed your livestock... then they plundered your house."'
        question1()
    else:
        print '"What was that you said?"'
        remember()
remember()
