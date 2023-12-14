def generate_playfair_key(key):
    
    key = key.replace(" ", "").upper()  
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    key_matrix = ""
    
    
    for char in key:
        if char not in key_matrix:
            key_matrix += char
    
    for char in alphabet:
        if char not in key_matrix:
            key_matrix += char
    
    
    playfair_matrix = [key_matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def encrypt_playfair(plaintext, key):
    playfair_matrix = generate_playfair_key(key)
    
    plaintext = plaintext.upper().replace(" ", "").replace("J", "I")
    
    
    pairs = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1 or plaintext[i] == plaintext[i + 1]:
            pairs.append(plaintext[i] + 'X')
            i += 1
        else:
            pairs.append(plaintext[i] + plaintext[i + 1])
            i += 2
    
    
    ciphertext = ""
    for pair in pairs:
        first_letter, second_letter = pair[0], pair[1]
        row1, col1 = 0, 0
        row2, col2 = 0, 0
        
        
        for i in range(5):
            for j in range(5):
                if playfair_matrix[i][j] == first_letter:
                    row1, col1 = i, j
                if playfair_matrix[i][j] == second_letter:
                    row2, col2 = i, j
        
        
        if row1 == row2:
            ciphertext += playfair_matrix[row1][(col1 + 1) % 5] + playfair_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += playfair_matrix[(row1 + 1) % 5][col1] + playfair_matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += playfair_matrix[row1][col2] + playfair_matrix[row2][col1]
    
    return ciphertext


plaintext = "CLASSROOM"
key = "MONARCHY"
encrypted_text = encrypt_playfair(plaintext, key)
print("Plaintext:", plaintext)
print("Key:", key)
print("Encrypted text:", encrypted_text)
