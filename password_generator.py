import random
import string

def generate_password(length=12):
    """
    Generate a random password with the specified length.
    The password will contain a mix of uppercase letters, 
    lowercase letters, digits, and punctuation symbols.
    
    :param length: Length of the password (default is 12)
    :return: Generated password as a string
    """

    # Define the character set to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices to select 'length' number of characters from the set
    password = ''.join(random.choices(characters, k=length))

    return password

def main():
    """
    Main function to run the password generator.
    Prompts the user for password length and generates a password.
    """

    print("Welcome to the Password Generator!")

    # Ask the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 4:
                print("Password length should be at least 4.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    # Run the main function
    main()
