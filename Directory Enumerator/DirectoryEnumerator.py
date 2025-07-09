import requests

url = input("Enter the target URL (e.g. http://example.com): ").strip('/')

wordlist = ['admin', 'login', 'config', 'uploads', '.git', 'backup']

print(f"\n[*] Starting directory enumeration on {url}\n")

for word in wordlist:
    targetURL = f"{url}/{word}/"
    try:
        response = requests.get(targetURL, timeout=3)
        if response.status_code in [200, 301, 302, 403]:
            print(f"[+] Found: {targetURL} (Status: {response.status_code})")
    except requests.RequestException:
        pass

print("\n[+] Scan complete.")