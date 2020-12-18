from telethon.tl.functions.channels import InviteToChannelRequest

async def enter_user_group(client, modal_window_number_chat, user_name_add):
    async def invite_user(chat_id, user_to_add):
        await client(InviteToChannelRequest(
            chat_id,
            [user_to_add]
        ))


    dialogs = await client.get_dialogs()
    iterator = 0
    chat_dict = {}
    for x in dialogs:
        try:
            link_chat = "t.me/" + str(x.entity.username)
            chat_dict[str(iterator)] = x.entity.id
            iterator += 1
        except AttributeError:
            continue
    res_chat_number = modal_window_number_chat - 1
    res_chat_number = str(res_chat_number)
    if  int(res_chat_number) <= int(iterator):
        chat_name = chat_dict[res_chat_number]
        chat = await client.get_entity(chat_name)
        for user_name in user_name_add:
            await invite_user(chat.id, user_name)




