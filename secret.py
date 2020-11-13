import base64

secret = "aHR0cHM6Ly9tZWdhLm56LyNGIVBIcGt3S3BhITM2VmNFN2dxa094eUcxeTVSTEFHNnc="

print("Input:",secret)
print("Output:",base64.b64decode(secret))

