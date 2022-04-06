# OwOBot
Discord bot originally created for OwOZone, written in Python.

## Features & Purpose
This bot is developed for Kitty's dedicated *and rather lewd* Discord server,
and will, in the future, have a number of features as time progresses. At the time of writing,
the bot has the following features.

- Bot help (ofc)
- Fetch images from the nekos.life api, both sfw and nsfw.
- Fetch specific types of lewd images.
- Purge messages by number amount if the user requesting it has the Administrator permission.

## Requirements
The bot requires Python3 to run, and the following modules must (for now) be installed by hand:
- aiohttp
- discord
- requests
- mysql

## Installation
To install and run this bot, do the following:
1. Create a new folder somewhere you won't forget, then using a terminal, open a command prompt.
2. `git clone https://github.com/Bloodfallen/OwOBot.git .`
3. Run the following commands:
```bash
python -m pip install aiohttp
python -m pip install discord
python -m pip install requests
python -m pip install mysql
```
4. Create a new file named `discToken.py`
5. Edit the new `discToken.py` file you have created, and add the following variable:
`botToken = ""`, ensure you place *your discord bot token* in this variable.
6. Ensure Python is added to your "PATH", and execute `python ./main.py`
7. ???
8. Profit.

## License
This application/bot is licenced under the MIT General Purpose license, which you can view [here](https://opensource.org/licenses/MIT), and is Copyright (C) Exile, 2022. 