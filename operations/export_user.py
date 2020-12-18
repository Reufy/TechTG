from telethon.errors.rpcerrorlist import ChatAdminRequiredError
from telethon import utils
import xlsxwriter

def make_filename(chat_name, ext):
    return f'{chat_name}_export_user_chat.{ext}'


def simplify(users):
    copy = []
    for user in users:
        copy.append({
            'ID пользователя': user.id,
            'Имя': user.first_name,
            'Фамилия': user.last_name,
            'Никнейм': user.username,
            'Телефон': user.phone,
            'Ваш контакт': user.contact,
            'Бот': user.bot,
            'Хэш': user.access_hash,

        })
    return copy


def export_to_xlsx(chat_name, users):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook("./result/" + make_filename(chat_name, 'xlsx'))
    worksheet = workbook.add_worksheet()

    users = simplify(users)
    worksheet.write_row(0, 0, users[0].keys())
    for i, row in enumerate(users):
        for j, value in enumerate(row.values()):
            worksheet.write(i + 1, j, value)
    workbook.close()


async def dump_users_one_chat(client, modal_window_number_chat):
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
        try:
            res_chat_number = int(modal_window_number_chat) - 1
            if  int(res_chat_number) <= int(iterator):
                chat_name = chat_dict[str(res_chat_number)]
                chat = await client.get_entity(chat_name)
                users = {}
                members = await client.get_participants(chat_name)
                for user in members:
                    users[user.id] = user
                export_to_xlsx(utils.get_display_name(chat), users.values())
        except ChatAdminRequiredError:
            pass


async def dump_users_all_chat(client):
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
                export_to_xlsx(utils.get_display_name(chat), users.values())
                it_chat += 1
            except ChatAdminRequiredError:
                it_chat += 1
                continue




