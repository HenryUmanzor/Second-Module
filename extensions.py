import re
Userinput= input("").strip()
def extentions():
    if re.search(r"^.+\.gif$",Userinput):
        print("image/gif")
    elif re.search(r"^.+\.jpg$",Userinput):
        print("image/jpeg")
    elif re.search(r"^.+\.jpeg$",Userinput):
        print("image/jpeg")
    elif re.search(r"^.+\.png$",Userinput):
        print("image/png")
    elif re.search(r"^.+\.pdf$",Userinput):
        print("application/pdf")
    elif re.search(r"^.+\.txt$",Userinput):
        print("text/plain")
    elif re.search(r"^.+\.zip$",Userinput):
        print("application/zip (application/x-zip-compressed)")
    else:
        print("application/octet-stream")

extentions()