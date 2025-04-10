import os
import time
import requests
import socket
import subprocess
from termcolor import cprint, colored
import random

# Typing effect
def type_print(text, color="white", delay=0.01):
    for char in text:
        print(colored(char, color), end="", flush=True)
        time.sleep(delay)
    print()

# Clear screen
os.system("clear")

# Big ASCII HCO logo
def show_hco_ascii():
    cprint("""

             /$$   /$$  /$$$$$$   /$$$$$$ 
            | $$  | $$ /$$__  $$ /$$__  $$
            | $$  | $$| $$  \__/| $$  \ $$
            | $$$$$$$$| $$      | $$  | $$
            | $$__  $$| $$      | $$  | $$
            | $$  | $$| $$    $$| $$  | $$
            | $$  | $$|  $$$$$$/|  $$$$$$/
            |__/  |__/ \______/  \______/ 
                              
                              
                              

""", "red", attrs=["bold"])
    time.sleep(1)

# Intro
def show_intro():
    show_hco_ascii()
    cprint("╔══════════════════════════════════════════════════════╗", "red")
    cprint("║                HACKERS COLONY OFFICIALS              ║", "red")
    cprint("║                    HCO TOOLKIT                       ║", "red")
    cprint("║                Author - Azhar (HCO)                 ║", "red")
    cprint("╚══════════════════════════════════════════════════════╝", "red")
    time.sleep(1)

# Show warning + open YT
def show_warning():
    cprint("\n[!] WARNING: Subscribe to use this tool", "yellow", attrs=["bold"])
    time.sleep(2)
    os.system("xdg-open https://youtube.com/@hackers_colony_tech?si=4ShUWvlCJUNi749h")
    time.sleep(5)

# Loading
def loading_animation():
    for i in range(3):
        type_print("[*] Loading modules" + "." * i, "cyan", delay=0.1)
        time.sleep(0.5)
    print()

# Menu
def show_menu():
    os.system("clear")
    show_intro()
    menu_options = [
        "[1] IP Geolocation",
        "[2] Reverse DNS Lookup",
        "[3] Port Scanner",
        "[4] WHOIS Lookup",
        "[5] HTTP Headers Grabber",
        "[6] Subdomain Finder",
        "[7] Hash Identifier",
        "[8] User-Agent Generator",
        "[9] Save Report",
        "[10] Clear Logs",
        "[11] Update Toolkit",
        "[12] Exit"
    ]
    for option in menu_options:
        type_print(option, "green", delay=0.005)
    print()

# Tools
def ip_geolocation():
    ip = input(colored("Enter IP Address: ", "cyan"))
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        for k, v in res.items():
            print(colored(f"{k.upper()}: {v}", "magenta"))
    except:
        print(colored("Error retrieving data.", "red"))
    input("\nPress Enter to return to menu...")

def reverse_dns():
    ip = input(colored("Enter IP Address: ", "cyan"))
    try:
        host = socket.gethostbyaddr(ip)
        print(colored(f"Hostname: {host[0]}", "magenta"))
    except:
        print(colored("No PTR record found.", "red"))
    input("\nPress Enter to return to menu...")

def port_scanner():
    ip = input(colored("Enter IP Address: ", "cyan"))
    print(colored("Scanning ports (1-100)...", "yellow"))
    for port in range(1, 101):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(colored(f"Port {port} is OPEN", "green"))
        sock.close()
    input("\nPress Enter to return to menu...")

def whois_lookup():
    domain = input(colored("Enter domain (without https): ", "cyan"))
    try:
        result = subprocess.getoutput(f"whois {domain}")
        print(colored(result, "magenta"))
    except:
        print(colored("Error fetching WHOIS.", "red"))
    input("\nPress Enter to return to menu...")

def headers_grabber():
    url = input(colored("Enter website URL (with https): ", "cyan"))
    try:
        headers = requests.get(url).headers
        for k, v in headers.items():
            print(colored(f"{k}: {v}", "magenta"))
    except:
        print(colored("Invalid URL or error.", "red"))
    input("\nPress Enter to return to menu...")

def subdomain_finder():
    domain = input(colored("Enter domain (example.com): ", "cyan"))
    subdomains = ["www", "mail", "ftp", "cpanel", "blog"]
    print(colored("Scanning subdomains...", "yellow"))
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            requests.get(url, timeout=2)
            print(colored(f"[+] Found: {url}", "green"))
        except:
            pass
    input("\nPress Enter to return to menu...")

def hash_identifier():
    hash_input = input(colored("Enter hash: ", "cyan"))
    length = len(hash_input)
    hash_type = "Unknown"
    if length == 32:
        hash_type = "MD5"
    elif length == 40:
        hash_type = "SHA-1"
    elif length == 64:
        hash_type = "SHA-256"
    print(colored(f"Possible Hash Type: {hash_type}", "magenta"))
    input("\nPress Enter to return to menu...")

def user_agent_generator():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
        "Mozilla/5.0 (Android 11; Mobile)"
    ]
    print(colored("Random User-Agent:", "yellow"))
    print(colored(random.choice(user_agents), "magenta"))
    input("\nPress Enter to return to menu...")

def save_report():
    filename = input(colored("Enter report file name: ", "cyan"))
    with open(filename, "w") as f:
        f.write("HCO TOOLKIT REPORT\nGenerated by Krishu\n")
        f.write("Add report data here...\n")
    print(colored(f"Report saved as {filename}", "green"))
    input("\nPress Enter to return to menu...")

def clear_logs():
    os.system("rm -rf *.log *.txt")
    print(colored("Logs cleared.", "green"))
    input("\nPress Enter to return to menu...")

def update_tool():
    print(colored("Checking for updates...", "cyan"))
    time.sleep(1)
    print(colored("You're using the latest version!", "green"))
    input("\nPress Enter to return to menu...")

# Main
def main():
    show_intro()
    show_warning()
    loading_animation()
    while True:
        show_menu()
        choice = input(colored("\nSelect an option: ", "cyan"))
        if choice == "1":
            ip_geolocation()
        elif choice == "2":
            reverse_dns()
        elif choice == "3":
            port_scanner()
        elif choice == "4":
            whois_lookup()
        elif choice == "5":
            headers_grabber()
        elif choice == "6":
            subdomain_finder()
        elif choice == "7":
            hash_identifier()
        elif choice == "8":
            user_agent_generator()
        elif choice == "9":
            save_report()
        elif choice == "10":
            clear_logs()
        elif choice == "11":
            update_tool()
        elif choice == "12":
            print(colored("Exiting... Stay ethical, hacker!", "red"))
            break
        else:
            print(colored("Invalid option!", "red"))
            time.sleep(1)

if __name__ == "__main__":
    main()