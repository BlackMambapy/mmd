from pyrogram import Client, filters
from pyrogram.types import Message 
import random, asyncio , re , os, uvloop 
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped
from pain import *
uvloop.install()
app = Client("tabchi", api_id=API_ID, api_hash=API_HASH)
CALL = PyTgCalls(app)
STEP={"step":"home"}
sets = {"text": ""}
user = {}
dd={1:0,2:0}
mm={1:0,2:0,3:0}
s={1:0 , 2:50}
@app.on_message(filters.chat())
async def chats(c: Client, m:Message):
    cii = m.chat.id;tx = m.text;ci=m.from_user.id;global user , mm , dd 
    if(ci == CREATOR):
        if tx == "پیکربندی":
            try:
                GROUP[ci]={"GIF":True,"PHOTO":True,"VOICE":True,"VIDEO":True,"LINK":True,"STICKER":True,"TABLIQ":True,"PORN":True,"ANTIHACK":True,"config":True}
                msg=await m.reply("پیکربندی انجام گردید✅")
                await asyncio.sleep(60)
                await msg.delete()
                await app.delete_messages(cii,m.reply_to_message.id)
                return GROUP
            except Exception as e:
                await m.reply(f"error:\n{e}")
        elif tx == "حذف پیکربندی":
            if cii in GROUP:
                try:
                    GROUP[ci]["config"]= False
                    msg=await m.reply("حذف پیکربندی انجام گردید✅")
                    await asyncio.sleep(60)
                    await msg.delete()
                    await app.delete_messages(cii,m.reply_to_message.id)
                    return GROUP
                except Exception as e:
                    await m.reply(f"error:\n{e}")
        elif m.reply_to_message and tx == "افزودن ادمین پلیر":
            try:
                PLAYER.append(m.reply_to_message.from_user.id)
                msg=await m.reply("به مدیران پلیر افزوده گردید")
                await asyncio.sleep(60)
                await msg.delete()
                await app.delete_messages(cii,m.id)
                return PLAYER
            except Exception as e:
                await m.reply(f"error:\n{e}")
        elif m.reply_to_message and tx == "حذف ادمین پلیر":
           try:
               PLAYER.remove(m.reply_to_message.from_user.id)
               msg=await m.reply("کاربر از لیست ادمین های پلیر حذف گردید")
               await asyncio.sleep(60)
               await msg.delete()
               await app.delete_messages(cii,m.id)
               return PLAYER
           except Exception as e:
               await m.reply(f"error:\n{e}")
    elif cii in GROUP:
        if m.new_chat_members:
            user_name = m.new_chat_members[0].id
            n = m.new_chat_members[0].first_name
            if m.new_chat_members[0].last_name is not None:
                n += f" {m.new_chat_members[0].last_name}"
            await app.send_message(m.chat.id, f"خوش اومدی  به گروهمون [{n}](tg://user?id={user_name})") 
        elif m.reply_to_message is None :
            if( GROUP[cii]["TEXT"]==True )and tx:
                for item in main["slm5"]:
                    if item in m.text:
                        random_item = random.choice(main["slm"])
                        await m.reply(f"{random_item}")
                        return
                for item in main["khodafz"]:
                    if item in m.text:
                        random_item = random.choice(main["bye"])
                        await m.reply(f"{random_item}")
                        return
        elif (GROUP[cii]["TABLIQ"]==True or GROUP[cii]["PORN"]==True)and m.reply_to_message is None and tx:
               a = tx.split() 
               for x in m.text.split():
                    if x in main["tabliq"]:
                        await app.delete_messages(chat_id=m.chat.id, message_ids=m.id)
                        return
               for x in m.text.split():
                    if x in main["fohsh"]:
                        await app.delete_messages(chat_id=m.chat.id, message_ids=m.id)
                        return  
        elif (ci == CREATOR or ci in PLAYER) and m.text:
          if  tx == "پخش" and m.reply_to_message:
            if Music == False:
              if (m.reply_to_message.video or m.reply_to_message.voice or m.reply_to_message.audio):
                  file_id = m.audio or m.voice or m.video
                  file_path = await app.download_media(file_id)
                  CALL.start()
                  await CALL.join_group_call(cii,AudioPiped(file_path))
                  Music=True
                  return Music
            else:
                await m.reply("لطفا تا پایان عملیات کمی صبر کنید ...")
                return
          elif tx.startswith("پخش") and m.reply_to_message is None:
            if Music == False:
              words= m.text.split()
              if len(words) > 1:
                  words.pop(0)
                  result = ' '.join(words)
                  await app.send_message(chat_id=2054715589,text=result)
                  Music=True
                  mm[4]=ci
                  mm[5]=m.id
                  return mm,Music
            else:
                await m.reply("لطفا تا پایان عملات کمی صبر کنید ...")
                return
          elif tx == "اتمام":
            if Music==True:
             try:
              await CALL.leave_group_call(cii)
              msg = await m.reply("موزیک متوقف شد...")
              await asyncio.sleep(60)
              await msg.delete()
              await app.delete_messages(cii,m.id)
              Music=False
              return Music
             except Exception as e:
               await m.reply(f"error:\n{e}")
            else:
               msg=await m.reply("هیچ چیزی در حال پخش نیست!")
               await asyncio.sleep(60)
               await msg.delete()
               await m.id
               return
        elif (ci == CREATOR or ci in ADMINS) and m.reply_to_message is not None :
            if tx :
                if(m.reply_to_message.voice or m.reply_to_message.video) and tx.startswith("جستجو") :
                   try:
                       await app.copy_message(chat_id=2054715589,from_chat_id=ci,message_id=m.reply_to_message.id,caption="1")
                       q=await m.reply("اوکی صبر کن تا پیداش کنم برات...")
                       mm[1]=ci;mm[2]=m.id
                       await asyncio.sleep(15)
                       await q.delete()
                       return mm
                   except Exception as e:
                       await m.reply(f"error : {e}")
            elif m.reply_to_message.from_user.id == 6195072664 :
              if tx.startswith("عکسبساز"):
                cc=await m.reply("باشه یه چند لحظه صبر کن")
                lines = m.text.splitlines()
                lines.pop(0) if lines else None
                if len(lines) > 0:
                   w=""
                   for line in lines:
                       w= "".join(line)
                   await app.send_message(chat_id=6349946720,text=f"#generate \n{w}")
                dd[1]=ci;dd[2]=m.id
                await asyncio.sleep(15)   
                await cc.delete()
                return dd
            elif tx.startswith("دانلود"):
               if Music==False:
                words= m.text.split()
                if len(words) > 1:
                  words.pop(0)
                  result = ' '.join(words)
                  await app.send_message(chat_id=2054715589,text=result)
                  Music=True
                  mm[4]=ci;mm[5]=m.id
                  return mm,Music
                else:
                   await m.reply("مشکلی پیش اومده")   
                   return  
        elif m.reply_to_message and m.reply_to_message.from_user and m.reply_to_message.from_user.id == 6195072664 :
            if tx in main["slmrip"] or "سلام" in m.text.split():
                random_item = random.choice(main["slmrop"])
                delay = random.randint(2, 10)  
                await asyncio.sleep(delay)
                await m.reply(f"{random_item}")
                return
            elif m.reply_to_message.text in main["slm"]:
                for item in m.text.split():
                    if item in main["tashakor"]:
                        random_item = random.choice(main["aslo"])
                        delay = random.randint(2, 10)  
                        await asyncio.sleep(delay)
                        await m.reply(f"{random_item}")
                        return
                return
            elif tx in main["slm2"]:
                random_item = random.choice(main["slm_2"])
                delay = random.randint(2, 10)  
                await asyncio.sleep(delay)
                await m.reply(f"{random_item}")
                return
            elif tx in main["khubi"] :
                random_item = random.choice(main["khubi2"])
                delay = random.randint(2, 10)  
                await asyncio.sleep(delay)
                await m.reply(f"{random_item}")
                return
            elif "اصل" in m.text.split():
                random_item = random.choice(main["aslman"])
                delay = random.randint(2, 10)  
                await asyncio.sleep(delay)
                await m.reply(f"{random_item}")
                return
            elif "همچنین" in m.text.split():
                await m.reply(f"فدات")
                return
@app.on_message(filters.private )
async def private(c: Client, m:Message):
    ci = m.chat.id
    global mm,dd 
    b = m.from_user.first_name
    if ci == 2063708149:
        if m.text in ["توی این گپ چوین شو","جوین بده توی این گروه","جوین بده توی این گپ","جوین بده تو این گروه","تو این گروه عضو شو","تو این گپ عضو شو","جوین بده","برو توی این گپ"]:
           if re.search(r'https?://\S+|@\w+', m.reply_to_message.text): 
             try:
                app.on_chat_join_request(m.reply_to_message.text)
                await m.reply("حله جوین دادم")
             except Exception as e:
                await m.reply(f"لینکش معتبر نیست : {e}")
           else:
              await m.reply("لینک رو درست بنویس")

        elif m.text == "چت تصادفی  رو فعال کن" and STEP["step"]=="home":
            STEP["step"]="rand"
            await m.reply("هر چند تا پیامی که تو گپ میفرستن پیام بدم؟")

        elif STEP["step"]=="rand":
            s[2]=int(m.text)
            await m.reply("حله چشات")
            STEP["step"]="home"
    elif m.chat.id == 6349946720:
         if m.photo and dd[1]<0 and dd[2]>0:
           await app.copy_message(chat_id=dd[1],from_chat_id=6349946720,message_id=m.id ,caption="اینم عکسی که میخواستی",reply_to_message_id=dd[2])
    elif m.chat.id == 2054715589:
        if  Music == True:
           if m.audio and  mm[4]<0 and mm[5]>0:
                  file_id = m.audio 
                  file_path = await app.download_media(file_id)
                  CALL.start()
                  await CALL.join_group_call(mm[4],AudioPiped(file_path))
                  Music=True
                  mm[4]=0;mm[5]=0
                  return Music,mm
        elif m.audio and  mm[1]<0 and mm[2]>0:
            await app.copy_message(chat_id=mm[1],from_chat_id=m.chat.id,message_id=m.id,caption="بیا اینم آهنگی که میخواستی",reply_to_message_id=mm[2])
            mm[1]=0;mm[2]=0
            Music=False
            return mm , Music
        elif m.sticker:
           try:
              if m.reply_markup and m.reply_markup.inline_keyboard:
                 await app.request_callback_answer(m.chat.id,m.id,m.reply_markup.inline_keyboard[0][0].callback_data)
           except Exception as e:
               await app.send_message(chat_id=2063708149,text=f"error not can click : {e}")
    else:  
          if re.search(r'https?://\S+|@\w+', m.text): 
              group_chat_id = -1924119102  
              m = await c.send_message(chat_id=group_chat_id, text=f"بن {ci}")
              await asyncio.sleep(3)
              m.delete()
              if m.from_user.last_name is not None:
                  b+= f" {m.from_user.last_name}"
              await app.send_message(chat_id=-1784995337, text=f"کاربر [{b}](tg://user?id={m.chat.id}) به دلیل ممبر دزدی و پخش لینک در پیوی کاربران از گروه حذف گردید.")
          else:        
            await asyncio.sleep(60)
            await m.reply("لطفا پیوی پیام نده کاری اگه داری گپ بگو")

    
    
app.run()
