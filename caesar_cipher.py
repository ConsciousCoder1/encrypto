print('''
    ______      _____                  _   _             
    | ___ \    /  __ \                | | (_)            
    | |_/ /   _| /  \/_ __ _   _ _ __ | |_ _  ___  _ __  
    |  __/ | | | |   | '__| | | | '_ \| __| |/ _ \| '_ \ 
    | |  | |_| | \__/\ |  | |_| | |_) | |_| | (_) | | | |
    \_|   \__, |\____/_|   \__, | .__/ \__|_|\___/|_| |_|
        __/ |            __/ | |                      
        |___/            |___/|_|                      ''')
print('\n--------------------- CAESAR STYLE ---------------------\n')
print("\nWelcome to PyCrytion -- Caeser Style!\n")


encode_decode = input("\nTo encrypt a message, type 'encode'. To decrypt a message, type 'decode'. --> ")
user_message = list(input("Please enter your message --> "))
cipher_number = int(input("How many places will you cipher shift? --> "))


def encode(user_message=user_message, cipher_number=cipher_number):
    from logo import alphabet
    user_message_encoded = ""
    for i in user_message:
        old_i_index = alphabet.index(i)
        new_i_index = alphabet.index(i) + cipher_number
        user_message_encoded += alphabet[new_i_index]
        if old_i_index == ' ':
            print(' ')
    print(f"Your encrypted message:\n{user_message_encoded}")
    

def decode(user_message = user_message, cipher_number = cipher_number):
    user_message_decoded = ""
    for i in user_message:
        old_i_index = alphabet.index(i)
        new_i_index = alphabet.index(i) - cipher_number
        user_message_decoded += alphabet[new_i_index]
    print(f"Your encrypted message:\n{user_message_decoded}")

if encode_decode == 'encode':
    encode(user_message=user_message, cipher_number=cipher_number)
elif encode_decode == 'decode':
    decode(user_message=user_message, cipher_number=cipher_number)
    
