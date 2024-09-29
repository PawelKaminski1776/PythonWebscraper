import requests
from bs4 import BeautifulSoup

# Set headers to match Postman
headers = {
    "User-Agent": "PostmanRuntime/7.42.0",
    "Accept": "*/*",
    "Connection": "keep-alive"
}
i = 20
response = requests.get("https://www.daft.ie/property-for-rent/ireland/houses?pageSize=20&from=20", headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
numofpages = soup.find("p", attrs={"class":"sc-63789aed-1 ixSIcp"})

print(numofpages)

while i < 400:
    response = requests.get("https://www.daft.ie/property-for-rent/ireland/houses?pageSize=20&from="+str(i), headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    homes = soup.findAll("p", attrs={"class":"sc-99fd5e84-0 jCdpeu"})
    homePrices = soup.findAll("p", attrs={"class":"sc-99fd5e84-0 gPSYkR"})
    for home in homes:
        print(home.text)
    for homePrice in homePrices:
        print(homePrice.text)
    i=i+20



