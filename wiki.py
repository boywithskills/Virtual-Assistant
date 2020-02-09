import wikipedia

while(True):
    inputs = input("Questions: ")
    print (str(wikipedia.summary(inputs)))
