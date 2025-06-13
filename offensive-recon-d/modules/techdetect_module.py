import subprocess

def run_tech_detect(domain):
    output = []
    output.append(f"=== Technology Detection for {domain} ===")

    try:
        # Use default system-installed whatweb
        command = ["whatweb", domain]
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        if result.stdout:
            output.append(result.stdout.strip())
        else:
            output.append("[!] No output from WhatWeb.")
    except FileNotFoundError:
        output.append("[!] WhatWeb not found. Make sure it is installed and in PATH.")
    except Exception as e:
        output.append(f"[!] WhatWeb error: {e}")

    return output
