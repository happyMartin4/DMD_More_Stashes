import zlib
from pathlib import Path

def main():
    home = Path.home()
    output_path = home / r'AppData\LocalLow\Realm Archive\Death Must Die\Saves\Output\decompressed.sav'
    input_path = home / r'AppData\LocalLow\Realm Archive\Death Must Die\Saves\Slot_0 - Copy.sav'
    readable = decompress(input_path)
    with open(output_path, 'w+', encoding='utf-8') as file:
        file.write(readable)

def read_byte_file_to_end(file_path):
    """Reads the entire binary content of the file specified by file_path."""
    with open(file_path, 'rb') as file:
        file_data = file.read()
    return file_data

def unzip_string(content):
    """Decompresses the binary data using Deflate algorithm and decodes it to a string."""
    # The zlib.decompress function requires the 'content' to have the correct header for DEFLATE
    # If it's raw DEFLATE data without headers, it might still work as is.
    # If it throws an error, try adding a 2-byte header or using decompressobj()
    decompressed_data = zlib.decompress(content, -zlib.MAX_WBITS)  # This syntax is for raw DEFLATE
    return decompressed_data.decode('utf-8')

def load_data(save_file_path):
    """Reads, decompresses, and decodes the game save data."""
    file_data = read_byte_file_to_end(save_file_path)
    json_data = unzip_string(file_data)
    return json_data

def decompress(input_path):
    json_data = load_data(input_path)
    return json_data

if __name__ == "__main__":
    main()