from telethon.errors.rpcerrorlist import ChatAdminRequiredError
from telethon import utils

async def get_history(chat_name, client):
    return [x async for x in client.iter_messages(chat_name)]


async def dump_one_chat_message(client, modal_window_number_chat):

            chat_dict = {}
            dialogs = await client.get_dialogs()
            iterator = 0
            for x in dialogs:
                try:
                    link_chat = "t.me/" + str(x.entity.username)
                    chat_dict[str(iterator)] = x.entity.id
                    iterator += 1
                except AttributeError:
                    pass
            res_chat_number = int(modal_window_number_chat) - 1
            if int(res_chat_number) <= int(iterator):
                chat_name = chat_dict[str(res_chat_number)]
                chat = await client.get_entity(chat_name)
                try:
                    history = await get_history(chat_name, client)
                    if not len(history):
                        pass
                    te = open(f"./result/{utils.get_display_name(chat)}_export_message.txt",  "a+", encoding="utf8")
                    for i in history:
                        try:
                            if i.from_id:
                                te.write((f"ID сообщения: {i.id}; Дата публикации: {i.date}; Текст сообщения: {i.message}; Отправленно пользователем с ID:{i.from_id}: Канал {i.peer_id} '\n"))
                                te.write('*' * 200 + '\n')
                            else:
                                te.write((f"ID сообщения: {i.id}; Дата публикации: {i.date}; Текст сообщения: {i.message}; Канал {i.peer_id} '\n"))
                                te.write('*' * 200 + '\n')
                        except AttributeError:
                            continue
                    te.close()
                except ChatAdminRequiredError:
                    pass





async def dump_all_chat_message(client):
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
                    try:
                        history = await get_history(chat_name, client)
                        if not len(history):
                            pass
                        te = open(f"./result/{utils.get_display_name(chat)}.txt", "a+", encoding="utf8")
                        for i in history:
                            try:
                                if i.from_id:
                                    te.write((
                                                 f"ID сообщения: {i.id}; Дата публикации: {i.date}; Текст сообщения: {i.message}; Отправленно пользователем с ID:{i.from_id}: Канал {i.peer_id} '\n"))
                                    te.write('*' * 200 + '\n')
                                else:
                                    te.write((
                                                 f"ID сообщения: {i.id}; Дата публикации: {i.date}; Текст сообщения: {i.message}; Канал {i.peer_id} '\n"))
                                    te.write('*' * 200 + '\n')
                            except AttributeError:
                                continue
                        te.close()
                        it_chat += 1
                    except ChatAdminRequiredError:
                        it_chat += 1




async def dump_one_chat_message_user_id(client, modal_window_number_chat, modal_window_user_id_one):
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
                res_chat_number = str(res_chat_number)
                if  int(res_chat_number) <= int(iterator):
                    chat_name = chat_dict[res_chat_number]
                    chat = await client.get_entity(chat_name)
                    user_id_search = modal_window_user_id_one
                    try:
                        history = await get_history(chat_name, client)
                        if not len(history):
                            pass
                        te = open(f"./result/{user_id_search}_{utils.get_display_name(chat)}.txt", "a+",
                                  encoding="utf8")
                        for i in history:
                            try:
                                if int(i.from_id.user_id) == int(user_id_search):
                                    if i.from_id:
                                        te.write((
                                            f"ID сообщения: {i.id}; Дата публикации: {i.date}; Текст сообщения: {i.message}; Отправленно пользователем с ID:{i.from_id}: Канал {i.peer_id} '\n"))
                                        te.write('*' * 200 + '\n')
                                    else:
                                        te.write((
                                            f"ID сообщения: {i.id}; Дата публикации: {i.date}; Текст сообщения: {i.message}; Канал {i.peer_id} '\n"))
                                        te.write('*' * 200 + '\n')
                            except AttributeError:
                                pass
                        te.close()
                    except ChatAdminRequiredError:
                        pass


async def dump_all_chat_message_user_id(client, modal_window_user_id):
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
                    user_id_search = modal_window_user_id
                    chat_name = chat_dict[str(it_chat)]
                    chat = await client.get_entity(chat_name)
                    try:
                        history = await get_history(chat_name, client)
                        if not len(history):
                            pass
                        te = open(f"./result/{user_id_search}_export_message_all_chat.txt", "a+",
                                  encoding="utf8")
                        for i in history:
                            try:
                                if int(i.from_id.user_id) == int(user_id_search):
                                    if i.from_id:
                                        te.write((
                                            f"ID сообщения: {i.id}; Дата публикации: {i.date}; Текст сообщения: {i.message}; Отправленно пользователем с ID:{i.from_id}: Канал {i.peer_id} '\n"))
                                        te.write('*' * 200 + '\n')
                                    else:
                                        te.write((
                                            f"ID сообщения: {i.id}; Дата публикации: {i.date}; Текст сообщения: {i.message}; Канал {i.peer_id} '\n"))
                                        te.write('*' * 200 + '\n')
                            except AttributeError:
                                pass
                        te.close()
                        it_chat += 1
                    except ChatAdminRequiredError:
                        it_chat += 1





