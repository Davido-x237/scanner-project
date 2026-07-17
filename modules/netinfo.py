"""
============================================================
Cyber Recon Toolkit
Module  : Network Information
Version : 2.0
Author  : David Didomi
============================================================
"""

import os
import socket
import platform
import uuid
from datetime import datetime

# ==========================================================
# CONFIGURATION
# ==========================================================

VERSION = "2.0"

REPORT_FILE = "reports/network_info_report.txt"
LOG_FILE = "logs/network_info.log"

# ==========================================================
# INITIALIZATION
# ==========================================================

def ensure_directories():
    """
    Create project folders if they do not already exist.
    """

    os.makedirs("reports", exist_ok=True)
    os.makedirs("logs", exist_ok=True)


# ==========================================================
# USER INTERFACE
# ==========================================================

def print_banner():

    print("\n" + "=" * 60)
    print("          CYBER RECON TOOLKIT")
    print("           Network Information")
    print(f"              Version {VERSION}")
    print("=" * 60)


# ==========================================================
# INFORMATION FUNCTIONS
# ==========================================================

def get_hostname():

    return socket.gethostname()


def get_local_ip():

    try:
        return socket.gethostbyname(socket.gethostname())

    except Exception:
        return "Unavailable"


def get_operating_system():

    return platform.system()


def get_os_version():

    return platform.version()


def get_machine():

    return platform.machine()


def get_processor():

    processor = platform.processor()

    if processor:
        return processor

    return "Unavailable"


def get_python_version():

    return platform.python_version()


def get_mac_address():

    mac = uuid.getnode()

    mac = ':'.join((
        f"{(mac >> ele) & 0xff:02X}"
        for ele in range(40, -1, -8)
    ))

    return mac


# ==========================================================
# LOGGING
# ==========================================================

def write_log(message):

    with open(LOG_FILE, "a") as log:

        log.write(
            f"[{datetime.now()}] {message}\n"
        )


# ==========================================================
# REPORTING
# ==========================================================

def write_report(info):

    with open(REPORT_FILE, "a") as report:

        report.write("\n")
        report.write("=" * 60 + "\n")
        report.write("NETWORK INFORMATION REPORT\n")
        report.write("=" * 60 + "\n")
        report.write(f"Date : {datetime.now()}\n\n")

        for key, value in info.items():

            report.write(f"{key:<20}: {value}\n")

# ==========================================================
# MAIN PROGRAM
# ==========================================================

def display_information(info):
    """
    Display the collected network information.
    """

    print("\n" + "=" * 60)
    print("              NETWORK INFORMATION")
    print("=" * 60)

    for key, value in info.items():
        print(f"{key:<20}: {value}")

    print("=" * 60)


# ==========================================================
# COLLECT INFORMATION
# ==========================================================

def collect_information():
    """
    Collect all available system and network information.
    """

    information = {
        "Hostname": get_hostname(),
        "Local IP": get_local_ip(),
        "Operating System": get_operating_system(),
        "OS Version": get_os_version(),
        "Machine": get_machine(),
        "Processor": get_processor(),
        "Python Version": get_python_version(),
        "MAC Address": get_mac_address()
    }

    return information


# ==========================================================
# MAIN
# ==========================================================

def main():

    ensure_directories()

    print_banner()

    information = collect_information()

    display_information(information)

    write_report(information)

    write_log("Network information collected successfully.")

    print("\n✅ Report saved to:", REPORT_FILE)
    print("✅ Log saved to:", LOG_FILE)


# ==========================================================
# PROGRAM ENTRY
# ==========================================================

if __name__ == "__main__":
    main()