import requests
from bs4 import BeautifulSoup
url = "https://www.skysports.com/f1/grandprix/monaco/results"
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")
Monaco = soup.find("div",class_="page-header page-header--takeover")
print(Monaco.text)

uri = "https://www.skysports.com/f1/grandprix/monaco/results/2022/qualifying-1"
request = requests.get(uri)
soup = BeautifulSoup(request.text, "html.parser")
Q1 = soup.find("div",class_="page-filters__offset")
print(Q1.text)

ura = "https://www.skysports.com/f1/grandprix/monaco/results/2022/qualifying-2"
request = requests.get(ura)
soup = BeautifulSoup(request.text, "html.parser")
Q2 = soup.find("div",class_="page-filters__offset")
print(Q2.text)

urq = "https://www.skysports.com/f1/grandprix/monaco/results/2022/qualifying-3"
request = requests.get(urq)
soup = BeautifulSoup(request.text, "html.parser")
Q3 = soup.find("div",class_="page-filters__offset")
print(Q3.text)

urw = "https://www.skysports.com/f1/grandprix/monaco/results/2022/race"
request = requests.get(urw)
soup = BeautifulSoup(request.text, "html.parser")
Race = soup.find("div",class_="page-filters__offset")
print(Race.text)

ury = "https://www.championat.com/auto/_f1/tournament/689/standing/"
request = requests.get(ury)
soup = BeautifulSoup(request.text, "html.parser")
DriverStandings= soup.find("dib",class_="js-tournament-tabs eane tournament-tabs")
print(DriverStandings.text)








