import openpyxl

book = openpyxl.load_workbook(filename="client_list.xlsx")
sheet = book["первые 2 базы"]

psb_dict = {}

for name_, inn_, phone_, psb_ in zip(sheet["A"], sheet["B"], sheet["C"], sheet["H"]):
    if type(phone_.value) == int and not psb_.value:
        psb_dict[str(inn_.value)] = [name_.value, str(phone_.value)]

print(psb_dict)
