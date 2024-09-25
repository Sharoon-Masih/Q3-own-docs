# first install pyjoke module usng pip
# pip install pyjokes

import pyjokes # imported the pyjoke module/package

joke = pyjokes.get_joke()

print(joke)

# now to execute it use 'python module-pip.py'

# ---------------------------------
# practice qs

# Q3
# first installing external module using pip and then import it.

import pyttsx3; # basically yeh be ek external package hai jokay basically use hota hai for converting text to speech.

engine = pyttsx3.init() #here initialize it.
engine.say("Hello, jane sharoon") # .say ma text likhega jo speech ma convert  krna hai.
engine.runAndWait() # then execute it.


