import re as reg
import decompress
from pathlib import Path


class FileHandler:
    def __init__(self, inputPath, outputPath):
         self.inputPath = inputPath
         self.outputPath = outputPath

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
    
    def save():
        return
    
    def swap():     
        return      
                    
    def delete():   
        return      
                    
    def export():   
        return      

    def parseStash(save):
        sentinel = r'"StashJson\":\"{\\\"Pages\\\":'
        position = save.find(sentinel)
        print(position)
        relevantSave = save[position + len(sentinel):]
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
            



def main():
    inputPath = Path.home() / r'AppData\LocalLow\Realm Archive\Death Must Die\Saves\Slot_0 - Copy.sav'
    outputPath = Path.home() / r'AppData\LocalLow\Realm Archive\Death Must Die\Saves\Output\decompressed.sav'
    handler = FileHandler(inputPath, outputPath)
    decompressedData = handler.readAndDecompress()
    result = handler.writeToFile(decompressedData)
    print(result)

    # Testing parseStash function
    try:
        with open(outputPath, 'r', encoding='utf-8') as file:
            save_data = file.read()
            #print(save_data)
            stash_data = FileHandler.parseStash(save_data)
            #print("Stash data:", stash_data)
            print("THIS IS STASH 1: " + stash_data[0])
            print("--"*40)
            print("THIS IS STASH 2: " + stash_data[1])
            print("--"*40)
            print("THIS IS STASH 3: " + stash_data[2])
    except Exception as e:
        print(f"Error reading file or parsing stash data: {str(e)}")

if __name__ == "__main__":
    main()