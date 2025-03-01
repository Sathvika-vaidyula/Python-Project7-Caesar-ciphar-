logo = '''   
  ____          _            ____ _       _                
 / ___|__ _ ___| |__   ___  / ___(_)_ __ | |__   ___ _ __ 
| |   / _` / __| '_ \ / _ \| |   | | '_ \| '_ \ / _ \ '__|
| |__| (_| \__ \ | | | (_) | |___| | |_) | | | |  __/ |   
 \____\__,_|___/_| |_|\___/ \____|_| .__/|_| |_|\___|_|  
                                    |_|                    
'''

print(logo)

alphabets = [chr(i) for i in range(97, 123)]  # Generates ['a', 'b', ..., 'z']

def caesar_cipher(original_text, shift_num, mode):
    cipher_text = ''
    
    for letter in original_text:
        if letter in alphabets:
            old_position = alphabets.index(letter)
            new_position = (old_position + shift_num) % 26 if mode == "encode" else (old_position - shift_num) % 26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += letter  # Keep spaces, numbers, and special characters unchanged

    print(f"Here is the {mode}d result: {cipher_text}")

# Loop to allow multiple encryptions/decryptions
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26  # Ensure shift is within range

    caesar_cipher(text, shift, direction)

    restart = input("Type 'yes' if you want to continue, otherwise type 'no':\n").lower()
    if restart == 'no':
        should_continue = False
        print("Goodbye!")
