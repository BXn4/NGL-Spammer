<h1 align="center">
 <br>
<img src="https://user-images.githubusercontent.com/78733248/212997444-e311a1e9-cfae-4217-8118-ac23512723a9.jpg" width="200"></a>
  <br>
  NGL Spammer
</h1>
<p align="center"><a href="https://github.com/BXn4/NGL-Spammer_en">EN</a> - <a href="https://github.com/BXn4/NGL-Spammer">HU</a></p>
<h4 align="center">NGL fiókok elárasztása kérdésekkel</h4>
<p align="center">
<p align="center">
  --> <a href="#ismertető">Ismertető</a> ·
  <a href="#használat">Használat / letöltés</a> ·
  <a href="#replit">Replit</a>·
  <a href="#példák">Példák</a>·
    <a href="#támogatás">Támogatás</a> <--
</p>
<p align="center">
<img src="https://user-images.githubusercontent.com/78733248/213006672-89089652-3251-4fd1-9bb2-e3d3507903c7.gif" width=200><br><br><br></p></img>

## Ismertető
Az NGL fiókok spammelését teszi lehetővé előre megírt kérdésekkel. Az APP maxikum 15 kérdést tud kezelni, de csak 10 kérdést fog küldeni, mivel néhol a kérdések nem mentek át. Miután sikeresen elküldte a kérdéseket a program vár 2 percet  (120 másodperc) , hogy az oldal ne észlelje spammnek. Miután letelt ez a idő, a következő fiókra fogja küldeni a kérdést. Ha a végére ért, kezdi az elejétől.

## Használat
Segítség: https://youtu.be/roLXTavyRkA<br>
Elsőnek szükséged lesz az NGL-es névre. <br> A @jel utáni szövegre van szükség. Néhol eltér, ezért ellenőrizni kell, hogy a linkben is ugyanaz a név szerepel.
Ha eltér, akkor a böngésző címsorából másold ki a nevet, mivel egy neven lehet több fiók is.
<img src="https://user-images.githubusercontent.com/78733248/213011344-bfaf61fa-9e02-4fe8-a70c-eeb99e19f341.png">
Miután ez megvan a nevet másoljuk bele a **fiokok.txt**-be.
Nincs korlátozva, hogy hány nevet adhatsz meg!
Majd ezután lehet indítani a programot.
<br>
**Minden módosítás után ellenőrizni fogja, hogy a fiókok léteznek-e.** Ha van olyan fiók, ami nem létezik, akkor megkérdezi, majd törli azt a fiókot. Ha ezt a lépést mindig kiszeretnéd hagyni, akkor az **MD5.md5** fájl tartalmát írd át 0-ra!
## Indítási paraméterek

[-f FIOK] [-k KERDES] [-i ISMETLES]
```bash
# Paraméterek lekérdezése
$ python NGL-Spammer -h

# Kapcsolók
# Pl: python NGL-Spammer -f valaki,valaki/crush -k "szia hogy vagy? , Mi újság?" -i 10
# Ha nem adjuk meg a -k kapcsolót, akkor a kérdéstípushoz megfelelően küldi a kérdéseket.
# Ha nem adjuk meg az -i kapcsolót, akkor végtelen ideig ismétli.
```

## Letöltés
A letöltéshez szükséged lesz a [Git](https://git-scm.com)-re , vagy a  [Releases](https://github.com/BXn4/NGL-Spammer/releases)-nél letöltöd a legfrissebbet. 
A futtatáshoz [Python](https://www.python.org/) szükséges, ha nincs letöltve, akkor nem fog működni.
Python letöltése:
[Windows](https://www.python.org/downloads)-ra
```bash
# Ubuntu / Debian
$ sudo apt install python

# Fedora
$ sudo dnf install python
```
```bash
# Letöltés Git-el
$ git clone https://github.com/bxn4/ngl-spammer

# Szükséges csomagok letöltése
$ pip install requests

# Ezután lépj bele a mappába és írd bele a kívánt fiókokat a fiokok.txt-be! (ha kihagytad volna)

# Mappába lépés
$ cd ngl-spammer

# Indítás
$ python NGL-Spammer.py

# Ha nem jó, akkor próbáld így:
$ python3 NGL-Spammer.py
```

## Replit
Sajnos Repliten már nem működik.

## Példák
<img src="https://user-images.githubusercontent.com/78733248/214125065-899f63c2-f6cd-494f-965f-a074ae556124.png" width=200></img><img src="https://user-images.githubusercontent.com/78733248/214125075-f3d02804-2861-49e7-9452-a4142117f0f8.png" width=200></img><img src="https://user-images.githubusercontent.com/78733248/214125086-1046b5ba-53df-448a-a225-fafb1832d48c.png" width=200></img><br>
A **kérdések.txt** tartalma:
```markdown
Melyik női hírességet fogadnád el testvérednek?
Hány országban voltál már?
A coca-colás napocskán miért van napszemüveg? Mi süt a szemébe?
```
A **fiokok.txt** tartalma:
```markdown
valaki
valaki/shipme
valaki/yourcrush
valaki/3words
valaki/tbh
valaki/dealbreaker

# Ha a / utáni részt is kimásolod, akkor annak megfelelően fogja küldeni a kérdést.
# Pl.: valaki/yourcrush --> Elküldi egy személy nevét.
```
A **tbh.txt** tartalma:
```markdown
Szerintem előnyös lenne, ha több figyelmet fordítanál rám
Nem változtatnék rajtad semmit se, tökéletes vagy <3
Szeretném, ha több önbizalmad lenne
```
A **neverhave.txt** tartalma:
```markdown
voltam külföldön
voltam állatkertben
ettem pizzát
```
## Támogatás

<a href="https://www.buymeacoffee.com/bxn4" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee">