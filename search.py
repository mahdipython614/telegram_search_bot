import asyncio
import threading

import telepot
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import GetAllChatsRequest
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty

api_id = 1022542
api_hash = "128fdf6107bef2945b730a8533b9915f"
zanjan = {}
zanjan2 = {}
zanjan3 = {}
zanjan4 = {}
zanjant = {}
zanjan_time = {}
zanjan_pass = {}
zanjan_pass_turn = {}
zanjan_code = {}
zanjan_ph = {}
zanjan_ph_turn = {}
zanjan_code_turn={}
client2={}
s = 0
t=0
start={}
loop = asyncio.new_event_loop()


def on_chat_message(msg):
    global s,start,t
    global msg_text,client2,loop
    global zanjan
    global zanjan2
    global zanjan3
    global zanjan4
    global zanjant
    global zanjan_time
    global zanjan_pass_turn
    global zanjan_pass
    global zanjan_code_turn
    global zanjan_code
    global zanjan_ph
    global zanjan_ph_turn
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat Message:', content_type, chat_type, chat_id)
    msg_text = int(msg['from']['id'])
    print(msg_text)
    print(msg)

    if content_type == 'text':
        if msg['text'] == '/start':
            bot.sendMessage(chat_id, 'گزینه مورد نظر را انتخاب کنید',
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(text="جستجوی دقیق", callback_data='8'),
                                 InlineKeyboardButton(text="جستجوی جز به جز", callback_data='9')],
                                [InlineKeyboardButton(text="پایان", callback_data='10')]
                            ]
                            ))
            start[chat_id]=0
            zanjan[chat_id]=[]
            try:
                zanjan3[chat_id]=[]
            except IndexError:
                pass
            client2[chat_id]=0
            zanjan4[chat_id]=0
            start[chat_id]=0
            zanjan2[chat_id] =0
            zanjant[chat_id]=0
            print(1,start)
        elif zanjan2[chat_id]==1:
            bot.sendMessage(chat_id, 'این عبارت جستجو شود:     ' + msg['text'],
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(text="تایید", callback_data='21'),
                                 InlineKeyboardButton(text="ویرایش", callback_data='11')],

                            ]
                            ))
            zanjan2[chat_id] = 0
            zanjan[chat_id]+=['"'+msg['text']+'"']
            zanjan3 = [msg['text']]
        elif zanjan4[chat_id] == 1:
            bot.sendMessage(chat_id, 'این عبارت جستجو شود:     ' + msg['text'],
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(text="تایید", callback_data='21'),
                                 InlineKeyboardButton(text="ویرایش", callback_data='100')],

                            ]
                            ))
            zanjan4[chat_id] = 0

            #res = re.sub('[' + string.punctuation + ']', '', msg['text']).split()
            zanjan[chat_id]+=[msg['text']]
            zanjan3 =[msg['text']]
        elif zanjant[chat_id] == 1:
            bot.sendMessage(chat_id, 'پیام ها هر ' + msg['text'] + 'ساعت ارسال شود',
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(text="تایید", callback_data='23'),
                                 InlineKeyboardButton(text="ویرایش", callback_data='24')],
                            ]
                            ))
            zanjan_time[chat_id] = eval(msg['text'])
            zanjant[chat_id] = 0

        elif zanjan_pass_turn[chat_id] == 1:
            zanjan_pass[chat_id] = msg['text']
            bot.sendMessage(chat_id, 'رمز عبور شما:  ' + msg['text'],
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(text="تایید", callback_data='27'),
                                 InlineKeyboardButton(text="ویرایش", callback_data='26')],
                            ]
                            ))
            zanjan_pass_turn[chat_id] = 0

        elif zanjan_ph_turn[chat_id]==1:
            zanjan_ph[chat_id]= msg['text']
            bot.sendMessage(chat_id, 'تلفن شما:  ' + msg['text'],
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(text="تایید", callback_data='29'),
                                 InlineKeyboardButton(text="ویرایش", callback_data='31')],
                            ]
                            ))
            zanjan_ph_turn[chat_id] = 0

        elif zanjan_code_turn[chat_id] == 1:
            zanjan_code_turn[chat_id] = 0
            bot.sendMessage(chat_id, 'ثبت شد')
            filter = InputMessagesFilterEmpty()
            print(start,111111111111111111111111111)
            if start[chat_id]==0:
                zanjan_code [chat_id]= str(int(int(msg['text'])/10))
            if start[chat_id]==1:
                zanjan_time[chat_id]=eval(msg['text'])

            print(zanjan_ph,zanjan_pass,zanjan_code)
            print(type(zanjan_ph),type(zanjan_pass),type(zanjan_code))

            client3 = TelegramClient(str(msg['message_id']), api_id, api_hash, loop=loop).start(
                    bot_token='1003236552:AAG0Qmb9j52J6pN5qHIhCpX5S5MBCzjwHwg')

            def thread1():
                global start,t

                if start[chat_id] == 1:
                    t.cancel()
                    start[chat_id]=0
                    print(start,33333333333333)
                if start[chat_id] == 0:
                    t = threading.Timer(zanjan_time[chat_id] * 3600, thread1)
                    t.start()
                async def sign():
                    global client2
                    #if not await client2[from_id].is_user_authorized():
                    await client2[chat_id].connect()
                    try:
                        await client2[chat_id].sign_in(zanjan_ph[chat_id], zanjan_code[chat_id])
                    except SessionPasswordNeededError:
                        await client2[chat_id].sign_in(password=zanjan_pass[chat_id])
                    #telethon.errors.rpcerrorlist.PhoneCodeInvalidError

                loop.run_until_complete(sign())

                async def main():
                    global zanjan_ph, m, b
                    m = await client2[chat_id](GetAllChatsRequest([0]))
                    for dia in m.chats:
                        bot.sendMessage(chat_id, 'پیام های جستجو شده از ' + dia.title)
                        print(dia)
                        for word in zanjan[chat_id]:
                            b = await client2[chat_id](SearchRequest(
                                peer=dia.id,  # On which chat/conversation
                                q=word,  # What to  for
                                filter=filter,  # Filter to use (maybe filter for media)
                                min_date=None,  # Minimum date
                                max_date=None,  # Maximum date
                                offset_id=0,  # ID of the message to use as offset
                                add_offset=0,  # Additional offset
                                limit=100000,  # How many results
                                max_id=0,  # Maximum message ID
                                min_id=0,  # Minimum message ID
                                from_id=None,  # Who must have sent the message (peer)
                                hash=0
                            ))
                            print(b)
                            async def bot_send_mes():
                                for l in b.messages:
                                    print(l.id)
                                    channel_message_id = l.id

                                    # functions.messages.ForwardMessagesRequest(from_peer=654845802, id=[544, 1, 12],
                                    # to_peer=654845802))
                                    # msg_id = generate_random_long()
                                    '''for dial in dialog:
                                        if dial.entity.id == dia.id:
                                            print(dial)
                                            await client2[from_id].send_message(chat_id, getattr(msg, 'message', '...'))
                                            await client3.forward_messages(entity=chat_id,messages=l,from_peer=dia.id)
    
                                    await client3.forward_messages(chat_id, l.media)
                                    try:
                                        await client3.send_message(chat_id,l.media)
                                    except telethon.errors.rpcerrorlist.MediaEmptyError:
                                        #await client3.send_file(chat_id,[channel_message_id],1324638498,)
                                        print(l.media)
                                        await client3.send_file(chat_id,l.media,caption=l.message)'''

                                    # await client3(functions.messages.SendMediaRequest(chat_id,InputMediaDocument(l.media.document.id),l.message,))
                                    # await client3(functions.messages.ForwardMessagesRequest(from_peer=chat_id,id=[channel_message_id,1],to_peer=))
                                    #print(channel_message_id, dia.username)

                                    #if dia.username!=None:
                                        #bot.forwardMessage(chat_id,'@'+dia.username,channel_message_id)

                                    if dia.username!=None:
                                        await client3.forward_messages(chat_id, channel_message_id, dia.username,)

                                    try:
                                            await client3.send_message(chat_id, l)
                                    except:
                                            pass

                            await bot_send_mes()

                loop.run_until_complete(main())
                bot.sendMessage(chat_id,'برای تغییر اطلاعات وارد شده تغییر اطلاعات را انتخاب کنید',reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton(text="تغییر اطلاعات", callback_data='32')]]))

                '''async def dis():
                    await client2[chat_id].log_out()
                loop.run_until_complete(dis())'''

            thread1()




def on_callback_query(msg):
    query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
    global zanjan,client2,loop,start
    global zanjan2
    global zanjan3
    global zanjan4
    global zanjant
    global zanjan_time
    global zanjan_pass_turn
    global zanjan_pass
    global zanjan_code_turn
    global zanjan_code
    global zanjan_ph
    global zanjan_ph_turn
    if data == '8':
        bot.sendMessage(from_id, 'عبارت را وارد کنید', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="بازگشت", callback_data='21')]
        ]
        ))
        zanjan2[from_id] = 1
        print(zanjan2,)
    elif data == '9':
        bot.sendMessage(from_id, 'عبارت را وارد کنید', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="بازگشت", callback_data='21')]
        ]
        ))

        zanjan4[from_id] = 1

    elif data == '10':

        bot.sendMessage(from_id, 'بازه زمانی ارسال را به ساعت وارد کنید',
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(text="بازگشت", callback_data='21')]
                            ]
                            ))
        zanjan4[from_id]=0
        print(start,222222222)
        if start[from_id]==0:
            zanjant[from_id] = 1
        if start[from_id]==1:
            zanjan_code_turn[from_id]=1
    elif data == '11':
        bot.sendMessage(from_id, 'عبارت را وارد کنید')
        zanjan2[from_id] = 1
        del zanjan[from_id][-1]

    elif data == '100':
        bot.sendMessage(from_id, 'عبارت را وارد کنید')
        del zanjan[from_id][-1]
        zanjan4[from_id] = 1


    elif data == '21':
        bot.sendMessage(from_id, 'کلمات یا عبارت های جدید اضافه کنید یا پایان را انتخاب کنید', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="جستجوی دقیق", callback_data='8'),
             InlineKeyboardButton(text="جستجوی جز به جز", callback_data='9')],
            [InlineKeyboardButton(text="پایان", callback_data='10')]
        ]
        ))

    elif data == '23':
        bot.sendMessage(from_id, 'رمز عبور خود را وارد کنید:(در صورت نداشتن رمز عبور 0 را وارد کنید)', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="بازگشت", callback_data='25')]
        ]
        ))

        zanjan_pass_turn[from_id] = 1

    elif data == '25':
        bot.sendMessage(from_id, 'گزینه مورد نظر را انتخاب کنید',
                        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton(text="جستجوی دقیق", callback_data='8'),
                             InlineKeyboardButton(text="جستجوی جز به جز", callback_data='9')],
                            [InlineKeyboardButton(text="پایان", callback_data='10')]
                        ]
                        ))

        zanjan_pass_turn[from_id] = 0

    elif data == '26':
        bot.sendMessage(from_id, 'رمز عبور خود را وارد کنيد', reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text='بازگشت', callback_data='25')]]))

        zanjan_pass_turn[from_id] = 1
        zanjan_pass[from_id] = ''

    elif data == '27':
        bot.sendMessage(from_id, 'تلفن خود را وارد کنید(برای مثال +989121212121)', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="بازگشت", callback_data='30')]]))
        zanjan_ph_turn[from_id] = 1

    elif data=='29':
        bot.sendMessage(from_id, 'کد ارسال شده را وارد کنید(در انتهای ان صفر قراردهید)', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="بازگشت", callback_data='28')]
        ]
        ))
        '''if not client2[from_id]==0:
            if client2[from_id].is_connected():
                async def c():
                    await client2[from_id].disconnect()
                loop.run_until_complete(c())'''
        client2[from_id] = TelegramClient(str(from_id), api_id, api_hash, loop=loop)

        async def c():
            await client2[from_id].connect()
        loop.run_until_complete(c())
        async def m():
            global zanjan_code_turn
            print(zanjan_ph[from_id],1)
            zanjan_code_turn[from_id] = 1
            await client2[from_id].send_code_request(zanjan_ph[from_id])
        loop.run_until_complete(m())
    elif data == '28':
        bot.sendMessage(from_id, 'گزینه مورد نظر را انتخاب کنید',
                        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton(text="جستجوی دقیق", callback_data='8'),
                             InlineKeyboardButton(text="جستجوی جز به جز", callback_data='9')],
                            [InlineKeyboardButton(text="پایان", callback_data='10')]
                        ]
                        ))

        zanjan_pass_turn[from_id] = 0

            # with client:
            # client.loop.run_until_complete(main())

    elif data=='30':
        bot.sendMessage(from_id, 'گزینه مورد نظر را انتخاب کنید',
                        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton(text="جستجوی دقیق", callback_data='8'),
                             InlineKeyboardButton(text="جستجوی جز به جز", callback_data='9')],
                            [InlineKeyboardButton(text="پایان", callback_data='10')]
                        ]
                        ))

        zanjan_ph_turn[from_id] = 0

    elif data=='31':
        bot.sendMessage(from_id, 'تلفن خود را وارد کنید(برای مثال +989121212121)', reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text='بازگشت', callback_data='30')]]))

        zanjan_ph_turn[from_id] = 1
        zanjan_ph[from_id] = ''

    elif data == '24':
        bot.sendMessage(from_id, 'بازه زمانی ارسال را به ساعت وارد کنید')

        zanjant[from_id] = 1
    elif data == '32':
        bot.sendMessage(from_id, 'گزینه مورد نظر را انتخاب کنید',
                        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton(text="جستجوی دقیق", callback_data='8'),
                             InlineKeyboardButton(text="جستجوی جز به جز", callback_data='9')],
                            [InlineKeyboardButton(text="پایان", callback_data='10')]
                        ]
                        ))
        start[from_id]=1
        zanjan[from_id]=[]
        try:
            zanjan3[from_id] = list([])
        except IndexError:
            pass
TOKEN = '1003236552:AAG0Qmb9j52J6pN5qHIhCpX5S5MBCzjwHwg'
bot = telepot.Bot(TOKEN)
print('Listening ...')

bot.message_loop({'chat': on_chat_message, 'callback_query': on_callback_query}, run_forever=True)