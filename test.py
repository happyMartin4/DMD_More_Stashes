def main():
    listOfNum = [1,2,3,1,1,5,3]
    metaDict = {}
    for num in listOfNum:
        if num in metaDict:
            metaDict[num] += 1
        else:
            metaDict[num] = 1
    
    print(metaDict)


if __name__ == '__main__':
    main()