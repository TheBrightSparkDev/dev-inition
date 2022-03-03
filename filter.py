import json

f = open("dictionary.json")

dictionary = json.load(f)
i = 0
for words in dictionary:
    if len(words) == 8:
        if "-" not in words:
            i = i + 1
            print(f"'{i}':'{words}',")

f.close()
