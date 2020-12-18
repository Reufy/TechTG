from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest

async def add_number_to_contact(client, phone_numbers):
    iter = 0
    while iter <20:
        contact = InputPhoneContact(client_id=0, phone=phone_numbers, first_name=phone_numbers, last_name=phone_numbers)
        result = await client(ImportContactsRequest([contact]))
        iter += 1





