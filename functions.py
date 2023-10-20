import requests
import re
from os import listdir

DIR = "./DOWNLOADED/"

def get_paper(doi, cat = ""):
    """
    Function that donwloads the paper from the given url

    input:
        - pdf doi
        - category
    """
    # The URL to the PDF file
    pdf_url = 'https://www.nature.com/articles/{}.pdf'.format(doi)
    url = 'https://www.nature.com/articles/{}'.format(doi)

    

    # Send an HTTP GET request to the URL
    response = requests.get(pdf_url)
    response_url = requests.get(url)

    if response_url.status_code == 200:

        temp = response_url.text.title()
        temp1 = re.findall(r"<Title>(.*)<\/Title>", temp)
        title = temp1[0].split("|")[0]
        title = title.replace(" ", "_")

        title = title.replace("/", "_")
        save_path = DIR + cat + doi + "_" + title + ".pdf"

    else:
        save_path = DIR + cat + doi + ".pdf"
    # Define the path where you want to save the downloaded PDF
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:

        # Open a file and write the content of the response to it
        with open(save_path, 'wb') as pdf_file:
            pdf_file.write(response.content)
        print(f"Downloaded and saved to {save_path}")
    else:
        print(f"Failed to download the PDF. Status code: {response.status_code}")


def check_downloaded(location):

    files = listdir(location)

    doilist = []
    for f in files:
        doilist.append(f.split("_")[0])

    return doilist