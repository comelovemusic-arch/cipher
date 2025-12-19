from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

KEY_FILE = Path("secret.key")
ENCRYPTED_FILE = Path("message.enc")


def pause():
    input("\nPress Enter to continue...")


def generate_and_save_key(overwrite: bool = False) -> None:
    if KEY_FILE.exists() and not overwrite:
        raise FileExistsError("secret.key already exists.")
    KEY_FILE.write_bytes(Fernet.generate_key())


def load_key() -> bytes:
    if not KEY_FILE.exists():
        raise FileNotFoundError("secret.key not found. Generate a key first (option 1).")
    key = KEY_FILE.read_bytes()
    if len(key) < 40:
        raise ValueError("secret.key looks corrupted/invalid.")
    return key


def encrypt_to_file(message: str) -> None:
    if not message.strip():
        raise ValueError("Message cannot be empty.")
    key = load_key()
    token = Fernet(key).encrypt(message.encode("utf-8"))
    ENCRYPTED_FILE.write_bytes(token)


def decrypt_from_file() -> str:
    if not ENCRYPTED_FILE.exists():
        raise FileNotFoundError("message.enc not found. Encrypt first (option 2).")

    key = load_key()
    token = ENCRYPTED_FILE.read_bytes()

    try:
        plaintext = Fernet(key).decrypt(token)
        return plaintext.decode("utf-8")
    except InvalidToken:
        return (
            "❌ Decryption failed.\n"
            "Most common causes:\n"
            "- You overwrote secret.key after encrypting\n"
            "- message.enc got edited/corrupted\n"
            "- You are running the script from a different folder\n"
        )


def menu() -> str:
    print("\nSecure File-Based Messaging System")
    print(f"Working folder:  {Path.cwd()}")
    print(f"Key file:        {KEY_FILE.resolve()}")
    print(f"Encrypted file:  {ENCRYPTED_FILE.resolve()}\n")
    print("1) Generate New Key")
    print("2) Encrypt Message → file")
    print("3) Decrypt Message ← file")
    print("4) Exit")
    return input("Select an option (1-4): ").strip()


def main() -> None:
    while True:
        choice = menu()

        if choice == "1":
            try:
                if KEY_FILE.exists():
                    ans = input("secret.key exists. Overwrite? (y/n): ").strip().lower()
                    if ans != "y":
                        print("Cancelled.")
                        pause()
                        continue
                    generate_and_save_key(overwrite=True)
                else:
                    generate_and_save_key()
                print("✅ Key generated and saved as secret.key")
            except Exception as e:
                print(f"❌ {e}")
            pause()

        elif choice == "2":
            try:
                msg = input("Enter message to encrypt: ")
                encrypt_to_file(msg)
                print(f"✅ Encrypted message saved to: {ENCRYPTED_FILE.resolve()}")
            except Exception as e:
                print(f"❌ {e}")
            pause()

        elif choice == "3":
            try:
                msg = decrypt_from_file()
                print("\nDecrypted message:")
                print(msg)
            except Exception as e:
                print(f"❌ {e}")
            pause()

        elif choice == "4":
            print("Bye 👋")
            break

        else:
            print("Invalid choice.")
            pause()


if __name__ == "__main__":
    main()

