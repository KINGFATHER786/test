import os,platform
os.system('git pull')
 
ass=platform.architecture()[0]
if ass=="32bit":
    print("wait for next update")
elif ass=="64bit":
    __import__("mani").main()