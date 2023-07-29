import os
import discord

from dotenv import load_dotenv
import pyautogui, pydirectinput

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")

client.run(TOKEN)


# Time for client to setup game windowz
# pyautogui.sleep(3)
# while True:
#     pyautogui.press('down')
#     pyautogui.sleep(1)
#     pydirectinput.press('z')
#     pyautogui.sleep(2)
#     pydirectinput.press('z')
#     pyautogui.sleep(1)
    

