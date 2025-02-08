# Read the encoded file
import os

file_path = os.path.join(os.path.dirname(__file__), "chall.txt")

with open(file_path, "rb") as f:
    encoded_data = f.read().decode("iso8859-1")

# Decode the flag
decoded_flag = ""

for c in encoded_data:
    binary = bin(ord(c))[2:].zfill(8)  # Convert character to binary (8 bits)

    # Replace the first '1' back to '0' to undo the encoding
    for i in range(8):
        if binary[i] == "1":
            binary = binary[:i] + "0" + binary[i + 1 :]
            break

    decoded_flag += chr(int(binary, 2))  # Convert back to ASCII
print(decoded_flag)
