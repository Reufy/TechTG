


async def chat_names_intro(client):
    chat_dict = {}
    dialogs = await client.get_dialogs()
    iterator = 1
    for x in dialogs:
        try:
            link_chat = "t.me/" + str(x.entity.username)
            result = "№" + str(
                iterator) + " " + x.name + " Ссылка на чат: " + link_chat + " ID чата: " + str(
                x.entity.id)
            chat_dict[str(iterator)] = result
            iterator += 1
        except AttributeError:
            continue
    return chat_dict
