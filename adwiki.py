import wikipedia

while(True):
    inp = input("Questions: ")

    print (str(wikipedia.summary(inp,sentences=4)))
