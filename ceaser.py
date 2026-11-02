"""Ceaser Cipher Tool: encrypt, decrypt and brute-force crack text."""

def shift_text(text, shift):
    """Shift every letter by `shift` places. Other characters stay the same."""
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def encrypt(text, shift):
    return shift_text(text, shift)


def decrypt(text, shift):
    return shift_text(text, -shift)


def brute_force(text):
    """Print the text decrypted with every possible shift."""
    print("\nAll possible shifts:\n")
    for shift in range(1, 26):
        print(f"Shift {shift:2}: {decrypt(text, shift)}")


def get_shift():
    """Keep asking until the user enters a whole number from 1 to 25."""
    while True:
        value = input("Enter shift (1-25): ").strip()
        if value.isdigit() and 1 <= int(value) <= 25:
            return int(value)
        print("Please enter a whole number between 1 and 25.")


def get_message():
    """Keep asking until the user enters something."""
    while True:
        message = input("Enter message: ")
        if message.strip():
            return message
        print("Message cannot be empty.")


def main():
    while True:
        print("\n=== Caesar Cipher Tool ===")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Brute-force crack (try all 25 shifts)")
        print("4. Quit")

        choice = input("\nChoose: ").strip()

        if choice == "1":
            message = get_message()
            shift = get_shift()
            print("Result:", encrypt(message, shift))
        elif choice == "2":
            message = get_message()
            shift = get_shift()
            print("Result:", decrypt(message, shift))
        elif choice == "3":
            message = get_message()
            brute_force(message)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()