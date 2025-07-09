import re

def identify_hash(hash_str):
    hash_str = hash_str.strip()
    hash_len = len(hash_str)

    candidates = []

    HASHES = {
        32: ["MD5"],
        40: ["SHA-1", "RIPEMD-160"],
        56: ["SHA-224"],
        64: ["SHA-256"],
        96: ["SHA-384"],
        128: ["SHA-512"],
        16: ["MySQL3.x", "DES(Unix)"],
        13: ["DES(Unix)"],
        34: ["MD5(phpBB3, Joomla)", "Haval-128"]
    }

    if re.fullmatch(r"[a-fA-F0-9]+", hash_str):
        if hash_len in HASHES:
            candidates.extend(HASHES[hash_len])
    elif re.fullmatch(r"[a-fA-F0-9+/=]+", hash_str):
        candidates.append("Possibly base64 or bcrypt")

    if hash_str.startswith("$1$"):
        candidates.append("MD5 Crypt")
    elif hash_str.startswith("$2a$") or hash_str.startswith("$2b$") or hash_str.startswith("$2y$"):
        candidates.append("bcrypt")
    elif hash_str.startswith("$5$"):
        candidates.append("SHA-256 Crypt")
    elif hash_str.startswith("$6$"):
        candidates.append("SHA-512 Crypt")

    return candidates if candidates else ["Unknown or unsupported hash type"]

if __name__ == "__main__":
    user_input = input("Enter hash: ").strip()
    result = identify_hash(user_input)
    print("\nPossible hash types: ")
    for algo in result:
        print(f" - {algo}")