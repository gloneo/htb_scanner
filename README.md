# htb_scanner
A very simple Hack the Box scanner to automate firsts enumerations.

# Installation
Use requirements.txt file to install dpendencies.
(pip3 install -r requirements.txt)
Make sure you have the following tools installed on your system:
  -nmap
  -whatweb
  -dirb
  -ffuf
  
# Usage
There are two ways to run the script:

1. Command-line arguments mode
Run the script with the target and wordlist paths as arguments to perform an automated scan without interaction:
python scanner.py -t <target> -d <dirb_wordlist_path> -s <ffuf_wordlist_path>
Example:
python scanner.py -t example.com -d /path/to/dirb_wordlist.txt -s /path/to/ffuf_wordlist.txt

2. Interactive menu mode
Run the script without any arguments to access an interactive menu that lets you:
- Perform a full automated scan
- Select individual scan steps to run
- Provide target and wordlists interactively
Just run: "python scanner.py"
