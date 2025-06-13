import requests

def fetch_crtsh(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    subdomains = set()

    try:
        response = requests.get(url, headers=headers, timeout=20)
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


def fetch_otx(domain, api_key):
    subdomains = set()
    headers = {
        "X-OTX-API-KEY": api_key,
        "User-Agent": "Mozilla/5.0"
    }
    try:
        response = requests.get(
            f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns",
            headers=headers,
            timeout=20
        )
        if response.status_code == 200:
            data = response.json()
            for record in data.get("passive_dns", []):
                hostname = record.get("hostname", "")
                if hostname.endswith(domain):
                    subdomains.add(hostname.strip())
    except Exception as e:
        subdomains.add(f"[!] OTX error: {e}")
    return subdomains


def run_subdomain_enum(domain):
    output = []
    output.append(f"=== Subdomain Enumeration for {domain} ===")

    otx_api_key = "5391b2a6a8a5b41d5d5f5a0bc306e1845d85a622fb5b90c906c1b5e6a1cc9486"

    crt_subs = fetch_crtsh(domain)
    otx_subs = fetch_otx(domain, otx_api_key)

    all_subs = sorted(set(crt_subs).union(otx_subs))

    if all_subs:
        output.append(f"[+] Found {len(all_subs)} subdomains:")
        for sub in all_subs:
            output.append(f"  - {sub}")
    else:
        output.append("[!] No subdomains found.")

    return output