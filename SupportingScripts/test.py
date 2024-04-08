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
        return self.getActiveListItem(self.activeStash)

    @property
    def rawInactive(self):
        return self._rawInactive

    @activeStash.setter
    def activeStash(self, newActive):
        self._activeStash = newActive


    @inactiveStash.setter
    def inactiveStash(self, newInactive):
        self._inactiveStash = newInactive
        self.rawInactive = self.inactiveStash

    @rawActive.setter
    def rawActive(self, newRawAct):
        self.setActiveListItem(self.activeStash, newRawAct) 

    @rawInactive.setter
    def rawInactive(self, newRawInact):
        output = ''
        try:
            with open(f'{self.outputPath}\\Stashes\\Stash_{newRawInact+1}', 'r', encoding='utf-8') as file:
                output = file.read()
        except Exception as e:
            print(f'Error reading from {newRawInact} while setting inactiveStash: {str(e)}\nDefaulting to empty stash')
            output = self.EMPTYSTASH
        self._rawInactive = output
    
    def getActiveListItem(self, index):
        try:
            return self.activeStashList[index]
        except Exception as e:
            print(f'unable to access list item at {index}')
            raise e
    
    def setActiveListItem(self, index, replacementRawStash):
        if len(self.activeStashList) > index:
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
        #this works
        storage = self.rawInactive
        if storage == self.rawInactive:
            print('storage assignment working')
        else:
            print('storage assignment not working.')
        #print(f'Swapping this stash: \n{str(self.rawActive)[:500]}\n\nFor this one:\n{str(self.rawActive)[:500]}')
        oldactive = self.rawActive
        if oldactive != self.rawActive:
            print('storing oldactive broken')

        oldinactive = self.rawInactive
        if oldinactive != self.rawInactive:
            print("storing oldinactive broken")
        #this seems to work
        wrote = self.exportOverwrite()
        if wrote == oldactive:
            print('export of active successful.')
        else:
            print('export of active unsuccessful.')
        self.rawActive = storage
        if self.rawActive != storage:
            print('assignment from storage to rawActive broken.')
        if self.rawActive == storage:
            print('assignment of rawActive from storage successful')  
        else:
            print('assignment of rawActive from storage unsuccessful')
        self.save()
        if self.rawActive == oldinactive:
            print('the new active stash has been properly swapped in.')
        else:
            print('the new active stash has not been properly swapped in.')
            #print('!'*150)
            #print(f'old:\n{str(oldinactive)[:1500]}'+ '-'*100 + f'\nnew:\n{str(self.rawActive)[:1500]}')
            #print('!'*150)
        self.inactiveStash = self.inactiveStash
        if self.rawInactive == oldactive:
            print('the new inactive has been successfully swapped into storage.')
        else:
            print('the new inactive was not successfully swapped into storage.')
            #print('!'*150)
            #print(f'old:\n{str(oldactive)[:1500]}'+ '-'*100 + f'\nnew:\n{str(self.rawInactive)[:1500]}')
            #print('!'*150)
    

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
        self.rawActive = self.EMPTYSTASH
        #print(f'SELF.RAWACTIVE == {self.rawActive}')
        self.save()
    
        try:
            with open(pathTo, 'w', encoding='utf-8') as file:
                file.write(self.rawActive)
        except Exception as e:
            print(f'Error reading from {pathTo}: {str(e)}')
            raise e
        return (fileIndex-1)
    

    """
    Outputs current inactive stash to 
    """
    def exportOverwrite(self):
        stashDirectory = os.path.join(self.outputPath, "Stashes")
        os.makedirs(stashDirectory, exist_ok=True)
        pathTo = os.path.join(stashDirectory, f'Stash_{(self.inactiveStash+1)}')
        try:
            with open(pathTo, 'w', encoding='utf-8') as file:
                file.write(self.rawActive)
        except Exception as e:
            print(f'Error writing to Stash_{self.inactiveStash+1}: {str(e)}')
            raise e
        self.inactiveStash = self.inactiveStash #Updates values held by rawInactive.
        self.rawActive = self.EMPTYSTASH
        self.save()
        with open(pathTo, 'r', encoding='utf-8') as file:
            output = file.read()
        return output
                    
    def delete(self):
        """Delete External Stash at self.inactive"""
        pathTo = os.path.join(self.outputPath, "Backups")
        try:
            os.remove(os.path.join(pathTo, f"Stash_{(self.inactiveStash+1)}"))   
        except FileNotFoundError:
            print('file \'Stash_{(self.inactiveStash+1)}, not found')
        except PermissionError:
            print('lack of permission to delete. Please run as admin.')
        except Exception as e:
            print(f'other error: {e}\nwhile trying to delete Stash_{self.inactiveStash+1}')

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
        currentStashes = self.parseStashes(rawSave) #returns a list
        for i, stash in enumerate(currentStashes):
            parts = rawSave.split(stash, 1)
            rawSave = f"Place_Holder_{i}".join(parts)
        
        for i, stash in enumerate(self.activeStashList):
            parts = rawSave.split(f"Place_Holder_{i}", 1)
            rawSave = stash.join(parts)
            
        decompress.recompress(rawSave, savePath)



    """
    takes raw string of save and returns the list of stashes in it.
    seems to be working right now.
    """
    def parseStashes(self, rawSave):
        sentinel = r'"StashJson\":\"{\\\"Pages\\\":'
        position = rawSave.find(sentinel)
        #print(position)
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
        #PLACEHOLDER
        if self.getActiveListItem(0) == self.parseStashes(rawSave)[0]:
            print("Setting active stash 0 works in init.")
        else:
            print("init is fucked.")
        #CURSED SETTERS THAT BREAK SETTING ACTIVE STASH 0
        self.activeStash = activeStash
        #self.inactiveStash = inactiveStash
        #self.rawInactive = self.inactiveStash
        #self.rawActive = self.activeStash
        if self.getActiveListItem(0) == self.parseStashes(rawSave)[0]:
            print("Declaring their values in init is fine.")
        else:
            print("declaring their values in init is fucked.")

#IMPORTANT: StashJson is in ['serializedSaveData', 'values', '0', '<value>']
def main():
    print('all good.')
    saveManager = FileHandler()
    for i in range(3):
        print(f'round {i} of swapping.')
        saveManager.activeStash = i
        saveManager.inactiveStash = i
        saveManager.swap()


if __name__ == "__main__":
    main()