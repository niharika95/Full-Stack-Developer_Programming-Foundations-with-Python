import webbrowser
import time

count = 1
while (count <= 3):
    time.sleep(7200)
    print "The program started at " + time.ctime()
    webbrowser.open("https://www.youtube.com/watch?v=Lco6wvYNYD8")
    count = count + 1



