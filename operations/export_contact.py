from telethon.tl.functions.contacts import GetContactsRequest
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import xlsxwriter





def simplify(object_cont):
    copy = []
    for cont in object_cont:
        copy.append({
            'ID контакта': cont.id,
            'Имя': cont.first_name,
            'Фамилия': cont.last_name,
            'Никнейм': cont.username,
            'Телефон': cont.phone,
            'Хэш': cont.access_hash
        })
    return copy

def export_to_xlsx(object_cont):
     # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook("./result/" + 'export_me_contacts.xlsx')
    worksheet = workbook.add_worksheet()

    object_cont = simplify(object_cont)
    worksheet.write_row(0, 0, object_cont[0].keys())
    for i, row in enumerate(object_cont):
        for j, value in enumerate(row.values()):
            worksheet.write(i + 1, j, value)
    workbook.close()



async def get_address_book(client, auth_session_string):
    object_contact = await client(GetContactsRequest(hash=0))
    if object_contact:
        object_cont = object_contact.users
        export_to_xlsx(object_cont)


    else:
        pass

