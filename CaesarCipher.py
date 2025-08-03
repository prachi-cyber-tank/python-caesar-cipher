def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Program ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Use 'E' or 'D'.")
        return

    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter shift value (number): "))
    except ValueError:
        print("Invalid input. Please enter a number for shift.")
        return

    if choice == 'e':
        result = caesar_encrypt(message, shift)
        print("\nEncrypted Message:", result)
    else:
        result = caesar_decrypt(message, shift)
        print("\nDecrypted Message:", result)

if __name__ == "__main__":
    main()
