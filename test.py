import requests
import re
doi = "s41558-023-01793-3"
pdf_url = 'https://www.nature.com/articles/{doi}.pdf'
url = 'https://www.nature.com/articles/{}'.format(doi)

# Define the path where you want to save the downloaded PDF
save_path = './DOWNLOADED/{pdf_name}.pdf'

# Send an HTTP GET request to the URL
response = requests.get(pdf_url)
response_url = requests.get(url)
if response_url.status_code == 200:
    temp = response_url.text.title()
    temp1 = re.findall(r"<Title>(.*)<\/Title>", temp)
    title = temp1[0].split("|")[0]
    title = title.replace(" ", "_")
    print(doi+"_"+title+".pdf")

