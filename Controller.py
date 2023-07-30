import os
import discord
import time

from dotenv import load_dotenv
import pyautogui, pydirectinput

# Set-up Client connection, get channel ID's for text and voice.
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
TXT_ID = os.getenv("TXT_CHANNEL_ID")
VC_ID = os.getenv("VOICE_CHANNEL_ID")

client = discord.Client(intents=discord.Intents.all())

# TODO: Initialize on_ready embed text and response for controls prompt.
# TODO: Allow to read from CSV file to customize control, and allow versatile controls_desc to reflect new control schemes
controls_desc = ("__**Controls**__: \n " +
                 "**Move Up:** u \n" +
                 "**Move Down:** d \n" +
                 "**Move Left:** l \n" +
                 "**Move Right:** r \n" +
                 "**Z:** z \n" +
                 "**X:** x \n" +
                 "**C:** c \n"
                )

# Hashmap to correspond command with keycode
control_map = {
    "u": "up",
    "d": "down",
    "l": "left",
    "r": "right",
    "z": "z",
    "x": "x",
    "c": "c"
}

# Can adjust time a key is held down for 
hold_time = 0.5

txt_channel, vc_channel = None, None

@client.event
async def on_ready():
    # Set up channel references
    txt_channel = client.get_channel(int(TXT_ID))
    vc_channel = client.get_channel(int(VC_ID))

    print("Controller is connected!")
    embed = discord.Embed(title="Controller Connected!", description=f"*Connected to text channel:* **{txt_channel.name}** \n *Connected to voice channel:* **{vc_channel.name}**",color=discord.Color.dark_green())
    await txt_channel.send(embed=embed)
    await txt_channel.send(controls_desc)


@client.event
async def on_message(message):
    # Restrict response to messages only within dedicated channel
    if message.channel.id != int(TXT_ID) or message.author.voice.channel.id != int(VC_ID):
        return
    
    # Avoid message/input loop
    if message.author == client.user:
        return
    
    # Print control scheme with commands
    if message.content == "controls":
        await message.channel.send(controls_desc)

    # Interface input with controls to control host game
    if message.content in control_map:
        with pydirectinput.press(control_map[message.content]):
            time.sleep(hold_time)
        
        

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
    

