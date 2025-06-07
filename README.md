# Offensive Recon Tool

## Purpose
Automated CLI tool for reconnaissance during penetration testing.

## Features
- WHOIS Lookup
- DNS Record Enumeration
- Subdomain Enumeration (`crt.sh`, AlienVault OTX)
- Port Scanning
- Banner Grabbing
- Web Technology Detection (`WhatWeb`, optional BuiltWith)

## Usage

```bash
python main.py --target example.com --whois --dns --subdomains --portscan --tech


Flag                                                        	Description
--target	                                                    (Required) Target domain
--whois	                                                        Perform WHOIS lookup
--dns	                                                        Enumerate A, MX, TXT, NS
--subdomains	                                                Find subdomains via crt.sh + OTX
--portscan	                                                    Scan common ports
--tech	                                                        Detect web stack (WhatWeb)