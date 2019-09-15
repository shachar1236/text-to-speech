import os

def speek(text):
    with open("talk.vbs", "w") as f:
        f.write("Dim sapi")
        f.write("\n")
        f.write("Set sapi=CreateObject(\"sapi.spvoice\")")
        f.write("\n")
        f.write("sapi.Speak "+'"'+text+'"')
    os.startfile("talk.vbs")

speek("something")
