# 🕵️ Offensive Recon Tool
The Offensive Recon Tool is an automated CLI-based reconnaissance framework designed for cybersecurity tasks. It helps you gather critical domain intel using a combination of Python modules and external tools.
## 📌 Features
- ✅ WHOIS Lookup  
- ✅ DNS Enumeration (A, MX, TXT, NS records)  
- ✅ Subdomain Enumeration (via `crt.sh`)  
- ✅ Port Scanning & Banner Grabbing  
- ✅ Technology Detection (via WhatWeb)  
- ✅ Full Report Generation (`.txt`)  
- ✅ Silent CLI output with timestamped progress  
- ✅ Supports `--all` flag to run everything at once  
- ✅ Works both **locally** and in **Docker**

## 🧠 Requirements
### Python Packages (installed via `requirements.txt`)
requests
dnspython
python-whois
### External Tools
- **WhatWeb** (required for tech detection)
- Git, Ruby (for installing WhatWeb)
## 🛠️ Local Usage (No Docker)
### 1. Install Python dependencies:
```bash
pip install -r requirements.txt
2. Install WhatWeb (one-time):
sudo apt update
sudo apt install git ruby ruby-dev build-essential libyaml-dev
git clone https://github.com/urbanadventurer/WhatWeb.git /opt/WhatWeb
cd /opt/WhatWeb
sudo gem install bundler
bundle install
sudo ln -s /opt/WhatWeb/whatweb /usr/local/bin/whatweb

3. Run the tool:
Run a single module:
python main.py --target example.com --whois
Run all modules:
python main.py --target example.com --all

🐳 Docker Usage
1. Build the Docker image:
docker build -t offensive-recon .
2. Run the tool in Docker:
🔁 Always use -v "%cd%":/app to mount current folder and save reports

Run all modules:
docker run -v "%cd%":/app offensive-recon python main.py --target example.com --all
Run a single module:
docker run -v "%cd%":/app offensive-recon python main.py --target example.com --whois
docker run -v "%cd%":/app offensive-recon python main.py --target example.com --dns
docker run -v "%cd%":/app offensive-recon python main.py --target example.com --subdomains
docker run -v "%cd%":/app offensive-recon python main.py --target example.com --portscan
docker run -v "%cd%":/app offensive-recon python main.py --target example.com --tech
🧾 Output Report
All results are saved in a .txt file automatically.
Format:
report_<domain>_<timestamp>.txt

Example:
report_google_com_2025-06-10_14-45-33.txt

🔇 Silent CLI Output
When you run the tool, the terminal shows only:
Target: example.com
[10:30:45] Running WHOIS Module...
[10:30:50] Running DNS Module...
...
[10:32:10] Report Generated!
✔ The actual data is saved silently to a .txt report.

🧪 Sample Full Command (Docker + all modules)
docker run -v "%cd%":/app offensive-recon python main.py --target aub.edu.lb --all

⚠️ Notes & Troubleshooting
•	If WhatWeb fails, check your internet or increase timeout.
•	Make sure whatweb is available in Docker path (/usr/local/bin).
•	Subdomain enumeration uses crt.sh, so results depend on its uptime.
•	Report will be saved in the same folder whether run locally or via Docker.
