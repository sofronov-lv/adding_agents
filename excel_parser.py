import openpyxl
from transliterate import translit


def check_phone_number(phone: str) -> str:
    if len(phone) < 11:
        return "7" + phone
    return phone


def get_email(fio: str, inn: str) -> str:
    """Generating a mail for each client according to a template"""
    fio_en = str(translit(fio, reversed=True))
    fio_en = fio_en.replace(" ", "_").replace("'", "").lower()
    return "s896_" + fio_en + "_" + inn[-1:-4:-1] + "@mail.ru"


def get_clients():
    """Get a list of all clients from excel"""
    book = openpyxl.load_workbook(filename="client_list.xlsx")
    sheet = book["clients"]  # name of the page sheet

    psb_dict = {}
    for name_, inn_, phone_, psb_ in zip(sheet["A"], sheet["B"], sheet["C"], sheet["H"]):
        phone_ = str(phone_.value)
        phone_ = check_phone_number(phone_)

        if phone_.isdigit() and not psb_.value:
            inn_ = str(inn_.value)
            name_ = name_.value.title()
            email = get_email(name_, inn_)

            psb_dict[inn_] = {
                "city_id": 1,
                "email": email,
                "fio": name_,
                "inn": inn_,
                "open_payment_account": True,
                "organization_name": f"ип {name_}",
                "phone": phone_
            }
    return psb_dict


if __name__ == "__main__":
    clients = get_clients()
    print(clients)
