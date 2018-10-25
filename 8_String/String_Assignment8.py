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
  return ((negative_count <= 1 and comparator.isdigit()) and int(comparator) !=0
