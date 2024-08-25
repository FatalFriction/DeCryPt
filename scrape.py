import requests
import os
import threading
import logging
import time
import random
from colorama import Fore

PROXY_DIR = "Proxy Scraper by M055AD"
FILES = ["http.txt", "https.txt", "socks4.txt", "socks5.txt"]

def scrape_proxies(url, filename, protocol_name):
    while True:
        try:
            response = requests.get(url, timeout=10).text.strip()
            if response in ["Rate limited.", "Internal Server Error"]:
                logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
            else:
                with open(os.path.join(PROXY_DIR, filename), "a") as f:
                    f.write(f"{response}\n")
                logging.info(f"{Fore.MAGENTA}|| {Fore.RESET}{Fore.CYAN}{Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}+{Fore.MAGENTA}{Fore.RESET}{Fore.BLUE}]{Fore.BLUE} Scraped {protocol_name} Proxy{Fore.RESET} {Fore.MAGENTA}||{Fore.RESET} {Fore.BLUE}Proxy Scraper by M055AD{Fore.RESET}")
        except:
            logging.info(f"{Fore.RED}|| {Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.MAGENTA}{Fore.RESET}{Fore.BLUE}]{Fore.LIGHTRED_EX} Timeout {protocol_name} Proxy{Fore.RESET} {Fore.RED}||{Fore.RESET} {Fore.BLUE}Proxy Scraper by M055AD{Fore.RESET}")

def http():
    scrape_proxies("https://gimmeproxy.com/api/getProxy?curl=false&protocol=http&ipPort=true", "http.txt", "HTTP")

def https():
    scrape_proxies("https://gimmeproxy.com/api/getProxy?curl=false&supportsHttps=true&ipPort=true", "https.txt", "HTTPS")

def socks4():
    scrape_proxies("https://gimmeproxy.com/api/getProxy?curl=false&protocol=socks4&ipPort=true", "socks4.txt", "SOCKS4")

def socks5():
    scrape_proxies("https://gimmeproxy.com/api/getProxy?curl=false&protocol=socks5&ipPort=true", "socks5.txt", "SOCKS5")

def exit_program():
    try:
        print("[+] Created by M055AD")
        os._exit(0)
    except:
        print("[-] Failed to Exit")

def directory_check():
    if not os.path.isdir(PROXY_DIR):
        print("[-] Proxy Scraping Directory Not Found")
        print("[!] Creating Proxy Scraping Directory")
        time.sleep(2)
        os.mkdir(PROXY_DIR)
        print(f"[+] Created Proxy Scraping Directory: {PROXY_DIR}")
        time.sleep(3)

    for file in FILES:
        file_path = os.path.join(PROXY_DIR, file)
        if not os.path.isfile(file_path):
            open(file_path, "w").close()

def banner_startup_mf():
    try:
        quotes = [
            f"""{Fore.RESET}{Fore.MAGENTA}       M055AD is a group of people who know how to use       {Fore.RESET}{Fore.BLUE}     ║
                  {Fore.RESET}{Fore.MAGENTA}computers better than "normal" people           {Fore.RESET}{Fore.BLUE}║""",
            f"   {Fore.RESET}{Fore.MAGENTA}\"It's not how you use it, it's how you do it\" - M055AD{Fore.RESET}{Fore.BLUE}         ║"
        ]
        quote = random.choice(quotes)
        print(f"{Fore.BLUE}")
        print("══════════════════════════════════════════════════════════════════╗")
        print("                                                                  ║")
        print(" '||''|.             ..|'''.|                  '||''|.    .       ║")
        print("  ||   ||    ....  .|'     '  ... ..  .... ...  ||   || .||.      ║")
        print("  ||    || .|...|| ||          ||' ''  '|.  |   ||...|'  ||       ║")
        print("  ||    || ||      '|.      .  ||       '|.|    ||       ||       ║")
        print(" .||...|'   '|...'  ''|....'  .||.       '|    .||.      '|.'     ║")
        print("                                     .. |                         ║")
        print("                                      ''                          ║")
        print("                                                                  ║")
        print(f"{quote}")
        print("                                                                  ║")
        print(f"                      {Fore.RESET}{Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}#{Fore.RESET}{Fore.MAGENTA}] Version     :{Fore.RESET}{Fore.CYAN} v0.1{Fore.RESET}{Fore.BLUE}                      ║")  
        print(f"                      {Fore.RESET}{Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}#{Fore.RESET}{Fore.MAGENTA}] Created by  : {Fore.RESET}{Fore.CYAN}M055AD{Fore.RESET}{Fore.BLUE}                    ║")
        print(f"                      {Fore.RESET}{Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}#{Fore.RESET}{Fore.MAGENTA}] M055AD      : {Fore.CYAN}CRACK ALL SHARED PROXIES{Fore.RESET}{Fore.BLUE}  ║")
        print("                                                                  ║")
        print("╔═════════════════════════════════════════════════════════════════╝")
        print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}D{Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}1{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} -> {Fore.RESET}{Fore.BLUE}|| Exit Proxy Scraper{Fore.RESET}")
        print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}e{Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}2{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} -> {Fore.RESET}{Fore.BLUE}|| Scrape HTTP Proxies{Fore.RESET}")
        print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}C{Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}3{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} -> {Fore.RESET}{Fore.BLUE}|| Scrape HTTPS Proxies{Fore.RESET}")
        print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}r{Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}4{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} -> {Fore.RESET}{Fore.BLUE}|| Scrape SOCKS4 Proxies{Fore.RESET}")
        print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}y{Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}5{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} -> {Fore.RESET}{Fore.BLUE}|| Scrape SOCKS5 Proxies{Fore.RESET}")
        print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}P{Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}6{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} -> {Fore.RESET}{Fore.BLUE}|| Scrape All Types of Proxies{Fore.RESET}")
    except KeyboardInterrupt:
        exit_program()

if __name__ == "__main__":
    os.system("cls")
    directory_check()   
    os.system("cls")
    logging.basicConfig(format=f"{Fore.CYAN}[{Fore.RESET}{Fore.LIGHTBLUE_EX}%(asctime)s{Fore.RESET}{Fore.CYAN}]{Fore.RESET} %(message)s", level=logging.INFO, datefmt="%H:%M:%S")
    
    try:
        banner_startup_mf()
        proxy_type = input(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}enter{Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}1-6{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.BLUE}Enter your choice: {Fore.RESET}")

        threads = []
        thread_count = 1  # Default to 1 thread if not specified

        if proxy_type in ['1', '2', '3', '4', '5', '6']:
            thread_count = int(input(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}enter{Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}amount of threads{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.BLUE}Enter thread count: {Fore.RESET}"))

        if proxy_type in ['1', '2', '3', '4', '5', '6']:
            func_map = {
                '1': http,
                '2': http,
                '3': socks4,
                '4': socks5,
                '5': https,
                '6': lambda: [http(), https(), socks4(), socks5()]
            }

            if proxy_type == '6':
                # Start all proxy functions in separate threads
                for func in func_map[proxy_type]:
                    t = threading.Thread(target=func)
                    t.start()
                    threads.append(t)
            else:
                # Start the selected proxy function in multiple threads if applicable
                for _ in range(thread_count):
                    t = threading.Thread(target=func_map[proxy_type])
                    t.start()
                    threads.append(t)

        else:
            print(f"{Fore.RED}[-] Invalid option selected{Fore.RESET}")

        for t in threads:
            t.join()
        
    except KeyboardInterrupt:
        exit_program()
