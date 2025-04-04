
#COREY GOES AT TOWN

import sys
import time

def writeln(_str):
    print(_str)
def cin(_str):
    return input(_str + ' ')
def zit():
    sys.exit(0)
writeln('''
Bowling alley: you go bowling!
Cinema: you watch a show!

''')
ayn = cin('Where would you like to go as Corey? ')
if ayn.lower() == 'b':
    writeln('''
You, Corey, enjoy shots at an alley to hit white rectangles
You do really well
    ''')

elif ayn.lower() == 'c':
    writeln('''
You, Corey, watch a great show un' take tons uh notes
    ''')


szstr = cin('Did you do what you wanted today?')
if szstr.upper() =='Y':
    zit()
    

writeln('''
You, Corey, go to bed und shut it
''')
