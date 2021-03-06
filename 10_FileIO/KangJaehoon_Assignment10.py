"""
Analysis
Write a program that repeatedly encrypts or decrypts a message given the
operation to perform and either the rotation key (when encrypting) or the
rotation key that was used to encrypt (in the case of decrypting)

Ceasar cipher program to allow a user to repeatedly specify an entire file of plain text
or encrypted text to process


Output to monitor:
  new_message (str)

Input from keyboard:
  ## message (str)
  the requested operation: operation (str) - 'E', 'e', 'D', or 'd'
  rotation_key(int)
  input the file name (instead of a line of text)
  
Tasks allocated to functions:
  validate_operation() - simple Predicate function
  validate_rotation_key() - simple Predicate function
  convert_rotation_key()
  keep_in_bounds()
  process_message()
"""    
# Design
# for file validation
import os.path
# A particular program performs encryption and decryption of text strings
# text is encrypted using a Caeser Cipher

# Initialize constants ---------------------------------------------------------

OPERATIONS = {'e':(1,"Encrypted"), 'd':(-1,"Decrypted")}

# Min and limit ordinals of printable ASCII
PRINTABLE_ASCII_MIN = 32
PRINTABLE_ASCII_LIMIT = 127
# Define constant
Neigative_One = -1
PRINTABLE_CHAR = 95
# Allowable rotation key prefixes
KEY_PREFIX = "-"
# Required file extension
FILE_EXT = ".txt"
# File processing modes
READ_MODE = 'r'
WRITE_MODE = 'w' 

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

# Implementing exception handling

# Checks that file exists and that extension is .txt
# param name(str)
# invoke isfile() from module os.path and endswith()
# return True when valid, False otherwise (bool)
def validate_file_name(name):
  return os.path.isfile(name) and name.endswith(FILE_EXT)

# Generates output file name from input file name, operation requested
# and converted rotation key
# param file_name (str)
# param operation (str)
# param rotation_key (int) - converted key
# invoke str.split(), str.replace() and str.join()
# return output file name (str)
def make_name(file_name, operation, rotation_key):
  name_list = file_name.split(".")
  name_list[0] = name_list[0].replace(OPERATIONS['e'][1],"")
  name_list[0] = name_list[0].replace(OPERATIONS['d'][1],"")
  name_list[0] += (OPERATIONS[operation][1] + str(rotation_key))
  return ".".join(name_list)

# Processes list of lines(i.e., messages)from input file list
# one line at a time
# param new_list(list)
# param rotation_key (int)
# invoke list.append()
#        process_message()
# return list of processed lines (i.e., messages)(list)
def process_message_list(new_list,rotation_key):
  LIST = []
  for line in new_list:
    message = process_message(line, rotation_key)
    LIST.append(message)
  return LIST

# Write each line in output list to file
# param file(type: _io.TextIOWrapper - i.e., it's a text file)
# param text_list(list)
# return None
def write_to_file(file, text_list):
  file_write = open('%s%s'%(file,FILE_EXT),WRITE_MODE)
  for i in text_list:
    file_write.write(i)
  file_write.close()
  return None

# Main -----------------------------------------------------------------------

# Gets plain text or cipher code, operation requested (encrypt or decrypt),
# and rotation key for Caesar cipher
# Generates cipher code or plain text
def main():
  # Describe program
  print("This program encrypts or decrypts messages " + \
        "using a Caesar cipher")
  # Priming read and repeat
  filename = input('Input the filename to be processed\n'
                  '(or press <ENTER> to quit): ')
  while filename:
    while not validate_file_name(filename):
      filename = input('Input the filename to be processed\n'
                    '(or press <ENTER> to quit): ')
    file_read = open('%s%s'%(filename,FILE_EXT),READ_MODE)
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
    new_list = file_read.readline()
    
    # Encrypt or decrypt contents of message
    rotation_key = convert_rotation_key(op_str, rotation_key_str)
    text_list = process_message_list(new_list,rotation_key)
    new_name = make_name(filename, operation, rotation_key)
    ####  Display result      
    ##  translation = process_message(message,rotation_key)
    ##  print('The %s message is: %s'%(('encrypted' if op_str.lower()=='e' else 'decrypted'),translation))
    write_to_file(new_name, text_list)
  # Continuation read
  filename = input('Input the filename to be processed\n'
                    '(or press <ENTER> to quit):  ')
  file_read.close()
main()
