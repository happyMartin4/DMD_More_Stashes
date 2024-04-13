from SupportingScripts import filehandle
from SupportingScripts import dataparse
import json
import os

def main():
    saveManager = filehandle.FileHandler()
    bigDict = dataparse.parseStash(saveManager.getActiveListItem(0))
    for key in bigDict:
        print(bigDict[key])

if __name__ == '__main__':
    main()