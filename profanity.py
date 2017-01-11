import urllib
def read_text():
    quotes = open("C:\Users\Niharika - PC\Desktop\movie quotes.txt")
    content = quotes.read()
    quotes.close()
    checkProfanity(content)

def checkProfanity(checkContent):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+checkContent)
    output = connection.read()
    if "true" in  output:
        print("Profanity Alert!")
    elif "false" in output:
        print("Profanity Free!")
    else:
        print("Could not scan the document properly.")
    connection.close()
    
read_text()
