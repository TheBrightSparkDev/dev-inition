import json

f = open("dictionary.json")

dictionary = json.load(f)

for words in dictionary:
    if len(words) == 4:
        if "-" not in words:
            definition = dictionary[words]
            print(f"'{words}':'{dictionary}',")


f.close()
