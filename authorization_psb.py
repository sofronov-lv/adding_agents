import requests
from bs4 import BeautifulSoup

from config import DATA, PSB_URL

session = requests.Session()  # starting a session with the site

authorization_responce = session.post(PSB_URL, data=DATA)  # authorization on the site using the ost method
profile_responce = session.get("https://lk.psb.services/orders/rko/order")
profile_responce.encoding = "utf-8"  # explicitly specify the encoding
print(profile_responce.text)
