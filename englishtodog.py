
#DOGS GET TRANSLATED

import sys
import time
import re

def writeln(_str):
    print(_str)
def cin(_str):
    return input(_str + ' ')
def zit():
    sys.exit(0)
def slee(_n):
    time.sleep(_n)

english = cin('What is des Englai?')
arenglish = english.split(' ')
for i in arenglish:
    szsz = i.lower()
    if re.compile('v').match(szsz):
        writeln('wooooof')
    elif re.compile('p').match(szsz):
        writeln('bark!')
    elif re.compile('x').match(szsz):
        writeln('zzzwoof')
    else:
        writeln('woof')
    slee(6)
