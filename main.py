import argparse
from modules import report_module
from modules import whois_module
from modules import dns_module
from modules import subdomain_module
from modules import portscan_module
from modules import techdetect_module


def main():
    parser = argparse.ArgumentParser(
        description="🕵️ Offensive Recon Tool - Automate recon tasks."
    )
    parser.add_argument('--target', required=True, help='Target domain (e.g., example.com)')
    parser.add_argument('--whois', action='store_true', help='Run WHOIS lookup')
    parser.add_argument('--dns', action='store_true', help='Run DNS enumeration')
    parser.add_argument('--subdomains', action='store_true', help='Run Subdomain Enumeration')
    parser.add_argument('--portscan', action='store_true', help='Run Port Scan')
    parser.add_argument('--tech', action='store_true', help='Detect web technologies')
  

    args = parser.parse_args()

    print(f" Target: {args.target}")
    
    report_file = report_module.init_report(args.target)

    if args.whois:
        print("\n[WHOIS Module]")
        output = whois_module.run_whois(args.target)
        for line in output:
            print(line)
        report_module.append_to_report(report_file, "WHOIS", output)

    #if args.whois:
     #   print("\n[WHOIS Module]")
      #  whois_module.run_whois(args.target)

    if args.dns:  
        print("\n[DNS Module]")
        output = dns_module.run_dns_enum(args.target)
        for line in output:
            print(line)
        report_module.append_to_report(report_file, "DNS", output)

    if args.subdomains:
        print("\n[Subdomain Module]")
        output = subdomain_module.run_subdomain_enum(args.target)
        for line in output:
            print(line)
        report_module.append_to_report(report_file, "Subdomain", output)

    if args.portscan:
        print("\n[Port Scan Module]")
        output = portscan_module.run_port_scan(args.target)
        for line in output:
            print(line)
        report_module.append_to_report(report_file, "PortScan", output)

    if args.tech:
        print("\n[Technology Detection Module]")
        output = techdetect_module.run_tech_detect(args.target)
        for line in output:
            print(line)
        report_module.append_to_report(report_file, "TechDetect", output)    

if __name__ == "__main__":
    main()
