<h1 align="center">
 <br>
<img src="https://user-images.githubusercontent.com/78733248/212997444-e311a1e9-cfae-4217-8118-ac23512723a9.jpg" width="200"></a>
  <br>
  NGL Spammer
</h1>
<p align="center"><a href="https://github.com/BXn4/NGL-Spammer_en">EN</a> - <a href="https://github.com/BXn4/NGL-Spammer">HU</a></p>
<h4 align="center">Flooding NGL accounts with questions</h4>
<p align="center">
<p align="center">
  --> <a href="#how-it-works">How it works</a> ·
  <a href="#how-to-use">How To Use / Download</a> ·
  <a href="#replit">Replit</a>·
  <a href="#examples">Examples</a>·
    <a href="#support-me">Support me!</a> <--
</p>
<p align="center">
<img src="https://user-images.githubusercontent.com/78733248/213006672-89089652-3251-4fd1-9bb2-e3d3507903c7.gif" width=200><br><br><br></p></img>

## How it works
Allows NGL  accounts to be spammed with pre-written questions. The APP can handle maximum 15 questions, but it will only send 10 questions, because some questions didn't delivered. When it successfully sent the questions, the program waits 2  minutes (120 seconds) so that the site does not detect it as spam. After this time, it will send the question to the next account. When it reaches the end, it start from the beginning.

## How To Use
Tutorial: https://youtu.be/roLXTavyRkA<br>
First you need the NGL account name. <br> You cant find the name after the "@" character. Or in the url field.
If it differs, copy the name from the address bar of the browser, because the accounts can have the same name.
<img src="https://user-images.githubusercontent.com/78733248/213011344-bfaf61fa-9e02-4fe8-a70c-eeb99e19f341.png">
Once we have this, copy the name into the **accounts.txt**.
There is no limit to how many names you can enter!
Then you can start the program.
## Startup parameters
[-a ACCOUNT] [-q QUESTION] [-r REPEAT]
```bash
# Query parameters
$ python NGL-Spammer -h

# Parameters
# For e.g. python NGL-Spammer -a someone, someone/crush -q "hi","how are you?","What's up?" -r 10
# The program will send 'hi' and 'how are you' to 'someone' and 'someone/crush' 10 times repeat
# If the -q parameter is not specified, the questions will be sent according to the question type.
# If we don't specify the -r parameter, it will repeat indefinitely.
```

## Download
First of all you need [Git](https://git-scm.com), or you can download it from  [Releases](https://github.com/bxn4/ngl-spammer_en/releases) the latest release.
To run it download, and install [Python](https://www.python.org/), if it is not installed  it will won't work.

```bash
# Download with git
$ git clone https://github.com/bxn4/ngl-spammer_en

# Download required packages
$ pip install requests

# Then enter the folder and write the desired accounts in accounts.txt! (in case if you missed it)

# Entering the folder
$ cd ngl-spammer_en

# To run it
$ python NGL-Spammer.py

# If it wont works:
$ python3 NGL-Spammer.py
```

## Replit
Before you run it, check if there is a new release! I always upload it to Replit a little later, you can find out that in the comments.
If there is a new one, fork it!<br>You can run it here if you don't want to download it-> [Replit](https://replit.com/@BXn4/NGL-Spammeren#main.py) <br><br><a href="[https://replit.com/@BXn4/NGL-Spammeren#main.py](https://replit.com/@BXn4/NGL-Spammeren#main.py)" target="_blank"><img src="https://img.shields.io/badge/replit-667881?style=for-the-badge&logo=replit&logoColor=white" alt="Replit"></a>

## Examples
<img src="https://user-images.githubusercontent.com/78733248/216411554-c4521db5-0c03-4853-a487-ca1f76a92a54.png" width=220></img><img src="https://user-images.githubusercontent.com/78733248/216411573-38f7d70e-0c55-4108-b18c-cd81569e0047.png" width=220></img><img src="https://user-images.githubusercontent.com/78733248/216411578-8b03308e-b10e-4a8c-8120-9662b93b7086.png" width=220></img><br>
Contents of **questions.txt**:
```markdown
What brings you here today?
Have you ever cheated at a board game?
Do you have any pets?
```
Contents of **accounts.txt**:
```markdown
name
name/shipme
name/yourcrush
name/3words
name/tbh
name/dealbreaker
name/rizzme

# If you also copy the part after /, the question will be send accordingly to that part.
# Ex: someone/yourcrush --> Sends a person's name to crush.
```
Contents of **tbh.txt**:
```markdown
I wouldn't change a thing you are perfect just the way you are!
Your sense of humor is one of your best qualities I wouldn't change that
Your dress
```
Contents of **neverhave.txt**: (the first part will be: I've never...)
```markdown
stolen something
cheated on taxes
used drugs
```
## Support me!

<a href="https://www.buymeacoffee.com/bence912" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee">
