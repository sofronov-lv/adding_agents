import json
import requests

from config import DATA_PSB, PSB_URL, ADD_PSB_URL

session = requests.Session()  # starting a session with the site

response = session.post(PSB_URL, data=DATA_PSB)  # authorization on the site using the ost method
json_dict = json.loads(response.text)
token = json_dict["access_token"]  # get a token for subsequent work

# adding a client to the site
# res = session.post(ADD_PSB_URL, data=user_data, headers={"Authorization": f"Bearer {token}"})
