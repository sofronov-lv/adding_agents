import json
import requests

from config import DATA, PSB_URL

session = requests.Session()  # starting a session with the site

response = session.post(PSB_URL, data=DATA)  # authorization on the site using the ost method
json_dict = json.loads(response.text)
token = json_dict["access_token"]  # get a token for subsequent work
headers = {"Authorization": f"Bearer {token}"}

email = "s896_client_bank_test_3@mail.ru"
fio = "ХАНВЕРДИЕВ ДАВИД АРСЕНОВИЧ"
inn = "500121199264"
phone_number = "9857604284"

user_data = {
    "city_id": 1,  # int
    "email": email,
    "fio": fio,
    "inn": inn,  # str
    "open_payment_account": True,
    "organization_name": f"ип {fio}",
    "phone": "7" + phone_number  # str
}

res = session.post("https://api.lk.psb.services/agent/v1/rko/order", data=user_data, headers=headers)
res.encoding = "utf-8"  # explicitly specify the encoding
print(res.text)
