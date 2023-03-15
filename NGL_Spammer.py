# ╔╗╔╔═╗╦    ╔═╗╔═╗╔═╗╔╦╗╔╦╗╔═╗╦═╗
# ║║║║ ╦║    ╚═╗╠═╝╠═╣║║║║║║║╣ ╠╦╝
# ╝╚╝╚═╝╩═╝  ╚═╝╩  ╩ ╩╩ ╩╩ ╩╚═╝╩╚═ v4.1
# bug fixes

# The program was made for automation.
# This program violates NGL's terms of service, use it at your own risk!
# Also, I don't support using it for harassment

import time
import requests
from random import *
from datetime import datetime
import uuid
import argparse

parser = argparse.ArgumentParser(prog = 'NGL-Spammer', description='NGL fiókok elárasztása kérdésekkel.')
parser.add_argument("-f", "--fiok", help="A fiók(ok) megadása ,-vel")
parser.add_argument("-k", "--kerdes", help="A kérdés(ek) megadása ,-vel ('szia','mit csinálsz?')", type=str)
parser.add_argument("-i", "--ismetles", help="Az ismétlések száma (0 = végtelen)", type=int)
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
    with open("szovegek/kerdesek.txt", "r", encoding="UTF-8") as olvas:
        kerdesek = [sorok.strip() for sorok in olvas]
    with open("szovegek/kerdesek.txt", "r", encoding="UTF-8") as olvas:
        kerdesekpot = [sorok.strip() for sorok in olvas]
    with open("szovegek/neverhave.txt", "r", encoding="UTF-8") as olvas:
        neverhave = [sorok.strip() for sorok in olvas]
    with open("szovegek/3words.txt", "r", encoding="UTF-8") as olvas:
        haromwords = [sorok.strip() for sorok in olvas]
    with open("szovegek/nevek.txt", "r", encoding="UTF-8") as olvas:
        nevek = [sorok.strip() for sorok in olvas]
    with open("szovegek/tbh.txt", "r", encoding="UTF-8") as olvas:
        tbh = [sorok.strip() for sorok in olvas]
    with open("szovegek/dealbreaker.txt", "r", encoding="UTF-8") as olvas:
        tizperde = [sorok.strip() for sorok in olvas]
    with open("szovegek/rizzme.txt", "r", encoding="UTF-8") as olvas:
        rizzme = [sorok.strip() for sorok in olvas]
    with open("fiokok.txt", "r") as olvas:
        fiokok = [sorok.strip() for sorok in olvas]
    mennyitkuldott = [1 for _ in range(len(fiokok))]
    fiokokszama = len(fiokok)

except (FileNotFoundError):
  print("Nem található a fájl!")

datum = datetime.now()
ido = datum.strftime("%H:%M:%S")
print("NGL Spammer by: BXn4")
print("\n[{}] >> Kezdés\n".format(ido))

if args.fiok is None:
  hossz = 0
else:
  hossz = 1
  fiokarg = args.fiok
  kerdesarg = args.kerdes
  if args.kerdes is None:
    kerdesarg = " "
  ismetles = args.ismetles
  if ismetles is None:
    ismetles = -1
  if ismetles == 0:
    ismetles = -1
  else:
    ismetles = args.ismetles

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
            szavak = ("Én még sohasem " + choice(neverhave))
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
        mit = "Kérdés"
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
      print(eszkozid)
      elkuld = request.post("https://ngl.link/api/submit", headers=fejresz, data=adat)
      eszkozid = eszkozidgeneralas()
      if elkuld.status_code == 200:
        print("-> %s (%s) \n[%s] %s" % (fiokok[jelenlegi],mennyitkuldott[jelenlegi],mit,kerdes) + "\n")
        #print(elkuld)
        mennyitkuldott[jelenlegi] += 1
        i = i + 1
      else:
        print("[{}] Nem sikerült elküldeni. Várok 2 percet mielőtt újra megpróbálom\n".format(elkuld.status_code))
        time.sleep(120)

    if (i == 10):
      eszkozid = eszkozidgeneralas()
      jelenlegi += 1
      if jelenlegi == fiokokszama:
        jelenlegi = 0
      datum = datetime.now()
      print("Következő: -> " + fiokok[jelenlegi])
      ido = datum.strftime("%H:%M:%S")
      print("[{}] >> Szünet (2 perc)\n".format(ido))
      time.sleep(120)
      i = 0
      if ismetles != -1:
        if fiok == utolso:
          x += 1
          datum = datetime.now()
          ido = datum.strftime("%H:%M:%S")
          print("[%s] Ismétlések száma: %s/%s\n" % (ido,x,ismetles))
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
          szavak = ("Én még sohasem " + choice(neverhave))
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
        mit = "Kérdés"
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
        print("-> %s (%s) \n[%s] %s" % (fiokok[jelenlegi],mennyitkuldott[jelenlegi],mit,kerdes) + "\n")
        #print(elkuld)
        mennyitkuldott[jelenlegi] += 1
        i = i + 1
      else:
        print("[{}] Nem sikerült elküldeni. Várok 2 percet mielőtt újra megpróbálom\n".format(elkuld.status_code))
        time.sleep(120)

    if (i == 10):
      eszkozid = eszkozidgeneralas()
      jelenlegi += 1
      if jelenlegi == fiokokszama:
        jelenlegi = 0
      datum = datetime.now()
      print("Következő: -> " + fiokok[jelenlegi])
      ido = datum.strftime("%H:%M:%S")
      print("[{}] >> Szünet (2 perc)\n".format(ido))
      time.sleep(120)
      i = 0
