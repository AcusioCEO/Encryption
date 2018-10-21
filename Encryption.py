import binascii


String = "Agreement finalized"
encoder = "{0:b}".format(5)
encryptedArray = []

print "\n\nThis is the orignial message: " + String
print "\n\n-------Encrypted data-------"
for x in String:

    index = ''.join(format(ord(x), 'b'))

    encryptedBinary = int(index, 2) ^ int(encoder, 2)

    print '{0:b}'.format(encryptedBinary)

    encryptedAscii = binascii.unhexlify('%x' % encryptedBinary)
    encryptedArray.append(encryptedAscii)

    # print encryptedAscii

print "-------End of Encrypted data-------\n\n"


print "Encrypted message: " + ''.join(encryptedArray)
