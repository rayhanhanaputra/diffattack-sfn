from sfnEncrypt import main

plainteks = "0000000000000000"
key = "000000000000000000000000"

binary_string = ""
key_string = ""
for c in plainteks:
    binary_string = binary_string + str(bin(int(c,16))[2:]).zfill(4)

for c in key:
    key_string = key_string + str(bin(int(c,16))[2:]).zfill(4)


fake = main(binary_string,key_string)

print("Output cipher:\t"+hex(int(fake,2))[2:])
# print("\t\tCE28-4415-9C1E-E46F")