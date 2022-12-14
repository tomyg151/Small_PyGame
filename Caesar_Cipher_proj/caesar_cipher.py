alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  """check if user input 'decod' or 'incode', run on the string and each letter that the function found's
  it's shifted the letter in the alphabet by the number that the user give's as input (called shifted_number).
  in the end print the string after shifting all the letter in the string.
  """
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:


# keep the number/symbol/space when the text is encoded/decoded?
# e.g. start_text = "meet me at 3"
# end_text = "•••• •• •• 3"

    if(char in alphabet):
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      position = start_text.index(char)
      end_text += start_text[position]
  print(f"Here's the {cipher_direction}d result: {end_text}")

"""print the game logo"""
from Art import logo
print(logo)


#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
flag = True
while flag:


  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?

  if(shift > 26 ):
    shift %= 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  to_continue = input("Type 'yes' if you want to continue , Type 'no' to stop the program\n").lower()
  if(to_continue == "no"):
    flag = False
    print("Goodbye")
