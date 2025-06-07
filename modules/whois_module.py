import whois as pywhois
import datetime

def run_whois(domain):
    output = []
    try:
        output.append(f"=== WHOIS for {domain} ===")
        data = pywhois.whois(domain)

        output.append(f"Registrar       : {data.registrar}")
        output.append(f"Creation Date   : {data.creation_date}")
        output.append(f"Expiration Date : {data.expiration_date}")
        output.append(f"Name Servers    : {data.name_servers}")
        output.append(f"Emails          : {data.emails}")

    except Exception as e:
        output.append(f"[!] Error during WHOIS lookup: {e}")
    
    return output
