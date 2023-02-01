import json
print("here")
with open("C:/Users/aloes/OneDrive/Code/Name Theory/names.json") as file:
    data = json.load(file)

print(data)
print("\n")

print(data["C"])
print("\n")

print(data["C"].keys())
print("\n")

print(data["C"]["Christian"])
print("\n")

currentVal = ''
for key, val in data["C"].items():
    print(key, val)
    
    if currentVal == '' or val != None:
        currentVal = val

    if val == None and key == "Carol":
        print("Reader sees: ", key, currentVal)
        #currentVal = ''


