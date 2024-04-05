import re as reg
import decompress
import os
from pathlib import Path


class FileHandler:
    EMPTYSTASH = r"{\\\"Width\\\":5,\\\"Height\\\":8,\\\"Items\\\":[{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"},{\\\"Code\\\":\\\"\\\",\\\"Type\\\":0,\\\"Rarity\\\":0,\\\"TierIndex\\\":0,\\\"IsUnique\\\":false,\\\"SubtypeCode\\\":\\\"\\\",\\\"IconVariant\\\":\\\"\\\",\\\"DropVariant\\\":\\\"\\\",\\\"Affixes\\\":[],\\\"WasOwnedByPlayer\\\":false,\\\"BoundToCharacterCode\\\":\\\"\\\"}]}"
    NUM_OF_ACTIVE_STASHES = 3
    def __str__(self):
        return f'reading save from: {self.inputPath}\nsaving file to: {self.outputPath}\ncurrently looking at active stash \
        {self.activeStash} + 1\ncurrently looking at inactive stash: {self.inactiveStash} + 1'

    @property
    def activeStash(self):
        return self._activeStash

    @property
    def inactiveStash(self):
        return self._inactiveStash

    @property
    def rawActive(self):
        return self._rawActive

    @property
    def rawInactive(self):
        return self._rawInactive

    @activeStash.setter
    def activeStash(self, newActive):
        self._activeStash = newActive
        self.rawActive = self.activeStash

    @inactiveStash.setter
    def inactiveStash(self, newInactive):
        self._inactiveStash = newInactive
        self.rawInactive = self.inactiveStash

    @rawActive.setter
    def rawActive(self, newRawAct):
        self._rawActive = self.activeStashList[newRawAct]

    @rawInactive.setter
    def rawInactive(self, newRawInact):
        output = ''
        try:
            with open(f'{self.outputPath}\\Stashes\\stash_{newRawInact}', 'r', encoding='utf-8') as file:
                output = file.read()
        except Exception as e:
            print(f'Error reading from {newRawInact} while setting inactiveStash: {str(e)}')
            output = self.EMPTYSTASH
        self._rawInactive = output
    
    def getActiveListItem(self, index):
        return self.activeStashList[index]
    
    def setActiveListItem(self, index, replacementRawStash):
        if len(activeStashList) > index:
            self.activeStashList[index] = replacementRawStash

    def setActiveList(self, replacementList):
        self.activeStashList = []
        if len(replacementList)>0:
            for stash in replacementList:
                self.activeStashList.append(stash)
        else:
            self.activeStashList = []


    """
    Decompresses the file into a readable format.
    Seems to be working.
    """
    def readAndDecompress(self):
        """Reads, decompresses the input file, and returns the decompressed data."""
        return decompress.decompressFile(self.inputPath)

    def writeToFile(self, data):
        """Writes the given data to the output file."""
        try:
            with open(self.outputPath, 'w', encoding='utf-8') as file:
                file.write(data)
            return f"Data written to '{self.outputPath}' successfully."
        except Exception as e:
            return f"Error writing to '{self.outputPath}': {str(e)}"
    
    def swap(self):
        storage = self.getActiveListItem(self.activeStash)
        self.setActiveListItem(self.activeStash, self.rawInactive) 
        self.rawInactive = storage             

    

    """
    writes out to a file to store a stash.
    working right now. 
    """
    def export(self, fileIndex=1):
        stashDirectory = os.path.join(self.outputPath, "Stashes")
        os.makedirs(stashDirectory, exist_ok=True)
        pathTo = os.path.join(stashDirectory, f'stash_{fileIndex}')
        while os.path.exists(pathTo):
            fileIndex += 1
            pathTo = os.path.join(stashDirectory, f'stash_{fileIndex}')
    
        try:
            with open(pathTo, 'w', encoding='utf-8') as file:
                file.write(self.rawActive)
        except Exception as e:
            print(f'Error reading from {pathTo}: {str(e)}')
            return 1
        return (fileIndex-1)
    
    def exportOverwrite(self):
        stashDirectory = os.path.join(self.outputPath, "Stashes")
        os.makedirs(stashDirectory, exist_ok=True)
        pathTo = os.path.join(stashDirectory, f'Stash_{(self.currentInactive+1)}')
        try:
            with open(pathTo, 'w', encoding='utf-8') as file:
                file.write(self.rawInactive)
        except Exception as e:
            print(f'Error reading from {newRawInact}: {str(e)}')
            return 1
        return (fileIndex-1)
                    
    def delete(self):
        """Delete External Stash at self.inactive"""   
        return

    def backup(self):
        backupDirectory = os.path.join(self.outputPath, "Backups")
        os.makedirs(backupDirectory, exist_ok=True)
        fileIndex = 1
        saveHolder = ''
        pathTo = os.path.join(backupDirectory, f'Backup_{fileIndex}.sav')
        while os.path.exists(pathTo):
            fileIndex += 1
            pathTo = os.path.join(backupDirectory, f'Backup_{fileIndex}.sav')
        with open(self.inputPath, 'rb') as file:
            saveHolder = file.read()
        with open(pathTo, 'wb') as file:
            file.write(saveHolder)
        
                    
    def save(self, savePath=None):
        if savePath==None:
            savePath = self.inputPath
        self.backup()
        rawSave = self.readAndDecompress()
        currentStashes = self.parseStashes(rawSave) #returns an array
        stashMeta = {}
        for i, stash in enumerate(currentStashes):
            #Compare to the list of what we have replaced with so we can skip reccurences.
            print(f"Replacement {i}: \n"+'---'*60 + f'\n{self.activeStashList[i]}'+'---'*60)
            if self.activeStashList[i] in stashMeta:
                stashMeta[str(self.activeStashList[i])] += 1
            else:
                stashMeta[str(self.activeStashList[i])] = 1
            rawSave = self.replaceNth(stashMeta[self.activeStashList[i]], rawSave, stash, self.activeStashList[i])
            
        decompress.recompress(rawSave, savePath)

    
    def replaceNth(self, n, text, old, new):
        parts = text.split(old, n + 1)
        if len(parts) > n:
            return old.join(parts[:-1]) + new + old.join(parts[-1:])
        print(f'error, can\'t find {n}th occurrence. less than {n} occurrences in passed text.')
        return text #output old if n > occurrences


    """
    takes raw string of save and returns the list of stashes in it.
    seems to be working right now.
    """
    def parseStashes(self, rawSave):
        sentinel = r'"StashJson\":\"{\\\"Pages\\\":'
        position = rawSave.find(sentinel)
        print(position)
        relevantSave = rawSave[position + len(sentinel):]
        if position == -1:
            return []  # Sentinel string not found; return empty list.
        brackets = 0
        braces = 0
        remember = 0
        output = []
        for i, letter in enumerate(relevantSave):
            #print(letter, end='')
            if letter == '[':
                braces += 1
                #print('[')
            elif letter == ']':
                braces -= 1
                #print(']')
                if braces == 0:
                    break
            elif letter == '{':
                #print('{')
                if brackets == 0:    
                    remember = i
                brackets += 1
            elif letter == '}':
                #print('}')
                brackets -= 1
                if brackets == 0:
                    output.append(relevantSave[remember:i+1])
        return output
            
    def __init__(self, inputPath=Path.home() / 'AppData\\LocalLow\\Realm Archive\\Death Must Die\\Saves\\Slot_0.sav' 
    , outputPath=Path.home() / 'AppData\\LocalLow\\Realm Archive\\Death Must Die\\Saves\\', activeStash=0, inactiveStash=0):
        self.inputPath = inputPath
        self.outputPath = outputPath
        self.backup()
        try:
            rawSave = self.readAndDecompress()
            self.setActiveList(self.parseStashes(rawSave))
        except Exception as e:
            self.setActiveList([])
            print(f"Error reading file or parsing stash data: {str(e)}")
        self.activeStash = activeStash
        self.inactiveStash = inactiveStash
        self.rawInactive = self.inactiveStash
        self.rawActive = self.activeStash


def main():
    print('all good.')
    saveManager = FileHandler()
    #print(saveManager.parseStashes)
    """
    for i in range(3):
        saveManager.activeStash = i
        saveManager.export()

    i = 1
    #for i in range(3):
    saveManager.inactiveStash=i
    saveManager.activeStashList[i] = saveManager.rawInactive
    saveManager.save()
    """
    print('done')

if __name__ == "__main__":
    main()