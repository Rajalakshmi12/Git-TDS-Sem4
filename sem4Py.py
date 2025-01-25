def byteFunc():
    #Create an array of 128 bytes
    bytes_array = bytearray([0xEF,0xBB,0xBF])
    bytes_array.extend(range(3,256))
    print(bytes_array[:10])
    
    #Write the bytes to a file
    with open("128bytes.txt","wb") as file:
        file.write(bytes_array)
    
byteFunc()

def generate_hexdump(file_path):
    try:
        with open(file_path, "rb") as file:
            offset = 0
            while chunk := file.read(16):  # Read 16 bytes at a time
                # Convert bytes to hex values
                hex_values = " ".join(f"{byte:02X}" for byte in chunk)
                # Convert bytes to printable ASCII (dots for non-printable)
                ascii_values = "".join(chr(byte) if 32 <= byte <= 256 else "." for byte in chunk)
                # Print offset, hex values, and ASCII representation
                print(f"{offset:08X}  {hex_values:<48}  {ascii_values}")
                offset += 16
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Example usage
generate_hexdump("128bytes.txt")
