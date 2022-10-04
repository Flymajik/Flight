import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from mahadif import Flight X
 
        Flight X()
 
 
 
elif bit == "32bit":
 
        from mahadif32 import Flight X
 
 
        Flight X()
