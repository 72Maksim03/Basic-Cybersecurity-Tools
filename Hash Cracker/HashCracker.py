import hashlib

def hashCrack(targetHash, algorithm, wordlist_path):
    try:
        with open(wordlist_path) as f:
            for line in f:
                word = line.strip()
                if not word:
                    continue

                hashedWord = hashWord(word, algorithm)

                if hashedWord == targetHash.lower():
                    print(f"Match found: {word}")
                    return
                
            print("\n[-] Password not found in wordlist.")
    except FileNotFoundError:
        print("Wordlist file not found.")

def hashWord(word, algorith):
    algo = algorith.lower()
    encoded = word.encode("utf-8")

    if algo == "md5":
        return hashlib.md5(encoded).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(encoded).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(encoded).hexdigest()
    elif algo == "sha512":
        return hashlib.sha512(encoded).hexdigest()
    else:
        raise ValueError("Unsupported algorithm")
    
if __name__ == "__main__":
    targetHash = input("Enter hash to crack: ").strip()
    algorithm = input("Enter hash algorithm (md5, sha1, sha256, sha512): ").strip()
    wordListPath = input("Enter path to wordlist file: ").strip()

    hashCrack(targetHash, algorithm, wordListPath)