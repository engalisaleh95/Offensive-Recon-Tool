import datetime
import socket

def init_report(domain):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    ip = "N/A"
    try:
        ip = socket.gethostbyname(domain)
    except:
        pass

    report_name = f"reports/report_{domain.replace('.', '_')}_{timestamp}.txt"
    with open(report_name, "w", encoding="utf-8") as f:
        f.write("=== RECON REPORT ===\n")
        f.write(f"Target     : {domain}\n")
        f.write(f"Resolved IP: {ip}\n")
        f.write(f"Timestamp  : {timestamp}\n")
        f.write("=" * 40 + "\n\n")

    return report_name


def append_to_report(report_name, section_title, content_lines):
    with open(report_name, "a", encoding="utf-8") as f:
        f.write(f"## {section_title} ##\n")
        for line in content_lines:
            f.write(f"{line}\n")
        f.write("\n")
