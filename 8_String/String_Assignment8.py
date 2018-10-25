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
