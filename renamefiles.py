import os

def rename_files():
    filelist = os.listdir(r"C:\Users\Niharika - PC\Desktop\prank")    
    print (filelist)
    os.chdir(r"C:\Users\Niharika - PC\Desktop\prank")
    for filename in filelist:
        print ("Old name: " + filename)
        os.rename(filename, filename.translate(None, '0123456789'))
        print ("New name: " + filename)
        
rename_files()
