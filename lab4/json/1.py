import json

with open("sample-data.json", "r") as openfile:
    data = json.load(openfile)

s = """Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
"""

for i in data["imdata"]:
    s += i["l1PhysIf"]["attributes"]["dn"] + "\n"
    #s += "\n"

print(s)