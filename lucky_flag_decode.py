import json

# Encoded string with Unicode escape sequences
enc = "\\u000e\\u0003\\u0001\\u0016\\u0004\\u0019\\u0015V\\u0011=\\u000bU=\\u000e\\u0017\\u0001\\t=R\\u0010=\\u0011\\t\\u000bSS\\u001f"

# Decode JSON string to get actual characters
decoded_str = json.loads(f'"{enc}"')

# XOR each character with 0x62 to decrypt
flag = "".join(chr(ord(c) ^ 0x62) for c in decoded_str)
print(flag)
