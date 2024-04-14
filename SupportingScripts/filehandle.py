from . import decompress
import os
from pathlib import Path
from datetime import datetime, timedelta
import re

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
            print(f'Error reading from Stash_{newRawInact+1} while setting inactiveStash: {str(e)}\nDefaulting to empty stash for stash {self.inactiveStash}')
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
        try:
            rawSave = self.readAndDecompress()
            self.setActiveList(self.parseStashes(rawSave))
        except Exception as e:
            self.setActiveList([])
            print(f"Error reading file or parsing stash data: {str(e)}")
        exportStatus, importStatus = False, False
        oldActive = self.rawActive
        oldInactive = self.rawInactive
        self.exportOverwrite()
        self.rawActive = oldInactive
        self.save()
        self.inactiveStash = self.inactiveStash #Try to update files to see if it stops corrupt stashes
        self.activeStash = self.activeStash
        if oldInactive == self.getActiveListItem(self.activeStash) and oldInactive != self.EMPTYSTASH:
            print('import true')
            importStatus = True
        if oldActive == self.rawInactive and self.rawInactive != self.EMPTYSTASH:
            print('export true')
            exportStatus = True
        else:
            if oldActive != self.rawInactive:
                print('exported stash does not align with what was previously there.')
            if self.rawInactive == self.EMPTYSTASH:
                print('exported stash was empty.')
        return (exportStatus, importStatus)

    """
    writes out to a file to store a stash.
    working right now. 
    """
    def export(self, fileIndex=1):
        try:
            rawSave = self.readAndDecompress()
            self.setActiveList(self.parseStashes(rawSave))
        except Exception as e:
            self.setActiveList([])
            print(f"Error reading file or parsing stash data: {str(e)}")

        if self.rawActive != self.EMPTYSTASH:
            stashDirectory = os.path.join(self.outputPath, "Stashes")
            os.makedirs(stashDirectory, exist_ok=True)
            pathTo = os.path.join(stashDirectory, f'Stash_{fileIndex}')
            while os.path.exists(pathTo):
                fileIndex += 1
                pathTo = os.path.join(stashDirectory, f'Stash_{fileIndex}')
            try:
                with open(pathTo, 'w', encoding='utf-8') as file:
                    file.write(self.rawActive)
                self.rawActive = self.EMPTYSTASH #Point of failure
                self.save()
            except Exception as e:
                print(f'Error writing to external file: {str(e)}\nAbandoning export attempt.')
                raise e
            self.inactiveStash = self.inactiveStash 
            return fileIndex-1
        else:
            print("Skipping export because active stash is empty.")
            return -1
    

    """
    Outputs current inactive stash to 
    """
    def exportOverwrite(self):
        try:
            rawSave = self.readAndDecompress()
            self.setActiveList(self.parseStashes(rawSave))
        except Exception as e:
            self.setActiveList([])
            print(f"Error reading file or parsing stash data: {str(e)}")

        stashDirectory = os.path.join(self.outputPath, "Stashes")
        os.makedirs(stashDirectory, exist_ok=True)
        pathTo = os.path.join(stashDirectory, f'Stash_{(self.inactiveStash+1)}')
        if self.rawActive != self.EMPTYSTASH:
            try:
                with open(pathTo, 'w', encoding='utf-8') as file:
                    file.write(self.rawActive)
            except Exception as e:
                print(f'Error writing to Stash_{self.inactiveStash+1}: {str(e)}')
                raise e
            self.inactiveStash = self.inactiveStash #Updates values held by rawInactive.
            self.rawActive = self.EMPTYSTASH
            self.save()
            self.inactiveStash = self.inactiveStash #Try to update files to see if it stops corrupt stashes
        else:
            print("Stash being exported is empty. Deleting instead of writing to it.")
            self.delete()
                    
    def delete(self):
        """Delete External Stash at self.inactive"""
        pathTo = os.path.join(self.outputPath, rf'Stashes\Stash_{self.inactiveStash+1}')
        try:
            os.remove(pathTo)
            self.inactiveStash=self.inactiveStash
            return 0   
        except FileNotFoundError:
            print('file \'Stash_{(self.inactiveStash+1)}, not found')
        except PermissionError:
            print('lack of permission to delete. Please run as admin.')
        except Exception as e:
            print(f'other error: {e}\nwhile trying to delete Stash_{self.inactiveStash+1}')
        self.inactiveStash = self.inactiveStash
        return 1

    def backupLogic(self, timeRange, filePath, amount):
        amount += 1
        now = datetime.now()
        print(filePath)
        filesUnfiltered = os.listdir(filePath)
        print(filesUnfiltered)
        files = []
        #erase files not using name conventions
        timeDict = {}
        for file in filesUnfiltered:
            search = re.search(r'Backup_[0-9]+_[0-9]+_[0-9]+_[0-9]+\.[0-9]+', file)
            if search:
                files.append(file)
        
        for i, file in enumerate(files):
            timeDict[f'{i}'] ={'name' : file, 'time' : os.path.getmtime(os.path.join(filePath, file))}
        try:
            mostRecent = max(timeDict.values(), key=lambda x: x['time'])
            diff = now - datetime.fromtimestamp(mostRecent['time'])
            exists = True
            print('able to find the save path for a backup and found the latest backup at ' + str(datetime.fromtimestamp(mostRecent['time'])))
        except ValueError:
            print('there does not appear to be a most recent file.')
            mostRecent = 0
            diff = timedelta(seconds=1)
            exists = False
        except Exception as e:
            print('something went wrong: ' + str(e))
            raise e
        
        print(diff)
        print(timeRange)
        if diff > timeRange or exists == False:
            backupPath = os.path.join(filePath, f'Backup_{now.month}_{now.day}_{now.year}_{now.hour}.{now.minute}.sav')
            print('trying to save a backup to ' + filePath)
            try:
                with open(self.inputPath, 'rb') as file:
                    save = file.read()
                if(os.path.exists(backupPath)):        
                    print(f'file with same name, {os.path.basename(backupPath)}, exists. aborting operation.')
                else:
                    with open(backupPath, 'wb') as file:
                        file.write(save)
                    print('backup completed successfully.')
                    print('trying to see if deletion is called for...')

            except Exception as e:
                print('something went wrong while trying to backup: ' + str(e))
        else:
            print('it hasn\'t been long enough yet for a backup')
        deleteLoop = True
        while deleteLoop:
            if len(files) > amount:
                print('beginning deletion.')
                files = []
                timeDict = {}
                filesUnfiltered = os.listdir(filePath)
                for file in filesUnfiltered:
                    search = re.search(r'Backup_[0-9]+_[0-9]+_[0-9]+_[0-9]+\.[0-9]+', file)
                    if search:
                        files.append(file)
                for i, file in enumerate(files):
                    timeDict[f'{i}'] ={'name' : file, 'time' : os.path.getmtime(os.path.join(filePath, file))}
                oldest = min(timeDict.values(), key=lambda x: x['time'])
                print('there are more backups than the acceptable amount. Trying to delete: ' + str(oldest['time']))
                os.remove(os.path.join(filePath, oldest['name']))
                print(oldest)
            else:
                print(f'files, {len(files)}.\namount: {amount}')
                deleteLoop = False



        



    def backup(self):
        backupDirectory = os.path.join(self.outputPath, "Backups")
        os.makedirs(backupDirectory, exist_ok=True)

        listOfTimeUnits = ['mon', 'week', 'day', 'hour', 'minute']


        targetTime = {}
        
        monSearch = re.search(r'mon:?\s?(\d+)', self.backups.lower())
        weekSearch = re.search(r'week:?\s?(\d+)', self.backups.lower())
        daySearch = re.search(r'day:?\s?(\d+)', self.backups.lower())
        hourSearch = re.search(r'hour:?\s?(\d+)', self.backups.lower())
        minSearch = re.search(r'min:?\s?(\d+)', self.backups.lower())

        listOfSearches = [monSearch, weekSearch, daySearch, hourSearch, minSearch]
        listOfConversions = [timedelta(days=30), timedelta(days=7), timedelta(days=1), timedelta(hours=1), timedelta(minutes=1)]
        for i, unit in enumerate(listOfTimeUnits):
            if listOfSearches[i]:
                thisAmount = listOfSearches[i].group(1)
            else:
                thisAmount = 0
            targetTime[f'{unit}'] = {'path' : f'{os.path.join(backupDirectory, unit)}', 'amount' : int(thisAmount), 'time' : listOfConversions[i]}

        for key in targetTime:
            print(f'{key}: {targetTime[key]}')

        for key in targetTime:
            if targetTime[key]['amount'] >= 1:
                os.makedirs(targetTime[key]['path'], exist_ok=True)
                self.backupLogic(targetTime[key]['time'], targetTime[key]['path'], targetTime[key]['amount'])


        
        '''
        pathTo = os.path.join(backupDirectory, f'Backup_{fileIndex}.sav')
        while os.path.exists(pathTo):
            fileIndex += 1
            pathTo = os.path.join(backupDirectory, f'Backup_{fileIndex}.sav')
        with open(self.inputPath, 'rb') as file:
            saveHolder = file.read()
        with open(pathTo, 'wb') as file:
            file.write(saveHolder)
        '''
                    
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
    , outputPath=Path.home() / 'AppData\\LocalLow\\Realm Archive\\Death Must Die\\Saves\\', activeStash=0, inactiveStash=0, backups='mon:4,week:4,day:7,hour:12,min:10'):
        self.backups = backups
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

#IMPORTANT: StashJson is in ['serializedSaveData', 'values', '0', '<value>']
def main():
    print('all good.')


if __name__ == "__main__":
    main()