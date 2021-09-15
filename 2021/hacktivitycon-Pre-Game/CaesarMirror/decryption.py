ALPHABET_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET_lower = 'abcdefghijklmnopqrstuvwxyz'
KEY = 13

def caesar_mirror_decrypt():
    encrypted_file = open("caesarmirror.txt", 'r')
    decrypted_file = open("caesarmirror_decrypted.txt", 'w')

    half_mirrored_plaintext = []
    final_mirrored_plaintext = []
    
    for line in encrypted_file:
        line = line.strip()
        plain_text = ''
        for c in line:
            if c.isupper():
                index = ALPHABET_upper.find(c)
                index = (index-KEY) % len(ALPHABET_upper)
                plain_text += ALPHABET_upper[index]
            elif c.islower():
                index = ALPHABET_lower.find(c)
                index = (index-KEY) % len(ALPHABET_lower)
                plain_text += ALPHABET_lower[index]
            else:
                plain_text += c
        
        decrypted_file.write(plain_text + '\n')
        half_mirrored_plaintext.append(plain_text.split('   '))
    
    encrypted_file.close()
    decrypted_file.close()
    
    for _, mirrored in half_mirrored_plaintext:
        final_mirrored_plaintext.append("".join(reversed(mirrored)))

    with open('caesarmirror_decrypted.txt', 'a') as file:
        file.write("\n")
        for i in range(len(half_mirrored_plaintext)):
            file.write(half_mirrored_plaintext[i][0] + ' ' + final_mirrored_plaintext[i] + '\n')

caesar_mirror_decrypt()
