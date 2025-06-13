import dns.resolver

def run_dns_enum(domain):
    output = []
    output.append(f"=== DNS ENUMERATION for {domain} ===")

    # Remove 'www.' if present
    if domain.startswith("www."):
        domain = domain[4:]

    record_types = ['A', 'MX', 'TXT', 'NS']
    for rtype in record_types:
        output.append(f"[{rtype} Records]")
        try:
            answers = dns.resolver.resolve(domain, rtype)
            for rdata in answers:
                output.append(f"  - {rdata}")
        except Exception as e:
            output.append(f"  [!] Error: {rtype} - {e}")

    return output
