"""
Python script that uses two implemented dunctions to download papers from a certin journal from natures index.
"""
import os
import requests
import re
from functions import get_paper, DIR, check_downloaded
from sys import argv


try:
    num_pages = int(argv[1])
    category = argv[2] + "/"
    print("NUmber of pages: ", num_pages," Category: ", category)
except:
    print("Missing arguments, provide: python3 scraper.py <number of pages> <category>")
    num_pages = 1
    category = "ngeo/"

current_directory = os.getcwd()
try:
    os.mkdir("./DOWNLOADED/{}".format(category))
except FileExistsError:
    print("Folder ready for use!")

try:
    dois = check_downloaded("./DOWNLOADED/{}".format(category))
    print("There are {} papers already donwloaded ...".format(len(dois)))
except:
    print("No downloaded papers already ...")
    dois = []

all_dois = []

try:
    for page in range(1, num_pages + 1):
        current_page = str(page)
        url = f'https://www.nature.com/{category}research-articles?searchType=journalSearch&sort=PubDate&page={str(page)}'
        r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})

        html = r.content
        temp1 = re.findall(r"articles\/(\w*-\w*-\w*-\w*)", str(html))

        for doi in temp1:
            if doi not in dois:
                try:
                    get_paper(doi, category)
                    all_dois.append(doi)

                except:
                    print("Error downloading or saving, here are all downloaded: ", all_dois)


except AttributeError:
    print('Invalid entry!')


if len(all_dois) < 1:
    print("All papers downloaded ...")
