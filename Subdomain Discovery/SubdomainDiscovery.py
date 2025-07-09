import socket

domain = input("Enter the target domain (e.g. example.com): ").strip()

subdomains = ['www', 'admin', 'test', 'dev', 'mail', 'ftp', 'api', 'blog']

print(f"\n[*] Starting subdomain discovery on {domain}\n")

foundAny = False

for sub in subdomains:
    full_domain = f"{sub}.{domain}"
    try:
        ip = socket.gethostbyname(full_domain)
        print(f"[+] Found: {full_domain} → {ip}")
        foundAny = True
    except socket.gaierror:
        pass

if not foundAny:
    print("[-] No subdomains found.")

print("\n[+] Scan complete.")