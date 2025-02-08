import base64
import urllib.parse

# Given encoded string
encoded_target = "JTNEJTNEUWZsSlglNUJPTERfREFUQSU1RG85MWNzeFdZMzlWZXNwbmVwSjMlNUJPTERfREFUQSU1RGY5bWI3JTVCT0xEX0RBVEElNURHZGpGR2I="

# Step 5: Base64 decode
decoded_step4 = base64.b64decode(encoded_target).decode()

# Step 4: URL decode
decoded_step3 = urllib.parse.unquote(decoded_step4)

# Step 3: Replace "[OLD_DATA]" back to "Z"
decoded_step2 = decoded_step3.replace("[OLD_DATA]", "Z")

# Step 2: Reverse the string
decoded_step1 = decoded_step2[::-1]

# Step 1: Base64 decode to get the original flag
original_flag = base64.b64decode(decoded_step1).decode()
print(original_flag)
