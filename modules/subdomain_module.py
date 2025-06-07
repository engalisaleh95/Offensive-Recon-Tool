import requests

def fetch_crtsh(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    subdomains = set()

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            raw_data = response.json()
            for entry in raw_data:
                name = entry.get('name_value', '')
                for sub in name.split('\n'):
                    if sub.endswith(domain):
                        subdomains.add(sub.strip())
    except Exception as e:
        subdomains.add(f"[!] crt.sh error: {e}")
    return subdomains

def run_subdomain_enum(domain):
    output = []
    output.append(f"=== Subdomain Enumeration for {domain} ===")
    
    
    otx_api_key = "5391b2a6a8a5b41d5d5f5a0bc306e1845d85a622fb5b90c906c1b5e6a1cc9486"
    
    crt_subs = fetch_crtsh(domain)
    all_subs = sorted(crt_subs)

    if all_subs:
        output.append(f"[+] Found {len(all_subs)} subdomains:")
        for sub in all_subs:
            output.append(f"  - {sub}")
    else:
        output.append("[!] No subdomains found.")
    return output
