import wolframalpha

inp= input("Question: ")

app_id = "T7HE4Q-WU34V7UEQQ"
client = wolframalpha.Client(app_id)

res = client.query(inp)
try:
    print(next(res.results).text)
except StopIteration:
    print("No more suggesstions.")
