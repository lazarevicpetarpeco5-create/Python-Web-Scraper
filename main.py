import requests # We use this lib to fetch a html page
from bs4 import BeautifulSoup # We will sue it to read teh recovered html page
import json # helps with python code interacting with json and vice versa
from pathlib import Path # so normal py lib for paths 
from scraper import request_html, parse_html, store_html

def show_banner():
    print(r"""
     __   __ _____ ____    __  __    _    _   _
    \ \ / /| ____/ ___|  |  \/  |  / \  | \ | |
     \ V / |  _| \___ \  | |\/| | / _ \ |  \| |
      | |  | |___ ___) | | |  | |/ ___ \| |\  |
      |_|  |_____|____/  |_|  |_/_/   \_\_| \_|

        +--------------------------------+
        |  P I K K I 2  //  WEB SCRAPER  |
        +--------------------------------+
          [>] awaiting target_
    """)

def main():
    show_banner()

    
    url = input("Enter The Target URL: ").strip()
    response_text_html =  request_html(url)
    result_html_data = parse_html(response_text_html)
    storing_of_html = store_html(result_html_data)
     
  
if __name__ == "__main__":
    main()