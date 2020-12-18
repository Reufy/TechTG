from telethon.errors.rpcerrorlist import ChatAdminRequiredError

async def get_history(chat_name, client):
    return [x async for x in client.iter_messages(chat_name)]


async def info_chat_result(client, res_date):
    dialogs = await client.get_dialogs()
    date_search = res_date
    with open('./result/info_chat_all.txt', 'a+',
              encoding='utf8') as res_file:
        for x in dialogs:
            print(x)
            try:
                if x.name == 'Telegram':
                    continue
                try:
                    test_chat = "t.me/" + str(x.entity.title)
                except AttributeError:
                    continue
                try:
                    chat_name = x.entity.id
                except AttributeError:
                    continue
                try:
                    members = await client.get_participants(chat_name)
                except ChatAdminRequiredError:
                    continue
                try:
                    history = await get_history(chat_name, client)
                except AttributeError:
                    continue
                if not len(history):
                    pass
                counter_message = 0
                for one_message in history:
                    if (str(date_search) in str(one_message.date)):
                        counter_message += 1
                    else:
                        break

                res_file.write(
                    "Чат: " + x.entity.title + " Колличество пользователей: " + str(
                        len(members)) + " Колличество сообщейний: " +
                    str(counter_message) + "\n")
            except:
                continue


async def info_chat_result_one_group(client, res_date, modal_window_number_chat):
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
    try:
        if  int(res_chat_number) <= int(iterator):
            chat_name = chat_dict[str(res_chat_number)]
            chat = await client.get_entity(chat_name)
            date_search = res_date
            try:
                members = await client.get_participants(chat_name)
            except ChatAdminRequiredError:
                pass
            try:
                history = await get_history(chat_name, client)
            except AttributeError:
                pass
            if not len(history):
                pass
            counter_message = 0
            for one_message in history:
                if (str(date_search) in str(one_message.date)):
                    counter_message += 1
                else:
                    break
            with open(f'./result/info_chat_one_№{modal_window_number_chat}.txt', 'a+',
                        encoding='utf8') as res_file:
                if chat.title:
                    res_file.write(
                            "Чат: " + chat.title + " Колличество пользователей: " + str(
                                len(members)) + " Колличество сообщейний: " +
                            str(counter_message) + "\n")
                else:
                    res_file.write(
                        "Чат: " + chat.id +  " Колличество сообщейний: " +
                        str(counter_message) + "\n")
    except:
        pass
