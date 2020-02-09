import wikipedia
import wolframalpha

while(True):
    inp = input("Your Question: ")

    try:
        #wolframalpha
            app_id = "T7HE4Q-WU34V7UEQQ"
            client = wolframalpha.Client(app_id)
            res = client.query(inp)
            print (next(res.results).text)

    except StopIteration:
        #wikipedia
        print (str(wikipedia.summary(inp,sentences=4)))
