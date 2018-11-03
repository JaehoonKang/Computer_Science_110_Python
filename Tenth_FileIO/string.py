"""
Analysis
Write a program that repeatedly encrypts or decrypts a message given the
operation to perform and either the rotation key (when encrypting) or the
rotation key that was used to encrypt (in the case of decrypting)

Output to monitor:
  new_message (str)

Input from keyboard:
  message (str)
  operation (str) - 'E', 'e', 'D', or 'd'
  rotation_key(int)

Tasks allocated to functions:
  validate_operation() - simple Predicate function
  validate_rotation_key() - simple Predicate function
  convert_rotation_key()
  keep_in_bounds()
  process_message()
"""    
# Design
# A particular program performs encryption and decryption of text strings
# text is encrypted using a Caeser Cipher

#Initialize constants ---------------------------------------------------------

OPERATIONS = {'e':(1,"Encrypted"), 'd':(-1,"Decrypted")}

# Min and limit ordinals of printable ASCII
PRINTABLE_ASCII_MIN = 32
PRINTABLE_ASCII_LIMIT = 127
# Define constant
Neigative_One = -1
PRINTABLE_CHAR = 95
# Allowable rotation key prefixes
KEY_PREFIX = "-"

# Functions ------------------------------------------------------------------

# Check that requested operation is valid
# param op_str (str) - operation requested
# invoke len()
# invoke str.lower()
# return  True when valid, False otherwise (bool)
def validate_operation(op_str):
  return op_str.lower() in OPERATIONS

# Check that rotation key is of form <digits> or -<digits>
# param rotation_key_str (str)
# invoke str.isdigit() 
# returns:  True when valid, False otherwise (bool)
def validate_rotation_key(rotation_key_str):
  comparator = rotation_key_str.replace(KEY_PREFIX,'')
  negative_count = rotation_key_str.count(KEY_PREFIX)
  return ((negative_count <= 1 and comparator.isdigit()) and int(comparator) !=0)

# Convert rotation key to value usable for requested operation
# param  op (str) - operation requested 
# param  rotation_key_str (str)
# invoke int()
# return encryption or decryption rotation key (int)
def convert_rotation_key(op_str, rotation_key_str):
  op_str = op_str.lower()
  rotation_key = int(rotation_key_str)
  de_rotation_key = Neigative_One * rotation_key
  return rotation_key if op_str == 'e' else de_rotation_key
  
# Perform string modulus operation to prevent processed character 
# from going out of bounds
# param ordinal (int)
# returns adjusted ordinal of new character (int)
# Hint:  Use two sequential while loops
def keep_in_bounds(ordinal):
  while ordinal >= PRINTABLE_ASCII_LIMIT:
    ordinal -= PRINTABLE_CHAR
  while ordinal < PRINTABLE_ASCII_MIN:
    ordinal += PRINTABLE_CHAR
  return ordinal
  
# Encrypt or decrypt message using rotation_key
# param message (str)
# param rotation_key (int)
# invoke keep_in_bounds() 
# return processed_message (str)
def process_message(message, rotation_key):
  ## temp = []
  temp = ''
  for char in message:
    char = ord(char)
    rotate_char = keep_in_bounds(char + rotation_key)
    processed_message = chr(rotate_char)
    ##temp.append(processed_message)
    temp +=processed_message
  return temp

# Main -----------------------------------------------------------------------

# Gets plain text or cipher code, operation requested (encrypt or decrypt),
# and rotation key for Caesar cipher
# Generates cipher code or plain text
def main():
  # Describe program
  print("This program encrypts or decrypts messages " + \
        "using a Caesar cipher")
  # Priming read and repeat
  message = input('Input the message to be processed\n'
                  '(or press <ENTER> to quit): ')
  while message:
    # Get remaining inputs, validate and convert as necessary
    op_str = input('Do you want to encrypt or decrypt?\n'
                 '(Enter E for encrypt or D for decrypt): ')
    while not validate_operation(op_str):
      print('That operation does not appear to be valid, please try again')
      op_str = input('Do you want to encrypt or decrypt?\n'
                     '(Enter E for encrypt or D for decrypt): ')
    rotation_key_str = input('Enter the rotation key to be used for encryption OR\n'
                             'the key that was used for encryption: ')
    while not validate_rotation_key(rotation_key_str):
      rotation_key_str = input('Enter the rotation key to be used for encryption OR\n'
                               'the key that was used for encryption: ')        
    # Encrypt or decrypt contents of message
    rotation_key = convert_rotation_key(op_str, rotation_key_str)
    # Display result      
    translation = process_message(message,rotation_key)
    print('The %s message is: %s'%(('encrypted' if op_str.lower()=='e' else 'decrypted'),translation))
    # Continuation read
    message = input('Input the message to be processed\n'
                      '(or press <ENTER> to quit):  ')

main()
