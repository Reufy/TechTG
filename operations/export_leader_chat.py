from collections import Counter
import xlsxwriter
from telethon import utils
from telethon.errors.rpcerrorlist import ChatAdminRequiredError
from telethon.tl.types import Message


def make_filename(chat_name, ext):
    return f'{chat_name}_leader_chat.{ext}'

def simplify(users):
    copy = []
    for user in users:
        copy.append({
            'ID пользователя': user.id,
            'Имя': user.first_name,
            'Фамилия': user.last_name,
            'Никнейм': user.username,
            'Телефон': user.phone,
            'Колличество сообщений': user.messages_count
        })
    return copy

def export_to_xlsx(chat_name, users):
    workbook = xlsxwriter.Workbook("./result/" + make_filename(chat_name, 'xlsx'))
    worksheet = workbook.add_worksheet()
    users = simplify(users)
    worksheet.write_row(0, 0, users[0].keys())
    for i, row in enumerate(users):
        for j, value in enumerate(row.values()):
            worksheet.write(i + 1, j, value)
    workbook.close()


async def get_history(chat_name, client):
    return [x async for x in client.iter_messages(chat_name)]

async def leader_one_chat(client, modal_window_number_chat):
            chat_dict = {}
            dialogs = await client.get_dialogs()
            iterator = 0
            for x in dialogs:
                try:
                    link_chat = "t.me/" + str(x.entity.username)
                    chat_dict[str(iterator)] = x.entity.id
                    iterator += 1
                except AttributeError:
                    continue
            res_chat_number = int(modal_window_number_chat) - 1
            if  int(res_chat_number) <= int(iterator):
                chat_name = chat_dict[str(res_chat_number)]
                chat = await client.get_entity(chat_name)
                users = {}
                try:
                    members = await client.get_participants(chat_name)
                    for user in members:
                       users[user.id] = user
                    history = await get_history(chat_name, client)
                    if not len(history):
                        pass
                    #Счётчик сообщений от пользователя по id
                    message_counter = Counter()
                    for item in history:
                        try:
                            if isinstance(item, Message):
                                 try:
                                   message_counter[item.from_id.user_id] += 1
                                 except:
                                    continue
                        except:
                            pass
                    #Счётчик уникальных отправителей
                    senders = []
                    for x in history:
                        if isinstance(x, Message):
                            try:
                                senders.append(x.from_id.user_id)
                            except:
                                continue
                    senders = set(senders)

                    for id, u in users.items():
                        u.messages_count = message_counter.get(id)
                        u.leak_phone = ''
                    export_to_xlsx(utils.get_display_name(chat), users.values())
                except ChatAdminRequiredError:
                    pass


async def leader_all_chat(client):
            chat_dict = {}
            dialogs = await client.get_dialogs()
            iterator = 1
            it_chat = 1
            for x in dialogs:
                try:
                    link_chat = "t.me/" + str(x.entity.username)
                    chat_dict[str(iterator)] = x.entity.id
                    iterator += 1
                except AttributeError:
                    continue
                chat_name = chat_dict[str(it_chat)]
                chat = await client.get_entity(chat_name)
                users = {}
                try:
                    members = await client.get_participants(chat_name)
                    for user in members:
                        users[user.id] = user
                    history = await get_history(chat_name, client)
                    if not len(history):
                        pass
                    message_counter = Counter()
                    for item in history:
                        try:
                            if isinstance(item, Message):
                                try:
                                    message_counter[item.from_id.user_id] += 1
                                except:
                                    continue
                        except:
                            continue
                    senders = []
                    for x in history:
                        if isinstance(x, Message):
                            try:
                                senders.append(x.from_id.user_id)
                            except:
                                pass
                    senders = set(senders)
                    for id, u in users.items():
                        u.messages_count = message_counter.get(id)
                        u.leak_phone = ''
                    export_to_xlsx(utils.get_display_name(chat), users.values())
                    it_chat += 1
                except ChatAdminRequiredError:
                    it_chat += 1





