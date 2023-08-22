import sys

# Read command line argument as string
text = sys.argv[1]

# Read each character in the string
print("Text in binary: ", text)
for char in text:
    # Print the character as binary
    print(bin(ord(char)), end=' ')
print()

# Print a new line before printing the hex
print("\nText in hex: ", text)
for char in text:
    # Print the character as hex
    print(hex(ord(char)), end=' ')

print()
