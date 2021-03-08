import json
f = open("last_vector_7th.txt")

Lines = f.readlines()

here = []

i = 0
while i < len(Lines):
    vector = json.loads(Lines[i])
    rank = int(Lines[i + 1])
    here.append(
        {"vector": vector["vector"], "results": vector["results"], "rank": rank + 12})
    i += 2

f.close()

f = open("last_vector_8th.txt")

Lines = f.readlines()

i = 0
while i < len(Lines):
    vector = json.loads(Lines[i])
    rank = int(Lines[i + 1])
    here.append(
        {"vector": vector["vector"], "results": vector["results"], "rank": rank})
    i += 2

f.close()

here = sorted(here, key=lambda i: i["rank"])

lmao = []

for i in range(len(here)):
    x = here[i]
    if max(x["results"][0], x["results"][1])/1e11 < 3 and x["rank"] <= 60:
        lmao.append(x)

lmao = sorted(lmao, key=lambda i: abs(i["results"][0] - i["results"][1]))

for i in range(len(lmao)):
    x = lmao[i]
    # print(i, x["results"][0]/1e11, x["results"][1]/1e11, x["rank"])

selected = [0, 1, 2, 3, 4, 5, 11, 12, 13, 15]

for i in selected:
    print(lmao[i]["vector"], ",")
