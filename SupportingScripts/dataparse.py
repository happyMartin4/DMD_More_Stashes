import json
import re
from . import filehandle
'''
stat term to real term:
bban = banishes (i = i bans)
hok = % chance to heal on kill (i = i% to heal 1 on kill)
e = evasion (i = i evasion)
msp = % less attack movement penalty (i = .9% less?)
pdr% = increased pickup drop rate (i = 3%)


item rarity 1, 2, 3, 4 = common, rare, epic, mythic
types:
    8 = relic
    4 = waist/belt
    9 = jewel
    7 = amulet
    1 = head
    2 = torso
    3 = glove
    5 = boot 
    0 = weapon

'''
def parseStash(stash: str) -> dict:
    output = ''
    for letter in stash:
        if letter != '\\':
            output = output+letter
    output = output.replace('{"Width":5,"Height":8,"Items":[', '')
    brackets = 0
    items = []
    item = ''
    for letter in output:
        if letter == '{':
            brackets += 1
        elif letter == '}':
            brackets -= 1
            if brackets == 0:
                items.append(item)
                item = ''
        elif brackets != 0:
            item = item + letter
    outDict = {}
    outDict['stash'] = {}
    outDict['stats'] = {}
    #for item in items:
        #print(item)

    for i, item in enumerate(items):
        codeSearch = re.search(r'Code":"([0-9a-zA-Z\-]+)"', item)
        if codeSearch:
            code = codeSearch.group(1)
        else:
            code = ''
        
        typeSearch = re.search(r'Type":([0-9]+)', item)
        if typeSearch:
            type = typeSearch.group(1)
        else:
            type = ''
        
        raritySearch = re.search(r'Rarity":([0-9]+)', item)
        if raritySearch:
            rarity = raritySearch.group(1)
        else:
            rarity = ''

        tierSearch = re.search(r'TierIndex":([0-9]+)', item)
        if tierSearch:
            tier = tierSearch.group(1)
        else:
            tier = ''

        uniqueSearch = re.search(r'IsUnique":([a-z]+)', item)
        if uniqueSearch:
            if uniqueSearch.group(1) == 'true':
                unique = 'true'
            elif uniqueSearch.group(1) == 'false':
                unique = 'false'
            else:
                unique = ''
        else:
            unique = ''

        subtypeCodeSearch = re.search(r'SubtypeCode":"([a-zA-Z0-9_]+)"', item)
        if subtypeCodeSearch:
            subtype = subtypeCodeSearch.group(1)
        else:
            subtype = ''

        iconVarianceSearch = re.search(r'IconVariant":"([a-zA-Z0-9_]+)"', item)
        if iconVarianceSearch:
            iconvariant = iconVarianceSearch.group(1)
        else:
            iconvariant = ''
        
        dropVarianceSearch = re.search(r'DropVariant":"([a-zA-Z0-9_]+)"', item)
        if dropVarianceSearch:
            dropvariant = dropVarianceSearch.group(1)
        else:
            dropvariant = ''

        affixSearch = re.search(r'Affixes":\[([^\]]+)', item)
        if affixSearch:
            affixesPreprocessed = affixSearch.group(1)
        else:
            affixesPreprocessed = ''

        codes = re.findall(r'"Code":"([a-zA-Z0-9_%]+)"', affixesPreprocessed)
        levels = re.findall(r'"Levels":([0-9]+)', affixesPreprocessed)
        affixes = dict(zip(codes, levels))

        ownedByPlayerSearch = re.search(r'WasOwnedByPlayer":([a-zA-Z]+)', item)
        if ownedByPlayerSearch:
            owned = ownedByPlayerSearch.group(1)
        else:
            owned = ''

        boundSearch = re.search(r'BoundToCharacterCode":"([a-zA-Z0-9]+)"', item)
        if boundSearch:
            bound = boundSearch.group(1)
        else:
            bound = ''

        outDict['stash'][i] = {'code' : code, 'type' : type, 'rarity' : rarity, 'tier' : tier, 'unique' : unique, 'subtype' : subtype, 'iconvariant' : iconvariant,
                      'dropvariant' : dropvariant, 'affixes' : affixes, 'owned' : owned, 'bound' : bound }
        
        filled= empty= rarityCommon= rarityRare= rarityEpic= rarityMythic= numWeapon= numHead= numTorso= numGlove= numWaist= numBoot= numRings= numAmulet= numRelic= numJewel= 0

        for key, item in outDict['stash'].items():
            #print(f'{key}: {item}\n\n')
            #storage space used
            if item['code'] == '':
                empty += 1
            else:
                filled += 1
            #stats for rarity
            if item['rarity'] == '4':
                rarityMythic += 1
            elif item['rarity'] == '3':
                rarityEpic += 1
            elif item['rarity'] == '2':
                rarityRare += 1
            elif item['rarity'] == '1':
                rarityCommon += 1


            #item types:
            if item['type'] == '0' and item['code'] != '':
                numWeapon += 1
            elif item['type'] == '1':
                numHead += 1
            elif item['type'] == '2':
                numTorso += 1
            elif item['type'] == '3':
                numGlove += 1
            elif item['type'] == '4':
                numWaist += 1
            elif item['type'] == '5':
                numBoot += 1
            elif item['type'] == '6':
                numRings += 1
            elif item['type'] == '7':
                numAmulet += 1
            elif item['type'] == '8':
                numRelic += 1
            elif item['type'] == '9':
                numJewel += 1
            #storage space used
            outDict['stats']['filled'] = filled
            outDict['stats']['empty'] = empty
            #rarity of items
            outDict['stats']['rarityMythic'] = rarityMythic
            outDict['stats']['rarityEpic'] = rarityEpic
            outDict['stats']['rarityRare'] = rarityRare
            outDict['stats']['rarityCommon'] = rarityCommon
            #item types
            outDict['stats']['weapons'] = numWeapon
            outDict['stats']['heads'] = numHead
            outDict['stats']['torsos'] = numTorso
            outDict['stats']['gloves'] = numGlove
            outDict['stats']['waists'] = numWaist
            outDict['stats']['boots'] = numBoot
            outDict['stats']['rings'] = numRings
            outDict['stats']['amulets'] = numAmulet
            outDict['stats']['relics'] = numRelic
            outDict['stats']['jewels'] = numJewel
            
        #print(f'filled: {outDict['stats']['filled']}\nempty: {outDict["stats"]['empty']}\nMythic: {outDict["stats"]['rarityMythic']}\n')
    return outDict

    
def splitItems(*args):
    output=[]
    for arg in args:
        output.append(arg)
    return output


def main():
    saveManager = filehandle.FileHandler()
    stashDict = parseStash(saveManager.getActiveListItem(0))
    print(stashDict)
    for key in stashDict:
        print(f'key: {key} == {stashDict[key]}')

if __name__ == '__main__':
    main()
