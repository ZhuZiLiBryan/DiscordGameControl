import os
import discord

from dotenv import load_dotenv
import pyautogui, pydirectinput

# Set-up Client connection, get channel ID's for text and voice.
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
TXT_ID = os.getenv("TXT_CHANNEL_ID")
VC_ID = os.getenv("VOICE_CHANNEL_ID")

client = discord.Client(intents=discord.Intents.all())

# TODO: Initialize on_ready embed text and response for controls prompt.
controls_desc = ("__**Controls**__: \n " +
                 ""
                )

txt_channel, vc_channel = None, None

@client.event
async def on_ready():
    # Set up channel references
    txt_channel = client.get_channel(int(TXT_ID))
    vc_channel = client.get_channel(int(VC_ID))
    print(type(txt_channel))

    print("Controller is connected!")
    embed = discord.Embed(title="Controller Connected!", description=f"*Connected to text channel:* **{txt_channel.name}** \n *Connected to voice channel:* **{vc_channel.name}**",color=discord.Color.dark_green())
    await txt_channel.send(embed=embed)


@client.event
async def on_message(message):
    # Restrict response to messages only within dedicated channel
    if message.channel.id != int(TXT_ID):
        return
    
    # Avoid message/input loop
    if message.author == client.user:
        return
    
    print(message.content)

    # TODO: Interface input with controls to control host game
    # print("Interface with pydirect input to move character in game")

# Error handling when received unhandled message.
@client.event
async def on_error(event, *args, **kwargs):        
    with open("errors.log", "a") as f:
        if event == "on_message":
            f.write(f"Error with message: {args[0]}\n")
        else:
            raise # Resort to default error handler



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
    

