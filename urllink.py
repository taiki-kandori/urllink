#!/usr/bin/python3
import bs4
import pyperclip
import requests
import sys


def main(url):
    try:
        with requests.get(url) as res:
            bs4_obj = bs4.BeautifulSoup(res.text, 'html.parser')
            title = bs4_obj.title.string
            md_link = f'[{title}]({url})'
            print(md_link)
            pyperclip.copy(md_link)

    except requests.HTTPError as e:
        print(e)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print('Usage: urllink <URL>')
        exit()
    else:
        main(args[1])