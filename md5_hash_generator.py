#md5_hash_generator
import hashlib, binascii

pin = input("Enter PIN (4 - 8 digits) : ")

while pin.isdigit() == False or len(pin) < 4 or len(pin) > 8:
    print("\n Invalid input \n")
    pin = input("Enter PIN (4 - 8 digits) : ")


md5_hash = hashlib.new('md5', pin.encode('utf-8')).digest()
print("Hash:\n",binascii.hexlify(md5_hash))

