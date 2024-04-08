import zlib
from pathlib import Path

def readByteFileToEnd(file_path):
    """Reads the entire binary content of the file specified by file_path."""
    with open(file_path, 'rb') as file:
        return file.read()

def unzipString(content):
    """Decompresses the binary data using the Deflate algorithm and decodes it to a string."""
    decompressedData = zlib.decompress(content, wbits=-15)
    #print('Decompressed data, decoding UTF-8.')
    return decompressedData.decode('utf-8-sig')

def decompressFile(file_path):
    """Wrapper function that reads, decompresses, and returns the decompressed data."""
    #print(f'Decompressing file at {file_path}...')
    binaryData = readByteFileToEnd(file_path)
    #print('Bytefile read. Unzipping...')
    return unzipString(binaryData)

def recompress(data_str, output_path):
    """Compresses the given string data using the Deflate algorithm, writes the binary compressed data to the specified output path, and possibly overwrites an old file."""
    bom = b'\xef\xbb\xbf'
    # Convert the string data back to binary
    data_bytes = bom + data_str.encode('utf-8')
    # Create a compression object for raw DEFLATE compression
    compressor = zlib.compressobj(wbits=-15)
    # Compress the data and flush to finalize compression
    compressed_data = compressor.compress(data_bytes) + compressor.flush()
    # Write the compressed binary data to the specified output path
    with open(output_path, 'wb') as file:
        file.write(compressed_data)

if __name__ == '__main__':
    input_path = Path.home() / 'AppData\\LocalLow\\Realm Archive\\Death Must Die\\Saves\\Slot_0.sav'
    output_path = Path.home() / 'AppData\\LocalLow\\Realm Archive\\Death Must Die\\Saves\\Recompressed_Slot_0.sav'
    text = decompressFile(input_path)
    recompress(text, output_path)
    #print(f'Recompression complete. Output file at {output_path}')


if __name__ == '__main__':
    file_path = Path.home() / 'AppData\\LocalLow\\Realm Archive\\Death Must Die\\Saves\\Slot_0.sav'
    #with open(file_path, 'rb') as file:
        #text = file.read()

    #try_decompress(text)

    for i in range(100):
        print('decompressing...')
        text = decompressFile(file_path)
        print('recompressing...')
        recompress(text, file_path)
        print(f'cycle: {i}, completed without incident.')
