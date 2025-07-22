import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

LOGO = r"""

 _____ __   _ ______  _     _         ______ _______ __   _ _______ _____ _______
   |   | \  | |     \ |     | |      |  ____ |______ | \  |    |      |   |_____|
 __|__ |  \_| |_____/ |_____| |_____ |_____| |______ |  \_|    |    __|__ |     |


By KL3FT3Z (https://github.com/toxy4ny)
"""

def banner():

    os.system("cls" if os.name == "nt" else "clear")
    print(LOGO)
    print("😈 OSINT Subdomain Finder in Certificate Transparency\n")

def get_subdomains(domain):
    url = f"https://crt.sh/?q={domain}&output=json"
    print(f"😈 Getting subdomains for {domain} through crt.sh ...")
    resp = requests.get(url, timeout=30)
    if resp.status_code != 200:
        print(f"👿 Couldn't get the data in crt.sh (Error Code {resp.status_code})")
        return []
    try:
        data = resp.json()
    except json.JSONDecodeError:
        print("👿 The JSON response could not be decoded.")
        return []
    subdomains = set()
    for entry in data:
        name = entry.get("common_name")
        if name and domain in name:
            subdomains.add(name.lower())
    return sorted(subdomains)

def check_alive(subdomain):
    for proto in ['https', 'http']:
        try:
            r = requests.get(f"{proto}://{subdomain}", timeout=5, verify=False)
            if r.status_code < 400:
                return proto, r.status_code
        except Exception:
            continue
    return None, None

def main():
    banner()
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    domain = input("😈 Enter the domain (for example, example.com ): ").strip()
    subdomains = get_subdomains(domain)
    if not subdomains:
        print("👿 No subdomains were found.")
        return

    print(f"😈 Found {len(subdomains)} subdomains. Check alive on Internet...")

    alive = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_sub = {executor.submit(check_alive, sub): sub for sub in subdomains}
        for future in as_completed(future_to_sub):
            sub = future_to_sub[future]
            proto, code = future.result()
            if proto:
                print(f"😈 {proto}://{sub} [{code}]")
                alive.append(f"{proto}://{sub} [{code}]")

   
    with open(f"{domain}_subdomains.txt", "w") as f:
        for sub in subdomains:
            f.write(sub + "\n")
    with open(f"{domain}_alive.txt", "w") as f:
        for line in alive:
            f.write(line + "\n")

    print(f"\n😈 All subdomains are saved in {domain}_subdomains.txt")
    print(f"😈 The available subdomains from the Internet are saved in {domain}_alive.txt")

if __name__ == "__main__":
    main()