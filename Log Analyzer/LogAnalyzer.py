import re
from collections import Counter

log_path = input("Enter path to log file: ").strip()

log_pattern = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+-\s+-\s+\[.*?\]\s+"(?P<method>\w+)\s+(?P<url>.*?)\s+HTTP/[\d.]+"\s+(?P<status>\d{3})'
)

ip_counter = Counter()
method_counter = Counter()
status_counter = Counter()
url_counter = Counter()

with open(log_path, 'r', encoding='utf-8', errors='ignore') as log_file:
    for line in log_file:
        match = log_pattern.search(line)
        if match:
            ip = match.group('ip')
            method = match.group('method')
            status = match.group('status')
            url = match.group('url')

            ip_counter[ip] += 1
            method_counter[method] += 1
            status_counter[status] += 1
            url_counter[url] += 1

print("\n🔍 Log Analysis Summary:\n")

print("📊 Top 10 IP addresses:")
for ip, count in ip_counter.most_common(10):
    print(f"{ip}: {count} requests")

print("\n📊 HTTP Methods Used:")
for method, count in method_counter.items():
    print(f"{method}: {count}")

print("\n📊 Response Status Codes:")
for code, count in status_counter.items():
    print(f"{code}: {count}")

print("\n📊 Top 10 Requested URLs:")
for url, count in url_counter.most_common(10):
    print(f"{url}: {count}")
