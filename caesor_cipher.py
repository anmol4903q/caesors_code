# 🔐 Caesar Cipher - Encryption & Decryption Tool in Python

# 📜 List of lowercase alphabets used for shifting
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z']

print("👋 Welcome to Caesar Cipher Codes!")

# 🔒 Function to encrypt a message
def encrypt(msg, shift):
    result = ""
    for n in msg:
        if n in alphabets:
            pos = alphabets.index(n)              # 🔍 Get index of current letter
            n_pos = (pos + shift) % 26            # 🔁 Shift and wrap using modulo
            result += alphabets[n_pos]            # ➕ Add shifted letter
        else:
            result += n                           # ❗ Keep non-alphabet characters unchanged
    print(f"🔐 Your encoded word is: {result}")
    print("*" * 90)

# 🔓 Function to decrypt a message
def decrypt(msg, shift):
    result2 = ""
    for n in msg:
        if n in alphabets:
            pos = alphabets.index(n)              # 🔍 Find current position
            n_pos = (pos - shift) % 26            # 🔁 Reverse shift using modulo
            result2 += alphabets[n_pos]           # ➕ Add decrypted letter
        else:
            result2 += n                          # ❗ Keep non-alphabet characters unchanged
    print(f"🔓 Your decoded word is: {result2}")
    print("*" * 90)

# 🔁 Loop: Keeps running until user says no
ch = "Y"
while ch == "Y":
    # 🎛️ Get user choice
    e_d = input("✏️ Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
    
    # 📝 Message and shift input
    msg = input("📩 Type your message here: ")
    shift = int(input("🔢 Enter how many shifts you want: "))

    # 🧠 Decision-making
    if e_d == "encode":
        encrypt(msg, shift)

    if e_d == "decode":
        decrypt(msg, shift)

    # 🔄 Ask to continue or stop
    ch = input("🔁 Do you want to run it again? (Y/N): ").upper()



