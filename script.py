import pandas
import numpy
import json

DekuList = ["Deku Tree Map Chest", "Deku Tree Slingshot Room Side Chest", "Deku Tree Slingshot Chest", "Deku Tree Compass Chest", "Deku Tree Compass Room Side Chest", "Deku Tree Basement Chest", "Deku Tree Queen Gohma Heart"]
JabuList = ["Jabu Jabus Belly Boomerang Chest", "Jabu Jabus Belly Map Chest", "Jabu Jabus Belly Compass Chest", "Jabu Jabus Belly Barinade Heart"]
ForestList = ["Forest Temple First Room Chest", "Forest Temple First Stalfos Chest", "Forest Temple Raised Island Courtyard Chest", "Forest Temple Map Chest", "Forest Temple Well Chest", "Forest Temple Eye Switch Chest", "Forest Temple Boss Key Chest", "Forest Temple Floormaster Chest", "Forest Temple Red Poe Chest", "Forest Temple Bow Chest", "Forest Temple Blue Poe Chest", "Forest Temple Falling Ceiling Room Chest", "Forest Temple Basement Chest", "Forest Temple Phantom Ganon Heart"]
FireList = ["Fire Temple Near Boss Chest", "Fire Temple Flare Dancer Chest", "Fire Temple Boss Key Chest", "Fire Temple Big Lava Room Lower Open Door Chest", "Fire Temple Big Lava Room Blocked Door Chest", "Fire Temple Boulder Maze Lower Chest", "Fire Temple Boulder Maze Side Room Chest", "Fire Temple Map Chest", "Fire Temple Boulder Maze Shortcut Chest", "Fire Temple Boulder Maze Upper Chest", "Fire Temple Scarecrow Chest","Fire Temple Compass Chest", "Fire Temple Megaton Hammer Chest", "Fire Temple Highest Goron Chest", "Fire Temple Volvagia Heart"]
WaterList = ["Water Temple Compass Chest", "Water Temple Map Chest", "Water Temple Cracked Wall Chest", "Water Temple Torches Chest", "Water Temple Boss Key Chest", "Water Temple Central Pillar Chest", "Water Temple Central Bow Target Chest", "Water Temple Longshot Chest", "Water Temple River Chest", "Water Temple Dragon Chest", "Water Temple Morpha Heart"]
ShadowList = ["Shadow Temple Map Chest", "Shadow Temple Hover Boots Chest", "Shadow Temple Compass Chest", "Shadow Temple Early Silver Rupee Chest", "Shadow Temple Invisible Blades Visible Chest", "Shadow Temple Invisible Blades Invisible Chest", "Shadow Temple Falling Spikes Lower Chest", "Shadow Temple Falling Spikes Upper Chest", "Shadow Temple Falling Spikes Switch Chest", "Shadow Temple Invisible Spikes Chest","Shadow Temple Freestanding Key", "Shadow Temple Wind Hint Chest", "Shadow Temple After Wind Enemy Chest", "Shadow Temple After Wind Hidden Chest", "Shadow Temple Spike Walls Left Chest", "Shadow Temple Boss Key Chest", "Shadow Temple Invisible Floormaster Chest", "Shadow Temple Bongo Bongo Heart"]
SpiritList = ["Spirit Temple Child Bridge Chest", "Spirit Temple Child Early Torches Chest", "Spirit Temple Child Climb North Chest", "Spirit Temple Child Climb East Chest", "Spirit Temple Map Chest", "Spirit Temple Sun Block Room Chest", "Spirit Temple Silver Gauntlets Chest", "Spirit Temple Compass Chest", "Spirit Temple Early Adult Right Chest", "Spirit Temple First Mirror Left Chest", "Spirit Temple First Mirror Right Chest", "Spirit Temple Statue Room Northeast Chest", "Spirit Temple Statue Room Hand Chest", "Spirit Temple Near Four Armos Chest", "Spirit Temple Hallway Right Invisible Chest", "Spirit Temple Hallway Left Invisible Chest", "Spirit Temple Mirror Shield Chest", "Spirit Temple Boss Key Chest", "Spirit Temple Topmost Chest", "Spirit Temple Twinrova Heart"]



def get_key(dict, val):
    for key, value in dict.items():
        if val == value:
            return key
    return 0

debugPrints = False
logFile = open("seed.json")
log = json.load(logFile)
score = 0

#Check For Skulltulas
if("Kak 30 Gold Skulltula Reward" in log[":woth_locations"].keys()):
    score += 15
    if debugPrints:
        print("30 Skulls Required!")

if("Kak 40 Gold Skulltula Reward" in log[":woth_locations"].keys()):
    score += 20
    if debugPrints:
        print("40 Skulls Required!")

if("Kak 50 Gold Skulltula Reward" in log[":woth_locations"].keys()):
    score += 25
    if debugPrints:
        print("50 Skulls Required!")

#Check For ZL Location
zl = get_key(log['locations'], "Zeldas Lullaby")

if zl == "Song from Impa":
    score += 0
    if debugPrints:
        print("ZL in Good Location")
elif zl == "Song from Malon":
    score += 0
    if debugPrints:
        print("ZL in Good Location")
elif zl == "Song from Saria":
    score += 0
    if debugPrints:
        print("ZL in Good Location")
elif zl == "Song from Ocarina of Time":
    score += 25
    if debugPrints:
        print("ZL in Bad Location")
elif zl == "Song from Windmill":
    score += 0
    if debugPrints:
        print("ZL in Good Location")
elif zl == "Sheik in Forest":
    score += 5
    if debugPrints:
        print("ZL in sub-par Location")
elif zl == "Sheik in Crater":
    score += 5
    if debugPrints:
        print("ZL in sub-par Location")
elif zl == "Sheik at Colossus":
    score += 10
    if debugPrints:
        print("ZL in sub-par Location")
elif zl == "Sheik in Kakariko":
    score += 20
    if debugPrints:
        print("ZL in Bad Location")
elif zl == "Sheik at Temple":
    score += 15
    if debugPrints:
        print("ZL in Bad Location")
else:
    print("ZL Not Detected!")

#Get OOT Song
oot = log['locations']["Song from Ocarina of Time"]
obtuse = True
if oot == "Zeldas Lullaby":
    score += 25
    obtuse = False
    if debugPrints:
        print("OOT Forces AD Always.")
elif oot == "Eponas Song":
    score += 10
    if debugPrints:
        print("OOT Forces AD Occasionally.")
elif oot == "Sarias Song":
    score += 5
    if debugPrints:
        print("OOT Forces AD Rarely.")
elif oot == "Suns Song":
    score += 5
    if debugPrints:
        print("OOT Forces AD Rarely.")
elif oot == "Song of Time":
    score += 5
    if debugPrints:
        print("OOT Forces AD Rarely.")
elif oot == "Song of Storms":
    score += 10
    if debugPrints:
        print("OOT Forces AD Occasionally.")
elif oot == "Minuet of Forest":
    score += 0
    if debugPrints:
        print("OOT Forces AD Never.")
elif oot == "Bolero of Fire":
    score += 0
    if debugPrints:
        print("OOT Forces AD Never.")
elif oot == "Serenade of Water":
    score += 0
    if debugPrints:
        print("OOT Forces AD Never.")
elif oot == "Requiem of Spirit":
    score += 5
    if debugPrints:
        print("OOT Forces AD Rarely.")
elif oot == "Nocturne of Shadow":
    score += 20
    obtuse = False
    if debugPrints:
        print("OOT Forces AD Always.")
elif oot == "Prelude of Light":
    score += 0
    if debugPrints:
        print("OOT Forces AD Never.")
else:
    print("OOT Song Not Detected!")

#Check Hookshot Sphere
i = 1
while i > 0:
    hook = get_key(log[':playthrough'][str(i)], "Progressive Hookshot")
    if hook:
        i = -1
    else:
        i += 1
        if i == 7:
            if debugPrints:
                print("Bad Hookshot!")
            score += 15
            i = -1

#Check Hookshot Sphere
i = 1
while i > 0:
    hook = get_key(log[':playthrough'][str(i)], "Bomb Bag")
    if hook:
        i = -1
    else:
        i += 1
        if i == 5:
            if debugPrints:
                print("Bad Bomb Bag!")
            score += 10
            i = -1

if "Song from Ocarina of Time" in log[":woth_locations"].keys():
    if debugPrints:
        print("AD Seed")
    score += 20
    if obtuse:
        if debugPrints:
            print("Obtuse AD")
        score += 20
else:
    if "Medallion" not in log["locations"]["Queen Gohma"]:
        for location in DekuList:
            if location in log[":woth_locations"].keys():
                if debugPrints:
                    print("Item in Stone Deku!")
                score += 10

    if "Medallion" not in log["locations"]["Barinade"]:
        for location in JabuList:
            if location in log[":woth_locations"].keys():
                if debugPrints:
                    print("Item in Stone Jabu!")
                score += 20

    if "Medallion" not in log["locations"]["Phantom Ganon"]:
        for location in ForestList:
            if location in log[":woth_locations"].keys():
                if debugPrints:
                    print("Item in Stone Forest!")
                score += 15

    if "Medallion" not in log["locations"]["Volvagia"]:
        for location in FireList:
            if location in log[":woth_locations"].keys():
                if debugPrints:
                    print("Item in Stone Fire!")
                score += 20

    if "Medallion" not in log["locations"]["Morpha"]:
        for location in WaterList:
            if location in log[":woth_locations"].keys():
                if debugPrints:
                    print("Item in Stone Water!")
                score += 20

    if "Medallion" not in log["locations"]["Bongo Bongo"]:
        for location in ShadowList:
            if location in log[":woth_locations"].keys():
                if debugPrints:
                    print("Item in Stone Shadow!")
                score += 20

    if "Medallion" not in log["locations"]["Twinrova"]:
        for location in SpiritList:
            if location in log[":woth_locations"].keys():
                if debugPrints:
                    print("Item in Stone Spirit!")
                score += 15


print("")
print("Seed Score: " + str(score))