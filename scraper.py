import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path

def request_html(url): # target url passed into function
 response = requests.get(url, timeout=10) # .get http for requests api
 response.raise_for_status() #check for errors
 return response.text

def parse_html(response_text_html):
 parsed_html = BeautifulSoup (response_text_html, "html.parser")
 return parsed_html


