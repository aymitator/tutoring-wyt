
#COREY GOES OUTTA TOWN 

import sys
import time

def writeln(_str):
    print(_str)
def cin(_str):
    return input(_str + ' ')
def zit():
    sys.exit(0)
writeln('''
Zoo: pet animals!
Coast zoo: watch water creatures!
Beach: coast a kite!
beach Stores: get candy!
Tillamook cheese area: get cheese! try cheese!
Ortland: see big city!
seAttle: see big city!

''')
ayn = cin('Where would Corey like to go? ')
if ayn.lower() == 'z':
    writeln('''
You, Corey, get taken to Ortland zoo, te' animals were created to make sure you were good
You, Corey, at a hamburger at McDonald's
    ''')

elif ayn.lower() == 'c':
    writeln('''
You, Corey, see a bunch a great water creatures
You, Corey, get salt water candies also chocolate at store
    ''')

elif ayn.lower() == 'b':
    writeln('''
You, Corey, get to see great ocean wit' great tides
You, Corey, eat tacos at Taco Bell
    ''')

elif ayn.lower() == 's':
    writeln('''
 You, Corey, get a lot a' CHOCOLATE at store at beach   
    ''')
elif ayn.lower() == 't':
    writeln('''
You, Corey, eat a lot a' cheese
    ''')
elif ayn.lower() == 'o':
    writeln('''
You, COREY, get taken to Orland, OR where you eat a crisoint und drink brewed starbucks brew    
    ''')
elif ayn.lower() == 'a':
    writeln('''
You, Corey, get taken to Seattle und you realize it's Ortland, but t'en you're still glad    
    ''')

szstr = cin('Did you go to where you wanted to go today?')
if szstr.upper() == 'Y':
    zit()

writeln('''
You, Corey, get sent to H., J., R.
''')

szstr = cin('Did you go to where you wanted to go today?')
if szstr.upper() =='Y':
    zit()
    

writeln('''
You, Corey, go to bed und shut it
''')