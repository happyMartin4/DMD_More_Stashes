import json
import re
from . import filehandle

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
    #for item in items:
        #print(item)

    for i, item in enumerate(items):
        codeSearch = re.search(r'Code":"([0-9a-zA-Z\-]+)"', item)
        if codeSearch:
            code = codeSearch.group(1)
            outDict[code] = {'value' : 'test'}
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

        outDict[i] = {'code' : code, 'type' : type, 'rarity' : rarity, 'tier' : tier, 'unique' : unique, 'subtype' : subtype, 'iconvariant' : iconvariant,
                      'dropvariant' : dropvariant, 'affixes' : affixes, 'owned' : owned, 'bound' : bound }
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
