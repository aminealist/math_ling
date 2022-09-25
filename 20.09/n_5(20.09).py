from json import load


with open("Pokemon.json", mode="r") as pok:
    a = load(pok)

print(a)
