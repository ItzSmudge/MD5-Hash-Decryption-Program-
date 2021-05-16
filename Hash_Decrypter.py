from hashlib import md5

print("MD5 HASH DECRYPTER")
print("="*20)
print()

pinHash = input("Enter password hash(MD5):")
print()

with open("PIN.txt","r") as wordlist:

    for pin in wordlist:
        hash = md5(pin.strip().encode('utf-8')).hexdigest()
        if hash == pinHash:
            print("PIN has been found:",pin)
    else:
        print("PIN has not been found")
