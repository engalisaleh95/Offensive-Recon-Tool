import argparse
from modules import report_module
from modules import whois_module
from modules import dns_module
from modules import subdomain_module
from modules import portscan_module
from modules import techdetect_module
import datetime


def timestamped(msg):
    now = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{now} {msg}")


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
    parser.add_argument('--all', action='store_true', help='Run all modules')

    args = parser.parse_args()

    print(f" Target: {args.target}")
    report_file = report_module.init_report(args.target)

    # If --all is used, set all flags to True
    if args.all:
        args.whois = args.dns = args.subdomains = args.portscan = args.tech = True

    if args.whois:
        timestamped("Running WHOIS module...")
        output = whois_module.run_whois(args.target)
        report_module.append_to_report(report_file, "WHOIS", output)

    if args.dns:
        timestamped("Running DNS module...")
        output = dns_module.run_dns_enum(args.target)
        report_module.append_to_report(report_file, "DNS", output)

    if args.subdomains:
        timestamped("Running Subdomain module...")
        output = subdomain_module.run_subdomain_enum(args.target)
        report_module.append_to_report(report_file, "Subdomains", output)

    if args.portscan:
        timestamped("Running PortScan module...")
        output = portscan_module.run_port_scan(args.target)
        report_module.append_to_report(report_file, "PortScan", output)

    if args.tech:
        timestamped("Running TechDetect module...")
        output = techdetect_module.run_tech_detect(args.target)
        report_module.append_to_report(report_file, "TechDetect", output)

    timestamped("Report Generated!")


if __name__ == "__main__":
    main()
