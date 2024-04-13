def encode(password):
    encoded_password = ''
    for num in password:
        if num.isdigit():
            encoded_number = str((int(num) + 3) % 10)
            encoded_password += encoded_number
    return encoded_password

# BDS decode function
def decode(encoded_password):
    decoded_password = ''
    for num in encoded_password:
        decoded_number = str((int(num) - 3) % 10)
        decoded_password += decoded_number
    return decoded_password



if __name__ == '__main__':
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode\n"
              "2. Decode\n"
              "3. Quit")
        choice = int(input("Please enter an option: "))
        password_input = input("Please enter your password to encode: ")
        if password_input.isnumeric():
            print("Your password has been encoded and stored!")
        else:
            print("Invalid password, please try again.")
        if choice == 1:
            encoded_password = encode(password_input)
            print(encoded_password)
        elif choice == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        else:
            break
            
