import subprocess

def run_tech_detect(domain):
    output = []
    output.append(f"=== Technology Detection for {domain} ===")

    path_to_whatweb = r"C:\Users\mhmd pc\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts\whatweb.exe"

    try:
        command = [path_to_whatweb, domain]
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)
        if result.stdout:
            output.append(result.stdout.strip())
        else:
            output.append("[!] No output from WhatWeb.")
    except Exception as e:
        output.append(f"[!] WhatWeb error: {e}")

    return output
