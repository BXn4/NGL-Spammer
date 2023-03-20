# ╔╗╔╔═╗╦    ╔═╗╔═╗╔═╗╔╦╗╔╦╗╔═╗╦═╗
# ║║║║ ╦║    ╚═╗╠═╝╠═╣║║║║║║║╣ ╠╦╝
# ╝╚╝╚═╝╩═╝  ╚═╝╩  ╩ ╩╩ ╩╩ ╩╚═╝╩╚═ v4.2
# added log + message sent check

# The program was made for automation.
# This program violates NGL's terms of service, use it at your own risk!
# Also, I don't support using it for harassment

import time
import requests
from random import *
from datetime import datetime
import uuid
import argparse

parser = argparse.ArgumentParser(prog = 'NGL-Spammer', description='Flooding NGL accounts with questions.')
parser.add_argument("-a", "--account", help="Accounts separated with ','")
parser.add_argument("-q", "--question", help="Separate question(s) with ',' ('hi','what are you doing?')", type=str)
parser.add_argument("-r", "--repeat", help="Number of repetitions (0 = infinite)", type=int)
args = parser.parse_args()

fiokokszama = 0
jelenlegi = 0
i = 0
hossz = 0
ismetles = 0
x = 0
kerdesekszama = 0
holtartakerdesben = 0
kerdesekpot = ""
mennyitkuldott = []
kerdesek = []
fiokok = []
neverhave = []
haromwords = []
nevek = []
tbh = []
kissmarryblocklist = []
tizperde = []
rizzme = []
fiok = ""
eszkozid = ""
szavak = ""
mit = ""
gameslugkuld = ""
kerdesarg = ""
fiokarg = ""
utolso = ""
nemsikerult = 0
request = requests.Session()

def eszkozidgeneralas():
  eszkozid = uuid.uuid4().hex
  return "-".join([eszkozid[i:i+8] for i in range(0, 32, 8)])

def haromnevgeneralas():
  for k in range(3):
    szavak = (choice(nevek))
    kissmarryblocklist.append(szavak.replace('\n', ''))

eszkozidgeneralas()
eszkozid = eszkozidgeneralas()

try:
  with open("src/questions.txt", "r", encoding="UTF-8") as olvas:
    kerdesek = [sorok.strip() for sorok in olvas]
  with open("src/questions.txt", "r", encoding="UTF-8") as olvas:
    kerdesekpot = [sorok.strip() for sorok in olvas]
  with open("src/neverhave.txt", "r", encoding="UTF-8") as olvas:
    neverhave = [sorok.strip() for sorok in olvas]
  with open("src/3words.txt", "r", encoding="UTF-8") as olvas:
    haromwords = [sorok.strip() for sorok in olvas]
  with open("src/names.txt", "r", encoding="UTF-8") as olvas:
    nevek = [sorok.strip() for sorok in olvas]
  with open("src/tbh.txt", "r", encoding="UTF-8") as olvas:
    tbh = [sorok.strip() for sorok in olvas]
  with open("src/dealbreaker.txt", "r", encoding="UTF-8") as olvas:
    tizperde = [sorok.strip() for sorok in olvas]
  with open("src/rizzme.txt", "r", encoding="UTF-8") as olvas:
    rizzme = [sorok.strip() for sorok in olvas]
  with open("accounts.txt", "r") as olvas:
    fiokok = [sorok.strip() for sorok in olvas]
  mennyitkuldott = [1 for _ in range(len(fiokok))]
  fiokokszama = len(fiokok)

except (FileNotFoundError):
  print("File not found!")

datum = datetime.now()
ido = datum.strftime("%H:%M:%S")
print("NGL Spammer by: BXn4")
print("\n[{}] >> Starting\n".format(ido))

if args.account is None:
  hossz = 0
else:
  hossz = 1
  fiokarg = args.account
  kerdesarg = args.question
  if args.question is None:
    kerdesarg = " "
  ismetles = args.repeat
  if ismetles is None:
    ismetles = -1
  if ismetles == 0:
    ismetles = -1
  else:
    ismetles = args.repeat

if hossz > 0:
  fiokok = []
  kerdesek = []
  fiokok_split = fiokarg.split(',')
  fiokok.extend(fiokok_split)
  utolso = fiokok[-1]
  kerdesek_split = kerdesarg.split(',')
  kerdesek.extend(kerdesek_split)
  fiokokszama = len(fiokok)
  kerdesekszama = len(kerdesek)
  while x != ismetles:
    if i < 10:
      time.sleep(1)
      fiok = fiokok[jelenlegi]
      if '/' in fiok:
        if "rizzme" in fiok:
          fiok_split = fiok.split("/")[0]
          fiok = fiok_split
          mit = "Rizzme"
          gameslugkuld = "rizzme"
          if kerdesarg == " ":
            kerdes = (choice(rizzme))
          else:
            kerdes = kerdesek[holtartakerdesben]
        if "neverhave" in fiok:
          fiok_split = fiok.split("/")[0]
          fiok = fiok_split
          mit = "Neverhave"
          gameslugkuld = "neverhave"
          if kerdesarg == " ":
            szavak = ("I've never " + choice(neverhave))
            neverHave = szavak.replace('\n', '')
            kerdes = neverHave
            szavak = ""
          else:
            kerdes = kerdesek[holtartakerdesben]
        if "crush" in fiok:
          fiok_split = fiok.split("/")[0]
          fiok = fiok_split
          mit = "Crush"
          gameslugkuld = "yourcrush"
          if kerdesarg == " ":
            szavak += (choice(nevek))
            crush = szavak.replace('\n', '')
            kerdes = crush
            szavak = ""
          else:
            kerdes = kerdesek[holtartakerdesben]
        if "shipme" in fiok:
          fiok_split = fiok.split("/")[0]
          fiok = fiok_split
          mit = "Shipme"
          gameslugkuld = "shipme"
          if kerdesarg == " ":
            szavak += (choice(nevek))
            shipme = szavak.replace('\n', '')
            kerdes = shipme
            szavak = ""
          else:
            kerdes = kerdesek[holtartakerdesben]
        if "tbh" in fiok:
          fiok_split = fiok.split("/")[0]
          fiok = fiok_split
          mit = "TBH"
          gameslugkuld = "tbh"
          if kerdesarg == " ":
            szavak = choice(tbh)
            tbhKuld = szavak.replace('\n', '')
            kerdes = tbhKuld
            szavak = ""
          else:
            kerdes = kerdesek[holtartakerdesben]
        if "dealbreaker" in fiok:
          fiok_split = fiok.split("/")[0]
          fiok = fiok_split
          mit = "10/10"
          gameslugkuld = "dealbreaker"
          if kerdesarg == " ":
            szavak = choice(tizperde)
            tizperdeKuld = szavak.replace('\n', '')
            kerdes = tizperdeKuld
            szavak = ""
          else:
            kerdes = kerdesek[holtartakerdesben]
        if "kissmarryblock" in fiok:
          fiok_split = fiok.split("/")[0]
          fiok = fiok_split
          mit = "KMB"
          gameslugkuld = "kissmarryblock"
          if kerdesarg == " ":
            haromnevgeneralas()
            while any(kissmarryblocklist.count(i) > 1 for i in kissmarryblocklist):
              szavak = ""
              kissmarryblocklist = []
              haromnevgeneralas()
            haromnevgeneralas()
            for k in range(3):
              if k == 2:
                szavak += f"{kissmarryblocklist[k]}"
              else:
                szavak += f"{kissmarryblocklist[k]}, "
            kerdes = szavak
            kissmarryblocklist = []
            szavak = ""
          else:
            kerdes = kerdesek[holtartakerdesben]
        if "3words" in fiok:
          fiok_split = fiok.split("/")[0]
          fiok = fiok_split
          gameslugkuld = "3words"
          mit = "3 Words"
          if kerdesarg == " ":
            szavak += (choice(haromwords) + ", " + choice(haromwords) + ", " + choice(haromwords))
            haromszo = szavak.replace('\n', '')
            kerdes = haromszo
            szavak = ""
          else:
            kerdes = kerdesek[holtartakerdesben]
      else:
        gameslugkuld = ""
        mit = "Question"
        if kerdesarg == " ":
          kerdes = (choice(kerdesekpot))
        else:
          kerdes = kerdesek[holtartakerdesben]
      if holtartakerdesben == kerdesekszama - 1:
        holtartakerdesben = -1
      url = f"https://ngl.link/{fiok}"
      holtartakerdesben += 1

      fejresz = {
        "Referer": url,
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"
        }

      adat = {
        "username": fiok,
        "question": kerdes,
        "deviceId": eszkozid,
        "gameSlug": gameslugkuld,
        "referrer": ""
        }
      
      #print(eszkozid)
      elkuld = request.post("https://ngl.link/api/submit", headers=fejresz, data=adat)
      eszkozid = eszkozidgeneralas()
      if elkuld.status_code == 200:
        nemsikerult = 0;
        print("-> %s (%s) \n[%s] %s" % (fiokok[jelenlegi],mennyitkuldott[jelenlegi],mit,kerdes) + "\n")
        #print(elkuld)
        mennyitkuldott[jelenlegi] += 1
        i = i + 1
      else:
        nemsikerult = nemsikerult + 1
        if nemsikerult < 4:
          print("[{} ({}/3)] Failed! I'll try again after 20 seconds.\n".format(elkuld.status_code,nemsikerult))
          time.sleep(20)
        else:
          datum = datetime.now()
          datumido = datum.strftime("%Y-%m-%d")
          ido = datum.strftime("%H:%M")
          with open("logs/{}.txt".format(datumido), mode='a') as logfile:
            logfile.write("{}\nAccount: {}\nError: {} https://www.abstractapi.com/http-status-codes/{}\nNGL: https://ngl.link/{}\n\n".format(ido,fiok,elkuld.status_code,elkuld.status_code,fiok))
          print("[!!!] Failed! I continue with the next account.\nThe account is in the: logs/{}.txt file!\n".format(datumido))
          nemsikerult = 0;
          i = 10

    if (i == 10):
      eszkozid = eszkozidgeneralas()
      jelenlegi += 1
      if jelenlegi == fiokokszama:
        jelenlegi = 0
      datum = datetime.now()
      print("Next: -> " + fiokok[jelenlegi])
      ido = datum.strftime("%H:%M:%S")
      print("[{}] >> Intermission (2 mins)\n".format(ido))
      time.sleep(120)
      i = 0
      if ismetles != -1:
        if fiok == utolso:
          x += 1
          datum = datetime.now()
          ido = datum.strftime("%H:%M:%S")
          print("[%s] Number of repeats: %s/%s\n" % (ido,x,ismetles))
else:
  while True:
    if (i < 10):
      time.sleep(1)
      fiok = fiokok[jelenlegi].strip()
      if '/' in fiok:
        if "rizzme" in fiok:
          fiok = fiok.split("/")[0]
          mit = "Rizzme"
          gameslugkuld = "rizzme"
          szavak += (choice(rizzme))
          rizzmeKuld = szavak.replace('\n', '')
          kerdes = rizzmeKuld
          szavak = ""
        if "neverhave" in fiok:
          fiok = fiok.split("/")[0]
          mit = "Neverhave"
          gameslugkuld = "neverhave"
          szavak = ("I've never " + choice(neverhave))
          neverHave = szavak.replace('\n', '')
          kerdes = neverHave
          szavak = ""
        if "crush" in fiok:
          fiok = fiok.split("/")[0]
          mit = "Crush"
          gameslugkuld = "yourcrush"
          szavak += (choice(nevek))
          crush = szavak.replace('\n', '')
          kerdes = crush
          szavak = ""
        if "shipme" in fiok:
          fiok = fiok.split("/")[0]
          mit = "Shipme"
          gameslugkuld = "shipme"
          szavak += (choice(nevek))
          shipme = szavak.replace('\n', '')
          kerdes = shipme
          szavak = ""
        if "tbh" in fiok:
          fiok = fiok.split("/")[0]
          mit = "TBH"
          gameslugkuld = "tbh"
          szavak = choice(tbh)
          tbhKuld = szavak.replace('\n', '')
          kerdes = tbhKuld
          szavak = ""
        if "dealbreaker" in fiok:
          fiok = fiok.split("/")[0]
          mit = "10/10"
          gameslugkuld = "dealbreaker"
          szavak = choice(tizperde)
          tizperdeKuld = szavak.replace('\n', '')
          kerdes = tizperdeKuld
          szavak = ""
        if "kissmarryblock" in fiok:
          fiok = fiok.split("/")[0]
          haromnevgeneralas()
          while any(kissmarryblocklist.count(i) > 1 for i in kissmarryblocklist):
            szavak = ""
            kissmarryblocklist = []
            haromnevgeneralas()
          haromnevgeneralas()
          mit = "KMB"
          gameslugkuld = "kissmarryblock"
          for k in range(3):
            if k == 2:
              szavak += f"{kissmarryblocklist[k]}"
            else:
              szavak += f"{kissmarryblocklist[k]}, "
          kerdes = szavak
          kissmarryblocklist = []
          szavak = ""
        if "3words" in fiok:
          gameslugkuld = "3words"
          fiok = fiok.split("/")[0]
          mit = "3 Words"
          szavak += (choice(haromwords) + ", " + choice(haromwords) + ", " + choice(haromwords))
          haromszo = szavak.replace('\n', '')
          kerdes = haromszo
          szavak = ""
      else:
        gameslugkuld = ""
        mit = "Question"
        kerdes = choice(kerdesek)
      url = f"https://ngl.link/{fiok}"

      fejresz = {
        "Referer": url,
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent":
          "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"
      }

      adat = {
        "username": fiok,
        "question": kerdes,
        "deviceId": eszkozid,
        "gameSlug": gameslugkuld,
        "referrer": ""
      }
      elkuld = request.post("https://ngl.link/api/submit", headers=fejresz, data=adat)
      eszkozid = eszkozidgeneralas()
      if elkuld.status_code == 200:
        nemsikerult = 0;
        print("-> %s (%s) \n[%s] %s" % (fiokok[jelenlegi],mennyitkuldott[jelenlegi],mit,kerdes) + "\n")
        #print(elkuld)
        mennyitkuldott[jelenlegi] += 1
        i = i + 1
      else:
        nemsikerult = nemsikerult + 1
        if nemsikerult < 4:
          print("[{} ({}/3)] Failed! I'll try again after 20 seconds.\n".format(elkuld.status_code,nemsikerult))
          time.sleep(20)
        else:
          datum = datetime.now()
          datumido = datum.strftime("%Y-%m-%d")
          ido = datum.strftime("%H:%M")
          with open("logs/{}.txt".format(datumido), mode='a') as logfile:
            logfile.write("{}\nAccount: {}\nError: {} https://www.abstractapi.com/http-status-codes/{}\nNGL: https://ngl.link/{}\n\n".format(ido,fiok,elkuld.status_code,elkuld.status_code,fiok))
          print("[!!!] Failed! I continue with the next account.\nThe account is in the: logs/{}.txt file!\n".format(datumido))
          nemsikerult = 0;
          i = 10

    if (i == 10):
      eszkozid = eszkozidgeneralas()
      jelenlegi += 1
      if jelenlegi == fiokokszama:
        jelenlegi = 0
      datum = datetime.now()
      print("Next: -> " + fiokok[jelenlegi])
      ido = datum.strftime("%H:%M:%S")
      print("[{}] >> Intermission (2 mins)\n".format(ido))
      time.sleep(120)
      i = 0
