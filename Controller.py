import os
import discord

from dotenv import load_dotenv
import pyautogui, pydirectinput

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print("Controller is connected!")
    print("Automatically print controls with their corresponding text commands here")

@client.event
async def on_message(message):
    print("Read user input, only respond if coming from a dedicated channel")
    print("Interface with pydirect input to move character in game")

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
    

