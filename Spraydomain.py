import requests
from colorama import Fore, Style
import pyfiglet

def find_subdomains(base_domain, wordlist):
    subdomains = set()

    for word in wordlist:
        subdomain = f"{word}.{base_domain}"
        url = f"http://{subdomain}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                subdomains.add(subdomain)
        except requests.exceptions.RequestException:
            pass

    return subdomains

def print_banner():
    banner_text = pyfiglet.figlet_format("Spray Subdomain")
    colored_banner = Fore.CYAN + banner_text + Style.RESET_ALL
    print(colored_banner)

def print_signature():
    signature = f"\n{Fore.YELLOW}-- @ODF5 Use the tool for security research only --{Style.RESET_ALL}"
    print(signature)

def main():
    print_banner()

    target_domain = input("Enter the base domain (e.g., example.com): ")
    wordlist_file = input("Enter the path to the wordlist file: ")

    with open(wordlist_file) as f:
        wordlist = f.read().splitlines()

    found_subdomains = find_subdomains(target_domain, wordlist)

    if found_subdomains:
        print(f"{Fore.GREEN}Found {len(found_subdomains)} subdomains:{Style.RESET_ALL}")
        for subdomain in found_subdomains:
            print(Fore.BLUE + subdomain + Style.RESET_ALL)
    else:
        print(f"{Fore.YELLOW}No subdomains found.{Style.RESET_ALL}")

    print_signature()

if __name__ == "__main__":
    main()
