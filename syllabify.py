#!/usr/local/bin/python3

import pandas
import os
from syllabipy.sonoripy import SonoriPy
from AppKit import NSPasteboard, NSStringPboardType

pb = NSPasteboard.generalPasteboard()
pbstring = pb.stringForType_(NSStringPboardType)

toConvert = pbstring.lower()

wordSplit = toConvert.split(' ')
x=''
for i in range(len(wordSplit)):
    y = SonoriPy(wordSplit[i])
    x+="-".join(y) + ' '

print(x)
