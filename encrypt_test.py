import base64

myHardCypher="wp7Dl8ORw6Fqw5jDm8KOwqvCj8Obw6LCvMOYw5bDlWrCuMKIw6XCq8Odw5zCjsK-w57CiMOWwrPDk8ONwpw="

# encryption using a Vigenère cipher taken from :
# https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
# END def encode

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
# END def decode


def main() : 
    print ("Running main ....")

    myKey = 'John'
    myClear = 'This is a string I want to hide.'
    myCypher = ''
    myNewClear = ''
    myHardClear = ''

    print(myClear)
    print(len(myClear))
    myCypher = encode(myKey, myClear)
    print (myCypher)
    print (len(myCypher))
    myNewClear = decode(myKey, myCypher)
    print (myNewClear)
    print (len(myNewClear))
    print (myHardCypher)
    print (len(myHardCypher))
    myHardClear = decode(myKey, myHardCypher)
    print (myHardClear)
    print (len(myHardClear))

    newKey=input("Enter the key to decrypt the cypher : (hint John) : ")
    
    myHardClear = decode(newKey, myHardCypher)
    print (myHardClear)
    print (len(myHardClear))


# END def main     

if __name__ == '__main__' :
    main()
    
