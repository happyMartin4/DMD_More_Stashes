import zlib

def readByteFileToEnd(file_path):
    """Reads the entire binary content of the file specified by file_path."""
    with open(file_path, 'rb') as file:
        return file.read()

def unzipString(content):
    """Decompresses the binary data using the Deflate algorithm and decodes it to a string."""
    decompressedData = zlib.decompress(content, -zlib.MAX_WBITS)
    return decompressedData.decode('utf-8')

def decompressFile(file_path):
    """Wrapper function that reads, decompresses, and returns the decompressed data."""
    binaryData = readByteFileToEnd(file_path)
    return unzipString(binaryData)