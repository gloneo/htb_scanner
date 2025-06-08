import subprocess
import argparse
import pyfiglet
from rich import print
from rich.console import Console
from prompt_toolkit import prompt

console = Console()

def port_scan(target):
    print("[bold cyan]1. Running port scan with Nmap...[/bold cyan]")
    command = f"nmap -p- -T4 -sV {target}"
    subprocess.run(command, shell=True)

def tech_detection(target):
    print("[bold cyan]2. Detecting web technologies with WhatWeb...[/bold cyan]")
    command = f"whatweb http://{target}"
    subprocess.run(command, shell=True)

def dir_enum(target, wordlist):
    print("[bold cyan]3. Directory enumeration with Dirb...[/bold cyan]")
    command = f"dirb http://{target} {wordlist}"
    subprocess.run(command, shell=True)

def subdomain_enum(target, wordlist):
    print("[bold cyan]4. Subdomain enumeration with ffuf...[/bold cyan]")
    command = f"ffuf -w {wordlist} -u http://{target} -H \"Host: FUZZ.{target}\""
    subprocess.run(command, shell=True)

def automated_scan(target=None, dir_wordlist=None, subd_wordlist=None):
    if not target:
        target = prompt("Enter the IP address or domain of the target: ")
    if not dir_wordlist:
        dir_wordlist = prompt("Enter the path to the wordlist for Dirb: ")
    if not subd_wordlist:
        subd_wordlist = prompt("Enter the path to the wordlist for ffuf: ")

    port_scan(target)
    tech_detection(target)
    dir_enum(target, dir_wordlist)
    subdomain_enum(target, subd_wordlist)

def choose_step():
    while True:
        print("\n[bold magenta]*** Select a step to perform ***[/bold magenta]")
        print("1. Port scan (Nmap)")
        print("2. Web tech detection (WhatWeb)")
        print("3. Directory enum (Dirb)")
        print("4. Subdomain enum (ffuf)")
        print("5. Return to main menu")

        choice = prompt("Select an option [1/2/3/4/5]: ")

        if choice == "1":
            target = prompt("Target IP or domain: ")
            port_scan(target)
        elif choice == "2":
            target = prompt("Target IP or domain: ")
            tech_detection(target)
        elif choice == "3":
            target = prompt("Target IP or domain: ")
            wordlist = prompt("Path to Dirb wordlist: ")
            dir_enum(target, wordlist)
        elif choice == "4":
            target = prompt("Target IP or domain: ")
            wordlist = prompt("Path to ffuf wordlist: ")
            subdomain_enum(target, wordlist)
        elif choice == "5":
            break
        else:
            print("[bold red]Invalid option. Please try again.[/bold red]")

def main_menu():
    banner = pyfiglet.figlet_format("HTB Scanner", font="slant")
    print(f"[bold green]{banner}[/bold green]")
    while True:
        print("\n[bold blue]=== MAIN MENU ===[/bold blue]")
        print("1. Automated scan")
        print("2. Choose which step to perform")
        print("3. Exit")

        choice = prompt("Select an option [1/2/3]: ")

        if choice == "1":
            automated_scan()
        elif choice == "2":
            choose_step()
        elif choice == "3":
            print("[bold red]Exiting...[/bold red]")
            break
        else:
            print("[bold red]Invalid option. Please try again.[/bold red]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Active Scanner for HTB targets")
    parser.add_argument("-t", "--host", help="Target IP or domain")
    parser.add_argument("-d", "--dir", help="Path to wordlist for Dirb")
    parser.add_argument("-s", "--sub", help="Path to wordlist for subdomain enum (ffuf)")

    args = parser.parse_args()

    if args.host and args.dir and args.sub:
        automated_scan(args.host, args.dir, args.sub)
    else:
        main_menu()
