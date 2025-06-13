import socket

def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip, port))
        banner = sock.recv(1024).decode(errors="ignore").strip()
        sock.close()
        return banner if banner else "No banner returned."
    except Exception:
        return "No banner grabbed."

def run_port_scan(domain, ports=[80, 443, 21, 22, 25, 8080]):
    output = []
    output.append(f"=== PORT SCAN for {domain} ===")

    try:
        ip = socket.gethostbyname(domain)
        output.append(f"[+] Resolved IP: {ip}")
    except Exception as e:
        output.append(f"[!] Failed to resolve domain: {e}")
        return output

    open_ports = []

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
                output.append(f"[OPEN] Port {port}")
            sock.close()
        except Exception as e:
            output.append(f"[!] Error on port {port}: {e}")

    output.append("--- Banner Grabbing ---")
    for port in open_ports:
        banner = grab_banner(ip, port)
        output.append(f"[Port {port}] {banner}")

    return output
