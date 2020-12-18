from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import EditAdminRequest
from telethon import types
import time


async def delete_user_group(client, modal_window_number_chat):
    SLEEP_TIME = 1000
    KICK_SLEEP_STEP = 200
    ANTI_MESSAGES_BOT = '@AntiServiceMessage_Bot'

    def perform_sleep():
        time.sleep(SLEEP_TIME)
    def check_chat_rights(chat):
        if not chat.admin_rights or not chat.admin_rights.ban_users:
            #Вы не админ
            pass

    async def grant_permissions(chat_id, user_id):
        rights = types.ChatAdminRights(
            delete_messages=True,
            add_admins=True
        )
        await client(EditAdminRequest(chat_id, user_id, rights, ''))

    async def invite_user(chat_id, user_to_add):
        await client(InviteToChannelRequest(
            chat_id,
            [user_to_add]
        ))

    async def kick_users(chat, users, ignore_ids):
        for index, user in enumerate(users):
            if user.username == ANTI_MESSAGES_BOT.replace('@', ''):
                continue
            if user.id in ignore_ids:
                continue
            if index % KICK_SLEEP_STEP == 0:
                perform_sleep()
            try:
                kicked = await client.kick_participant(chat, user)
            except Exception:
                perform_sleep()


    me = await client.get_me()
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
        try:
            check_chat_rights(chat)
        except Exception:
            time.sleep(0.3)
            pass
        users = await client.get_participants(chat_name)
        admins = await client.get_participants(chat_name, filter=types.ChannelParticipantsAdmins)

        try:
            await invite_user(chat.id, ANTI_MESSAGES_BOT)
        except:
            pass
        try:
            await grant_permissions(chat.id, ANTI_MESSAGES_BOT)
        except:
            pass

        ignore_ids = [x.id for x in admins]
        ignore_ids.append(me.id)
        ignore_ids = set(ignore_ids)

        await kick_users(chat, users, ignore_ids)
