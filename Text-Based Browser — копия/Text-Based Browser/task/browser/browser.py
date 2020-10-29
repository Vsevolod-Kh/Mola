from collections import deque
from bs4 import BeautifulSoup
from colorama import init
from termcolor import colored
import os
import sys
import requests

path = sys.argv
os.makedirs(str(path[1]), exist_ok=True)
stack = deque()

init()


class Browser:
    def __init__(self, url):
        self.url = url

        if "." in url:

            if url.split("//")[0] != "https:":
                url = "https://" + url

            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')

            if r.status_code == 200:
                for link in soup.find_all('a'):
                    link.string = colored(link.text, 'blue')
                print(soup.text)
                site_txt = open(str(path[1]) + '/' + 'site', 'w')
                site_txt.write(soup.text)
            else:
                print("Error")
        else:
            print("Error: Incorrect URL")


while True:
    user = str(input(''))

    stack.append(user)
    if user == "exit":
        break
    elif user == "back":
        if len(stack) > 0:
            del stack[-1]
            del stack[-1]
            project = Browser(stack.pop())
    else:
        project = Browser(user)
